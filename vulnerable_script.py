import os

def search_files():
    filename = input("Enter the filename to search: ")
    # 🚨 Vulnerability: Command injection
    os.system(f"find / -name {filename}")

if __name__ == "__main__":
    search_files()
