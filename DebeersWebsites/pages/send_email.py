import smtplib
from email.message import EmailMessage
import sys
import os
from datetime import datetime

# Get report path from BAT file
report_path = sys.argv[1]

# Extract only file name (for attachment name)
report_filename = os.path.basename(report_path)

# Timestamp for subject
timestamp = datetime.now().strftime("%d-%m-%Y %H:%M")

msg = EmailMessage()
msg["Subject"] = f"Debeers Test Execution Report - {timestamp}"
msg["From"] = "debeerslive@gmail.com"
msg["To"] = "debeerslive@gmail.com"

msg.set_content("Please find attached report.")

with open(report_path, "rb") as f:
    msg.add_attachment(
        f.read(),
        maintype="text",
        subtype="html",
        filename=report_filename
    )

with smtplib.SMTP("smtp.gmail.com", 587) as s:
    s.starttls()
    s.login("debeerslive@gmail.com", "Ibm@@123")
    s.send_message(msg)

print(f"Email sent with report: {report_filename}...")