import os

def dangerous_input():
    cmd = input("Enter command: ")
    os.system(cmd)  # This should trigger CWE‑78 Command Injection

dangerous_input()
