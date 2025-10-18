#!/usr/bin/env python3
"""
Email Setup Test Script
"""
import os
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from app.utils.email import send_email

def test_email_setup():
    """Test if email credentials are properly set"""
    print("=== Email Setup Test ===\n")
    
    # Check environment variables
    email_user = os.getenv('EMAIL_USER')
    email_pass = os.getenv('EMAIL_PASS')
    from_email = os.getenv('FROM_EMAIL')
    
    print("1. Checking environment variables...")
    print(f"   EMAIL_USER: {'SET' if email_user else 'NOT SET'}")
    print(f"   EMAIL_PASS: {'SET' if email_pass else 'NOT SET'}")
    print(f"   FROM_EMAIL: {'SET' if from_email else 'NOT SET'}")
    
    if not all([email_user, email_pass, from_email]):
        print("\n❌ Email credentials not properly set!")
        print("\nTo fix this, run one of these commands:")
        print("\nPowerShell:")
        print('$env:EMAIL_USER="your-email@gmail.com"')
        print('$env:EMAIL_PASS="your-app-password"')
        print('$env:FROM_EMAIL="your-email@gmail.com"')
        print("\nCommand Prompt:")
        print('set EMAIL_USER=your-email@gmail.com')
        print('set EMAIL_PASS=your-app-password')
        print('set FROM_EMAIL=your-email@gmail.com')
        return False
    
    print("\n✅ All email credentials are set!")
    
    # Test sending an email
    print("\n2. Testing email sending...")
    test_result = send_email(
        to_email="test@example.com",
        subject="Test Email from TalentAcquisition",
        body="This is a test email to verify your SMTP setup is working correctly."
    )
    
    if test_result:
        print("✅ Email test successful!")
        print("🎉 Your email setup is working correctly!")
        print("\nYou can now run the TalentAcquisition app and it will send real emails.")
        return True
    else:
        print("❌ Email test failed!")
        print("Check your credentials and try again.")
        return False

if __name__ == "__main__":
    success = test_email_setup()
    
    if success:
        print("\n🚀 Ready to send real emails!")
        print("Run: streamlit run app/ui.py")
    else:
        print("\n🔧 Please fix the email setup and try again.")



