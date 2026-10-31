🛡️ AryaPen – Web Application Penetration Testing Toolkit 🛡️

AryaPen is a Python-based educational cybersecurity project designed to perform basic security assessments of web applications and authorized systems.

The project aims to provide a simple and user-friendly platform for learning web application security testing and penetration testing concepts.

🚀 Project Overview

AryaPen is a beginner-friendly penetration testing toolkit that combines Python and Flask to provide a web-based security assessment dashboard.

It is being developed with a modular architecture so that additional security testing features can be integrated in future versions.

✨ Features

- TCP Port Scanner: Identifies open and closed TCP ports on authorized local targets.
- Web Dashboard: Provides a simple interface for security assessment.
- Target Validation: Validates HTTP and HTTPS URL formats.
- Service Identification: Displays common service names associated with TCP ports.
- HTTP Security Header Analyzer: Planned.
- SSL Certificate Checker: Planned.
- Security Assessment Reports: Planned.

🛠️ Technologies Used

Technology| Purpose
Python| Core programming
Flask| Backend framework
HTML5| Webpage structure
CSS3| Dashboard styling
JavaScript| Frontend interaction
Requests| HTTP operations
Socket| TCP port scanning
Git & GitHub| Version control

📁 Project Structure

AryaPen/
│
├── app.py
├── requirements.txt
│
├── scanner/
│   └── port_scanner.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
├── reports/
├── database/
├── .gitignore
└── README.md

⚙️ Installation and Setup

1. Clone the repository

git clone https://github.com/asmitston/AryaPen.git

2. Navigate to project directory

cd AryaPen

3. Create virtual environment

python -m venv venv

4. Activate virtual environment

Windows:

venv\Scripts\activate

5. Install dependencies

pip install -r requirements.txt

6. Run the application

python app.py

7. Open in browser

http://127.0.0.1:5000

🧪 Current Development Status

Phase| Module| Status
Phase 1| Project Setup and Flask Dashboard| Completed
Phase 2| TCP Port Scanner| In Development
Phase 3| HTTP Security Header Analyzer| Planned
Phase 4| SSL Certificate Checker| Planned
Phase 5| Vulnerability Assessment| Planned
Phase 6| Security Report Generator| Planned

🎯 Project Objectives

- Understand web application security fundamentals.
- Learn Python-based security testing.
- Identify basic network and web security configurations.
- Develop practical cybersecurity skills.
- Build a modular penetration testing toolkit.

🔮 Future Enhancements

- Advanced HTTP security analysis.
- SSL/TLS configuration assessment.
- Common web security misconfiguration detection.
- Improved security dashboard.
- PDF and HTML report generation.
- Scan history and result management.

⚠️ Disclaimer

AryaPen is developed strictly for educational purposes and authorized security testing.

Users must only test applications, networks, and systems that they own or have explicit permission to assess.

The developer is not responsible for misuse of this software or unauthorized testing activities.

👨‍💻 Author

Your Name

GitHub: https://github.com/asmitston

⭐ Support

If you find this educational project useful, consider giving the repository a star on GitHub.

---

AryaPen – Learn. Analyze. Secure.
