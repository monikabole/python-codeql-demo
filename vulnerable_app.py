import os

def run_command():
    user_input = input("Enter your command: ")
    # CWE-78: Command Injection
    os.system(user_input)  # 🚨 Dangerous use of raw input

run_command()
