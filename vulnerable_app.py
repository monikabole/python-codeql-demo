import os

def run_command(user_input):
    os.system("echo " + user_input)

run_command(input("Enter something: "))
