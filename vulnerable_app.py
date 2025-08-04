import os

# CWE-78: Command Injection
def run_command():
    user_input = input("Enter your command: ")
    os.system(user_input)  # 🚨 Dangerous use of raw input

# CWE-259: Hardcoded Password
def login():
    password = "1234"  # ❌ Hardcoded credentials
    entered = input("Enter password: ")
    if entered == password:
        print("Access granted")

run_command()
login()
