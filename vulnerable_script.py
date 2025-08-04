import os

# Hardcoded password
username = "admin"
password = "123456"

# Unsafe command execution
os.system("rm -rf /")  # Dangerous!

# Insecure use of eval()
user_input = input("Enter something: ")
eval(user_input)
