# Importing necessary libraries
import os
import argparse
import smtplib
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from time import sleep

# Create argument parser for command line interface
parser = argparse.ArgumentParser(description="Send multiple test emails using Gmail.")

# Add argument for the number of emails to send
parser.add_argument(
    "-n", "--number", type=int, default=1, help="Number of emails to send (default: 1)"
)

# Add argument for receiver emails
parser.add_argument(
    "-r", "--receivers", nargs="+", required=True, help="List of receiver email addresses"
)

# Parse command line arguments
args = parser.parse_args()

# Validate receiver emails - ensure at least one email is provided
receiver_emails = args.receivers
if not receiver_emails:
    print("Error: At least one receiver email must be provided.")
    exit(1)

# Check if the number of emails is valid - must be at least 1
if args.number < 1:
    print("Error: The number of emails must be at least 1.")
    exit(1)

# Set the count of emails to send
count = args.number

# Load environment variables and get Gmail credentials
load_dotenv()
sender_email = os.getenv("GMAIL_USER")
app_password = os.getenv("GMAIL_APP_PASSWORD")

# Main email sending loop - iterate through the specified number of emails
for i in range(count):
    # Send email to each recipient in the list
    for receiver_email in receiver_emails:
        # Create email subject and body with incremental numbering
        subject = f"Test Email {i+1}"
        body = f"This is test email number {i+1} to {receiver_email}"

        # Create MIME message object for email formatting
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # Attempt to send the email with error handling
        try:
            # Connect to Gmail SMTP server
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()  # Enable encryption
            server.login(sender_email, app_password)  # Authenticate with Gmail
            server.sendmail(sender_email, receiver_email, msg.as_string())  # Send email
            server.quit()  # Close connection
            print(f"✅ Email {i+1} sent to {receiver_email}")
        except Exception as e:
            # Handle any errors during email sending
            print(f"❌ Failed to send email {i+1} to {receiver_email}: {str(e)}")

    # Sleep for 0.5 seconds between email batches to avoid rate limiting
    sleep(0.5)
