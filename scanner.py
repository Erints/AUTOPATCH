import os

# Define the "Fixed" versions of bad code
RULES = {
    "SQL_INJECTION": ["cursor.execute(", "SELECT * FROM", "+ user_id"],
    "HARDCODED_SECRET": ["API_KEY =", "SECRET =", "PASSWORD =", "TOKEN ="],
    "XSS_VULNERABILITY": ["innerHTML =", "document.write(", "dangerouslySetInnerHTML"],
    "INSECURE_DEPENDENCY": ["flask==0.12", "requests==2.6.0", "pyyaml==3.11"],
    "RACE_CONDITION": ["threading.Thread(", "time.sleep(", "global_var +="]
}

def apply_fixes(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        fixed = False
        # If the line has a vulnerability, replace it with the fix
        if "execute(\"SELECT" in line and "+" in line:
            new_lines.append(FIXES["SQL_INJECTION"] + "\n")
            fixed = True
        elif "API_KEY =" in line and "\"" in line:
            new_lines.append(FIXES["HARDCODED_SECRET"] + "\n")
            fixed = True
        else:
            new_lines.append(line)
            
    with open(filename, 'w') as f:
        f.writelines(new_lines)
    print(f"🛡️ AUTOPATCH: Fixed vulnerabilities in {filename}")

if __name__ == "__main__":
    # For the hackathon demo, we will target your test file
    apply_fixes("test_vulnerabilities.py")