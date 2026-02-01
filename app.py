import streamlit as st
import scanner # This imports your existing scanner logic

st.set_page_config(page_title="AUTOPATCH Dashboard", page_icon="🛡️")

st.title("🛡️ AUTOPATCH Security Dashboard")
st.markdown("### AI-Powered Vulnerability Detection & Remediation")

uploaded_file = st.file_uploader("Upload a Python or JS file to scan", type=['py', 'js'])

if uploaded_file is not None:
    # Read the file
    content = uploaded_file.read().decode("utf-8")
    st.code(content, language='python')
    
    if st.button("Run Security Audit"):
        st.write("---")
        st.subheader("Scan Results")
        
        # Check against your RULES
        found_bugs = False
        lines = content.split('\n')
        
        for i, line in enumerate(lines):
            for bug_type, patterns in scanner.RULES.items():
                if any(p in line for p in patterns):
                    found_bugs = True
                    st.error(f"🚨 **{bug_type}** found on line {i+1}")
                    
                    # Provide the Auto-Patch
                    if bug_type == "SQL_INJECTION":
                        st.info("💡 **AUTO-PATCH:** Use parameterized queries instead of string concatenation (+).")
                    elif bug_type == "HARDCODED_SECRET":
                        st.info("💡 **AUTO-PATCH:** Move this secret to an environment variable (.env).")
                    elif bug_type == "RACE_CONDITION":
                        st.info("💡 **AUTO-PATCH:** Implement threading.Lock() to protect shared state.")

        if not found_bugs:
            st.success("✅ No vulnerabilities detected! Your code is safe.")
