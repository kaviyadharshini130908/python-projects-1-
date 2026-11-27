
from dotenv import load_dotenv
import os
load_dotenv()
app_name = os.getenv("APP_NAME")
student_name = os.getenv("STUDENT_NAME")
print("App Name:", app_name)
print("Student Name:", student_name)
