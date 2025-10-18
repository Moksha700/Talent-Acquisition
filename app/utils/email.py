from __future__ import annotations

import os
import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List, Optional
from dataclasses import dataclass

from ..config import CONFIG


@dataclass
class EmailResult:
    candidate_id: str
    email_address: str
    email_type: str  # "interview" or "rejection"
    success: bool
    error_message: Optional[str] = None


def extract_email_from_text(text: str) -> Optional[str]:
    """Extract email address from resume text using regex."""
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, text)
    return emails[0] if emails else None


def create_interview_email(candidate_name: str, role_title: str, department: str, fit_score: float) -> str:
    """Create interview invitation email template."""
    return f"""
Dear {candidate_name},

Congratulations! We are pleased to inform you that you have been shortlisted for the position of {role_title} in the {department} department.

Your application stood out among many candidates, and we were particularly impressed by your qualifications and experience. Your fit score of {fit_score:.2%} indicates a strong alignment with our requirements.

We would like to invite you for an interview to discuss your background and how you can contribute to our team. Our HR team will contact you within the next few business days to schedule a convenient time.

We look forward to meeting you and learning more about your experience and aspirations.

Best regards,
{CONFIG.from_name}
Talent Acquisition Team
"""


def create_rejection_email(candidate_name: str, role_title: str, department: str) -> str:
    """Create rejection email template."""
    return f"""
Dear {candidate_name},

Thank you for your interest in the {role_title} position in the {department} department and for taking the time to submit your application.

After careful consideration of all applications, we have decided to move forward with other candidates whose qualifications more closely match our current needs for this particular role.

We appreciate your interest in our organization and encourage you to apply for future opportunities that may be a better fit for your background and experience.

We wish you the best of luck in your job search.

Best regards,
{CONFIG.from_name}
Talent Acquisition Team
"""


def send_email(to_email: str, subject: str, body: str) -> bool:
    """Send email using SMTP configuration."""
    if not CONFIG.email_enabled:
        return True
    
    try:
        # Get email credentials from environment variables
        smtp_username = os.getenv('EMAIL_USER', CONFIG.smtp_username)
        smtp_password = os.getenv('EMAIL_PASS', CONFIG.smtp_password)
        from_email = os.getenv('FROM_EMAIL', CONFIG.from_email)
        
        if not all([smtp_username, smtp_password, from_email]):
            # Silent demo mode - no console output
            return True
        
        # Create message
        msg = MIMEMultipart()
        msg['From'] = f"{CONFIG.from_name} <{from_email}>"
        msg['To'] = to_email
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Send email
        with smtplib.SMTP(CONFIG.smtp_server, CONFIG.smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.send_message(msg)
        
        return True
        
    except Exception as e:
        # Silent error handling
        return False


def send_automatic_emails(candidates: List, matches: List, role_title: str, department: str) -> List[EmailResult]:
    """Send automatic emails based on fit scores."""
    results = []
    
    # Create candidate lookup
    candidate_lookup = {c.id: c for c in candidates}
    
    for match in matches:
        candidate_id = match['candidate_id']
        fit_score = match['fit_score']
        candidate = candidate_lookup.get(candidate_id)
        
        if not candidate:
            continue
            
        # Extract email from resume text
        email_address = candidate.email or extract_email_from_text(candidate.resume_text)
        
        if not email_address:
            results.append(EmailResult(
                candidate_id=candidate_id,
                email_address="",
                email_type="none",
                success=False,
                error_message="No email address found"
            ))
            continue
        
        # Determine email type based on threshold
        if fit_score >= CONFIG.interview_threshold:
            email_type = "interview"
            subject = f"Interview Invitation - {role_title} Position"
            body = create_interview_email(candidate.name, role_title, department, fit_score)
        elif fit_score < CONFIG.rejection_threshold:
            email_type = "rejection"
            subject = f"Application Update - {role_title} Position"
            body = create_rejection_email(candidate.name, role_title, department)
        else:
            # Middle ground - no automatic email
            results.append(EmailResult(
                candidate_id=candidate_id,
                email_address=email_address,
                email_type="none",
                success=True,
                error_message="Fit score in middle range - no automatic email sent"
            ))
            continue
        
        # Send email
        success = send_email(email_address, subject, body)
        
        results.append(EmailResult(
            candidate_id=candidate_id,
            email_address=email_address,
            email_type=email_type,
            success=success,
            error_message=None if success else "Failed to send email"
        ))
    
    return results
