import os

def vulnerable():
    user_input = input("Enter command: ")
    os.system(user_input)  # 🚨 CodeQL should flag this as a Command Injection vulnerability

vulnerable()
