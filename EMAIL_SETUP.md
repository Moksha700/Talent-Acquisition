# Email Configuration Guide

## Setting Up Email Credentials

To enable automatic email sending, you need to set up your email credentials as environment variables.

### For Gmail (Recommended)

1. **Enable 2-Factor Authentication** on your Gmail account
2. **Generate an App Password**:
   - Go to Google Account settings
   - Security → 2-Step Verification → App passwords
   - Generate a password for "Mail"
3. **Set Environment Variables**:

```bash
# Windows PowerShell
$env:EMAIL_USER="your-email@gmail.com"
$env:EMAIL_PASS="your-app-password"
$env:FROM_EMAIL="your-email@gmail.com"

# Windows Command Prompt
set EMAIL_USER=your-email@gmail.com
set EMAIL_PASS=your-app-password
set FROM_EMAIL=your-email@gmail.com

# Linux/Mac
export EMAIL_USER="your-email@gmail.com"
export EMAIL_PASS="your-app-password"
export FROM_EMAIL="your-email@gmail.com"
```

### For Other Email Providers

Update the SMTP settings in `app/config.py`:

```python
smtp_server: str = "smtp.your-provider.com"
smtp_port: int = 587  # or 465 for SSL
```

### Testing Email Functionality

1. **Without Credentials**: The system will show "[EMAIL DISABLED]" messages in the console
2. **With Credentials**: Emails will be sent automatically based on fit scores

### Email Thresholds

- **Interview Threshold** (default: 0.3): Candidates with fit score ≥ this threshold receive interview emails
- **Rejection Threshold** (default: 0.1): Candidates with fit score < this threshold receive rejection emails
- **Middle Range**: Candidates between thresholds receive no automatic email

### Email Templates

- **Interview Email**: Congratulatory message with fit score and next steps
- **Rejection Email**: Professional rejection notice encouraging future applications

### Troubleshooting

- **No emails sent**: Check environment variables are set correctly
- **Authentication failed**: Verify app password and 2FA settings
- **No email addresses found**: Ensure resumes contain valid email addresses
