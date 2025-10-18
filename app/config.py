from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass
class AppConfig:
    data_dir: Path = Path("data")
    output_dir: Path = Path("outputs")
    candidate_dir: Path = Path("data/candidates")
    roles_dir: Path = Path("data/roles")
    use_langchain: bool = False
    use_crewai: bool = False
    
    # Email configuration
    email_enabled: bool = True
    smtp_server: str = "smtp.gmail.com"
    smtp_port: int = 587
    smtp_username: str = ""  # Set via environment variable EMAIL_USER
    smtp_password: str = ""  # Set via environment variable EMAIL_PASS
    from_email: str = ""  # Set via environment variable FROM_EMAIL
    from_name: str = "Talent Acquisition Team"
    
    # Fit score threshold for automatic emails
    interview_threshold: float = 0.3  # Candidates above this score get interview emails
    rejection_threshold: float = 0.1  # Candidates below this score get rejection emails


CONFIG = AppConfig()

