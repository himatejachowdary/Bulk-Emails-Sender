# 📚 How I Built the Bulk Email Sender

This guide walks through the process of creating a Python-based bulk email sender using Gmail's SMTP server.

---

## 💡 Idea

I wanted to create a script that could send multiple emails automatically for testing, announcements, or bulk messages using a Gmail account.

---

## 🧰 Tools Used

- Python
- `smtplib` (built-in)
- `email.mime` for formatting
- `dotenv` to securely manage credentials

---

## 🛠️ Step-by-Step Build

### 1. Setup the Project
```bash
mkdir bulk-email-sender
cd bulk-email-sender

### 2. . Create Python File
File: send_email.py

Used smtplib, looped over recipient list and repeated email sends. Added exception handling and dynamic subject/body.
EMAIL=myemail@gmail.com
APP_PASSWORD=xxxxxx

### 3 . 4. GitHub Repo
Pushed to GitHub

Added .gitignore, README.md, LICENSE, and LEARN.md

📌 Key Learning
Sending authenticated emails using SMTP

Protecting credentials via environment variables

Writing reusable, safe, and automated Python scripts
