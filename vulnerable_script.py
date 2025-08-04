import os

def run_command():
    user_input = input("Enter a command: ")
    os.system(user_input)  # 💀 Command injection vulnerability

run_command()
