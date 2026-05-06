import smtplib
import sys
from email.message import EmailMessage
import os
from dotenv import load_dotenv
from datetime import datetime
import logging

load_dotenv(override=True)
logger = logging.getLogger(__name__)

COUNTRY = os.getenv("LOCALE").upper()
ENV = os.getenv("ENVIRONMENT").upper()
TESTING = os.getenv("TESTING_TYPE").upper()
URL = os.getenv("BASE_URL")

# 1. Validation: Ensure a path was actually passed
if len(sys.argv) < 2:
    logger.error("***** ERROR: NO REPORT PATH PROVIDED..*****")
    sys.exit(1)

report_path = sys.argv[1]  # first argument in the .bat file. report path in this case.
test_files = sys.argv[2:]  # remaining arguments. test files in this case.
file_list = "\n".join(f"- {file}" for file in test_files) if test_files else "No test files provided"
report_filename = os.path.basename(report_path)
timestamp = datetime.now().strftime("%d-%m-%Y %H:%M")

# 2. Setup Email
msg = EmailMessage()
msg["Subject"] = f"[{ENV}-{COUNTRY}] Test Execution Report"
msg["From"] = "debeerslive@gmail.com"
msg["To"] = "prashant_vadher@epam.com"
#Plain text content
text_body  = f"""Hello,

ENVIRONMENT: {ENV}
COUNTRY: {COUNTRY}
TESTING TYPE: {TESTING}
EXECUTION TIME: {timestamp}
REPORT FILENAME: {report_filename}
EXECUTED TEST FILES:
{file_list}


Please find the attached test execution report.

Regards,
Prashant Vadher
"""
msg.set_content(text_body )

#Html text content

html_body = f"""
<html>
<body style="font-family: Arial, sans-serif; font-size: 14px; line-height: 1.6;">

<p style="margin-bottom: 16px;"><b>Hello,</b></p>

<p style="margin-bottom: 16px;">
<b>ENVIRONMENT:</b> {ENV}<br>
<b>COUNTRY:</b> {COUNTRY}<br>
<b>EXECUTION TIME:</b> {timestamp}<br>
<b>REPORT FILENAME:</b> {report_filename}
</p>

<p style="margin-bottom: 8px;"><b>EXECUTED TEST FILES:</b></p>

<ul style="margin-top: 0; margin-bottom: 16px; padding-left: 20px;">
{''.join(f"<li style='margin-bottom: 6px;'>{file}</li>" for file in test_files) if test_files else "<li>No test files provided</li>"}
</ul>

<p style="margin-bottom: 16px;">
Please find the attached test execution report.
</p>
<br>
<br>
<p>
Regards,<br>
Prashant Vadher
</p>

</body>
</html>
"""

msg.add_alternative(html_body, subtype="html")

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
    logger.error(f"***** THE FILE AT {report_path} WAS NOT FOUND..*****")
    sys.exit(1)

# 4. Send Email
try:
    with smtplib.SMTP("smtp.gmail.com", 587) as s:
        s.starttls()
        # Use an App Password here, NOT your regular login password
        s.login("debeerslive@gmail.com", "fuxm gcus bdgi kgtg")
        s.send_message(msg)
    logger.info(f"EMAIL SENT SUCCESSFULLY WITH REPORT: {report_filename}")
except Exception as e:
    logger.error(f"*****FAILED TO SEND EMAIL: {e} *****")