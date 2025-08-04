# CWE-78: Command Injection
import os
def run_command():
    user_input = input("Enter shell command: ")
    os.system(user_input)  # 🚨 Raw shell injection

run_command()


# CWE-259: Hardcoded Credentials
def insecure_login():
    password = "supersecret"  # 🚨 Hardcoded password
    user_input = input("Password: ")
    if user_input == password:
        print("Logged in")

insecure_login()


# CWE-94: Eval Injection
def code_exec():
    code = input("Run Python code: ")
    eval(code)  # 🚨 Arbitrary code execution

code_exec()

