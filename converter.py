import time
from utils import delay


def cgpa_to_cwa():
    value = float(input("\nEnter CGPA: "))
    to_cwa = (value * 100) / 4
    time.sleep(0.6)
    print("\nProcessing", end="")
    delay()
    print(f"A CGPA of {value} corresponds to {to_cwa:.2f} CWA")


def cwa_to_gpa():
    value = float(input("\nEnter CWA: "))
    to_gpa = (value / 100) * 4.0
    time.sleep(0.6)
    print("\nProcessing", end="")
    delay()
    print(f"A CWA of {value} corresponds to {to_gpa:.2f} GPA.")