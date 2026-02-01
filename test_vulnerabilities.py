# --- AUTOPATCH TEST FILE ---
# 1. Hardcoded Secret (Requirement: Detect hardcoded secrets)
API_KEY = "sk-1234567890abcdef"
admin_password = "password123"

# 2. SQL Injection (Requirement: Detect SQL injection)
def get_user_data(user_input):
    query = "SELECT * FROM users WHERE id = " + user_input
    print(f"Executing: {query}")

# 3. XSS Risk (Requirement: Detect XSS)
# Using innerHTML with user variables in JS-style strings
unsafe_html = "document.getElementById('display').innerHTML = " + user_input

# 4. Insecure Dependency (Requirement: Detect insecure dependencies)
import os
os.system("rm -rf /") # Highly dangerous shell command

# 5. Race Condition Risk (Requirement: Detect race conditions)
import threading
global_counter = 0 # Using global state without locks
