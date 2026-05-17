# CodeAlpha - Secure Coding Review

## Project Title
Secure Coding Review of a Python Flask Login Application

---

## Description
This project was developed as part of the **CodeAlpha Cyber Security Internship** under **Task 3: Secure Coding Review**.

The project demonstrates how to:

- Review insecure application code
- Identify security vulnerabilities
- Document findings in a professional report
- Create a remediated secure version of the application

The project contains:

- A deliberately vulnerable Flask application
- A remediated secure Flask application
- A detailed secure coding review report

---

## Project Structure

```text
CodeAlpha_SecureCodingReview/
│
├── vulnerable_app/
│   └── app.py
│
├── fixed_app/
│   └── app.py
│
├── review_report/
│   └── secure_coding_review_report.md
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Vulnerabilities Reviewed

The vulnerable version contains the following issues:

- SQL Injection
- Hardcoded Secret Key
- Plaintext Password Storage
- Debug Mode Enabled
- Weak Input Validation
- Insecure Password Field

The fixed version addresses these vulnerabilities using secure coding practices.

---

## Technologies Used

- Python 3
- Flask
- SQLite3
- Werkzeug Security
- Bandit

---

## Setup Instructions

### Kali Linux Setup

#### 1. Update Package List

```bash
sudo apt update
```

#### 2. Create Project Folder

```bash
mkdir CodeAlpha_SecureCodingReview
cd CodeAlpha_SecureCodingReview
```

#### 3. Create a Virtual Environment

```bash
python3 -m venv venv
```

#### 4. Activate Virtual Environment

```bash
source venv/bin/activate
```

#### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Windows Setup

#### 1. Install Python

Download and install Python 3 from:

https://www.python.org/downloads/

While installing, check:

- **Add Python to PATH**

#### 2. Open Command Prompt and Create Project Folder

```bash
mkdir CodeAlpha_SecureCodingReview
cd CodeAlpha_SecureCodingReview
```

#### 3. Create Virtual Environment

```bash
python -m venv venv
```

#### 4. Activate Virtual Environment

```bash
venv\Scripts\activate
```

#### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Applications

### Run the Vulnerable Application

#### Kali Linux

```bash
cd vulnerable_app
python3 app.py
```

#### Windows

```bash
cd vulnerable_app
python app.py
```

#### Open in Browser

```bash
http://127.0.0.1:5000
```

---

### Run the Fixed Application

#### Kali Linux

```bash
cd fixed_app
python3 app.py
```

#### Windows

```bash
cd fixed_app
python app.py
```

#### Open in Browser

```bash
http://127.0.0.1:5000
```

---

## Default Test Credentials

### Vulnerable App

- **Username:** admin
- **Password:** admin123

### Fixed App

- **Username:** admin
- **Password:** admin123

---

## SQL Injection Demonstration for Vulnerable App

You can demonstrate SQL Injection in the vulnerable app using payloads like:

```text
Username: ' OR '1'='1
Password: ' OR '1'='1
```

or

```text
Username: admin' --
Password: anything
```

> This should be used only for educational purposes in your own local testing environment.

---

## Static Analysis with Bandit

Run Bandit scan from the project root:

### Kali Linux

```bash
bandit -r vulnerable_app/
```

### Windows

```bash
bandit -r vulnerable_app/
```

### Save the Report

#### Kali Linux

```bash
bandit -r vulnerable_app/ -f txt -o bandit_report.txt
```

#### Windows

```bash
bandit -r vulnerable_app/ -f txt -o bandit_report.txt
```

---

## Key Security Improvements in Fixed Version

- Replaced dynamic SQL queries with parameterized queries
- Used password hashing instead of plaintext password storage
- Removed weak hardcoded secret key
- Disabled debug mode
- Added basic input validation
- Changed password field to secure password type
- Prevented duplicate admin creation

---

## Author

**Anish Kumar Patel**  
The British College Kathmandu  
Cyber Security and Digital Forensics
