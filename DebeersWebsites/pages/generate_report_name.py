from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv(override=True)

COUNTRY = os.getenv("LOCALE").upper()
ENV = os.getenv("ENVIRONMENT").upper()
TESTING = os.getenv("TESTING_TYPE").upper()
MODULE = os.getenv("MODULE").upper()



timestamp = datetime.now().strftime("%d%m%Y-%H%M")

report_name = f"reports/{timestamp}_{ENV}_{COUNTRY}_{TESTING}_{MODULE}_REPORT.html"

print(report_name)