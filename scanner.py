import os

# The 5 Mandatory Requirements for your Hackathon
RULES = {
    "SQL_INJECTION": ["+", ".format(", "f\""],
    "HARDCODED_SECRET": ["password =", "api_key =", "token =", "secret ="],
    "INSECURE_DEP": ["import os", "import subprocess", "pickle.load("],
    "XSS_RISK": ["innerHTML", "document.write("],
    "RACE_CONDITION": ["threading.Thread(", "global ", "while True:"]
}

def run_audit():
    print("🛡️ AUTOPATCH: Running Security Scan...")
    for file in os.listdir('.'):
        # We check Python (.py) and JavaScript (.js) files
        if file.endswith(('.py', '.js')) and file != 'scanner.py':
            with open(file, 'r') as f:
                lines = f.readlines()
                for i, line in enumerate(lines):
                    for bug_type, patterns in RULES.items():
                        if any(p in line for p in patterns):
                            print(f"🚨 {bug_type} found in {file} on line {i+1}")
                            
                            # --- AUTO-PATCH LOGIC ---
                            if bug_type == "SQL_INJECTION":
                                print("  💡 AUTO-PATCH: Use parameterized queries instead of '+'")
                            elif bug_type == "HARDCODED_SECRET":
                                print("  💡 AUTO-PATCH: Use os.getenv() for keys!")
                            elif bug_type == "INSECURE_DEP":
                                print("  💡 AUTO-PATCH: Avoid shell=True in subprocess.")
                            elif bug_type == "XSS_RISK":
                                print("  💡 AUTO-PATCH: Use textContent instead of innerHTML.")
                            elif bug_type == "RACE_CONDITION":
                                print("  💡 AUTO-PATCH: Use threading.Lock() to prevent data corruption.")

def check_dependencies():
    if os.path.exists("requirements.txt"):
        print("\n🛡️ AUTOPATCH: Checking requirements.txt for old libraries...")
        with open("requirements.txt", 'r') as f:
            content = f.read()
            if "flask==0.1" in content:
                print("🚨 [INSECURE_DEP] Flask version 0.1 is dangerous. Upgrade to 3.0+!")

if __name__ == "__main__":
    run_audit()
    check_dependencies()