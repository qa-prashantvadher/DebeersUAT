import smtplib
import sys
import os
from email.message import EmailMessage
from datetime import datetime

# 1. Validation: Ensure a path was actually passed
if len(sys.argv) < 2:
    print("Error: No report path provided.")
    sys.exit(1)

report_path = sys.argv[1]
report_filename = os.path.basename(report_path)
timestamp = datetime.now().strftime("%d-%m-%Y %H:%M")

# 2. Setup Email
msg = EmailMessage()
msg["Subject"] = f"Debeers Test Execution Report - {timestamp}"
msg["From"] = "debeerslive@gmail.com"
msg["To"] = "prashant_vadher@epam.com"
msg.set_content("Please find the attached execution report.")

# 3. Read and Attach File
try:
    with open(report_path, "rb") as f:
        file_data = f.read()
        # Using 'application/octet-stream' is safer for general attachments
        msg.add_attachment(
            file_data,
            maintype="application",
            subtype="octet-stream",
            filename=report_filename
        )
except FileNotFoundError:
    print(f"*****: THE FILE AT {report_path} WAS NOT FOUND.*****")
    sys.exit(1)

# 4. Send Email
try:
    with smtplib.SMTP("smtp.gmail.com", 587) as s:
        s.starttls()
        # Use an App Password here, NOT your regular login password
        s.login("debeerslive@gmail.com", "fuxm gcus bdgi kgtg")
        s.send_message(msg)
    print(f"EMAIL SENT SUCCESSFULLY WITH REPORT: {report_filename}")
except Exception as e:
    print(f"*****FAILED TO SEND EMAIL: {e} *****")