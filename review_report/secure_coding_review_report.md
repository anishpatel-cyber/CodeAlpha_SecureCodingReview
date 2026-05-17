# Secure Coding Review Report

## Project Title
Secure Coding Review of a Python Flask Login Application

---

## Objective
The purpose of this project is to review a Flask web application, find security problems, and fix them using secure coding practices.

---

## Application Reviewed

- Python Flask login application
- SQLite database
- User login form

---

## Tools Used

- Python 3
- Flask
- SQLite3
- Bandit
- Manual Code Review

---

## Vulnerabilities Found

### 1. SQL Injection

#### Problem
The application builds SQL queries directly using user input.

#### Vulnerable Code

```python
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
```

#### Risk Level
**High**

#### Impact
An attacker can bypass authentication or manipulate the database query.

#### Remediation
Use parameterized queries:

```python
cursor.execute(
    "SELECT username, password FROM users WHERE username = ?",
    (username,)
)
```

---

### 2. Hardcoded Secret Key

#### Description
The Flask secret key is hardcoded and weak.

#### Vulnerable Code

```python
app.secret_key = "12345"
```

#### Risk Level
**Medium**

#### Impact
Attackers may forge session data if the secret key is predictable.

#### Remediation
Use environment variables or securely generated keys.

---

### 3. Plaintext Password Storage

#### Description
Passwords are stored directly in the database without hashing.

#### Risk Level
**High**

#### Impact
If the database is compromised, all user credentials are exposed.

#### Remediation
Use password hashing with:

```python
from werkzeug.security import generate_password_hash
```

Example:

```python
hashed_password = generate_password_hash(password)
```

---

### 4. Debug Mode Enabled

#### Description
The application runs with debug mode enabled.

#### Vulnerable Code

```python
app.run(debug=True)
```

#### Risk Level
**Medium**

#### Impact
Debug mode may expose stack traces and internal application details.

#### Remediation
Disable debug mode in production:

```python
app.run(debug=False)
```

---

### 5. Weak Input Validation

#### Description
The application does not validate input length or format.

#### Risk Level
**Medium**

#### Impact
Improper input handling may contribute to attacks or application instability.

#### Remediation
Validate user inputs before processing.

---

## Static Analysis Findings

Bandit was used to perform static analysis of the codebase. The tool highlighted insecure patterns such as hardcoded secrets and unsafe implementation practices.

---

## Secure Version Improvements

The remediated application includes:

- Parameterized SQL queries
- Password hashing
- Stronger secret key management
- Disabled debug mode
- Improved form handling and validation

---

## Conclusion

The review identified several common but critical security issues in the application. After remediation, the application follows more secure coding practices and provides better protection against common web application attacks.

---

## Step 7: What to Demonstrate in Your Internship Submission

For GitHub and video explanation, show:

- Vulnerable code
- SQL injection demo
- Bandit scan
- Secure fixed code
- Explanation of each vulnerability
- How each fix works

---

## Step 8: Commands for Kali Linux

From project root:

```bash
python3 -m venv venv
source venv/bin/activate
pip install flask bandit werkzeug
python3 vulnerable_app/app.py
```

### Run Bandit Scan

```bash
bandit -r vulnerable_app/
```

### Run Secure Version

```bash
python3 fixed_app/app.py
```
