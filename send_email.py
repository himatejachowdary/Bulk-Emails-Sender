import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Gmail login
sender_email = ""
app_password = ""

# Recipients
receiver_emails = [""]

# Repeat 5 times
for i in range(2):
    for receiver_email in receiver_emails:
        subject = f"Test Email {i+1}"
        body = f"This is test email number {i+1} to {receiver_email}"

        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender_email, app_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            server.quit()
            print(f"✅ Email {i+1} sent to {receiver_email}")
        except Exception as e:
            print(f"❌ Failed to send email {i+1} to {receiver_email}: {str(e)}")
