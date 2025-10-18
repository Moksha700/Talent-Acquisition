# 🤖 Agentic AI Talent Acquisition & Faculty Management System

A comprehensive, local-first Python application that demonstrates an intelligent multi-agent pipeline for academic faculty recruitment and ongoing development. The system uses classic NLP and scikit-learn for an out-of-the-box experience, with optional integrations for LangChain and CrewAI.

## ✨ Features

- **Multi-Agent Pipeline**: Sourcing, Screening, Interview, Onboarding, and Development agents
- **Intelligent Resume Processing**: Supports CSV/JSON/text/PDF files with automatic email extraction
- **Automatic Role Classification**: AI-powered role creation from job titles
- **Smart Candidate Matching**: TF-IDF embeddings with fit score calculation
- **Automatic Email System**: Interview invitations and rejection notices based on fit scores
- **Interactive Web UI**: Streamlit-based dashboard with real-time analysis
- **Comprehensive Reporting**: JSON and Markdown export capabilities

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/talent-acquisition.git
   cd talent-acquisition
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv .venv
   
   # Windows
   .venv\Scripts\activate
   
   # Linux/Mac
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   python -m nltk.downloader punkt stopwords
   ```

4. **Run the application**
   ```bash
   # CLI Demo
   python -m app.cli demo
   
   # Web UI
   streamlit run app/ui.py
   ```

## 📧 Email Configuration (Optional)

To enable automatic email sending:

1. **Set environment variables**
   ```bash
   # Windows PowerShell
   $env:EMAIL_USER="your-email@gmail.com"
   $env:EMAIL_PASS="your-app-password"
   $env:FROM_EMAIL="your-email@gmail.com"
   
   # Linux/Mac
   export EMAIL_USER="your-email@gmail.com"
   export EMAIL_PASS="your-app-password"
   export FROM_EMAIL="your-email@gmail.com"
   ```

2. **Gmail Setup**
   - Enable 2-Factor Authentication
   - Generate App Password (not regular password)
   - Use App Password as EMAIL_PASS

## 🎯 Usage

### Web Interface
1. Open `http://localhost:8501` in your browser
2. Upload candidate resumes via sidebar
3. Use "Define Role" to create or classify job positions
4. Set email thresholds for automatic notifications
5. Click "Compute Fit & Generate Report"
6. View results in the dashboard

### Command Line Interface
```bash
# Run end-to-end demo
python -m app.cli demo

# Ingest candidates
python -m app.cli ingest --data ./data

# Match candidates to role
python -m app.cli match --role ./data/roles/cs_assistant_professor.yaml --out ./outputs

# Generate report
python -m app.cli report --out ./outputs
```

## 📁 Project Structure

```
app/
├── __init__.py
├── cli.py                 # Command-line interface
├── config.py             # Configuration settings
├── data_models.py        # Data structures
├── embeddings.py         # Text embedding utilities
├── orchestrator.py       # Main orchestration logic
├── parsing.py            # Resume parsing
├── role_classifier.py    # Automatic role creation
├── scoring.py           # Candidate scoring
├── ui.py                # Streamlit web interface
├── agents/              # Multi-agent system
│   ├── sourcing.py
│   ├── screening.py
│   ├── interview.py
│   ├── onboarding.py
│   └── development.py
├── utils/               # Utility functions
│   ├── io.py
│   ├── text.py
│   └── email.py         # Email functionality
└── reports/             # Report generation
    └── generator.py

data/
├── candidates/          # Resume files
└── roles/              # Job role definitions

outputs/                 # Generated reports
```

## 🔧 Configuration

### Email Settings
- **Interview Threshold**: Candidates above this score receive interview emails (default: 0.3)
- **Rejection Threshold**: Candidates below this score receive rejection emails (default: 0.1)

### Supported File Formats
- **Resumes**: `.txt`, `.pdf`, `.json`
- **Roles**: `.yaml`, `.yml`, `.json`

## 🧠 AI Features

### Role Classification
The system automatically generates comprehensive role profiles from job titles:
- Department detection
- Required/preferred skills
- Research focus areas
- Teaching requirements

### Candidate Matching
- TF-IDF based similarity scoring
- Multi-criteria evaluation
- Strength/risk analysis
- Automated next steps

### Email Automation
- Professional email templates
- Automatic email extraction from resumes
- Threshold-based email sending
- SMTP integration

## 📊 Sample Data

The repository includes sample data:
- Candidate profiles with email addresses
- Pre-defined role templates
- Example reports and outputs

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with Python, Streamlit, and scikit-learn
- Optional integrations with LangChain and CrewAI
- Inspired by modern AI-powered recruitment systems

## 📞 Support

For questions or support, please open an issue on GitHub.

---

**Note**: This system emphasizes fairness and transparency with explainable scoring features. All processing runs locally without requiring internet access for the default workflow.