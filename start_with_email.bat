@echo off
echo Setting up email environment variables...

REM Set your Gmail credentials here
set EMAIL_USER=your-email@gmail.com
set EMAIL_PASS=your-app-password
set FROM_EMAIL=your-email@gmail.com

echo Email credentials set!
echo EMAIL_USER: %EMAIL_USER%
echo FROM_EMAIL: %FROM_EMAIL%

echo.
echo Starting TalentAcquisition application...

cd /d "C:\Users\Mokshagna\Downloads\TalentAcquisition (3)\TalentAcquisition"
call .venv\Scripts\activate
streamlit run app/ui.py

pause



