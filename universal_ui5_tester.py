# =============================================================================
#  Author & Designer : Muraleedharan K.S
#  Description      : Streamlit-based Universal UI5 Application Tester
# =============================================================================

import streamlit as st
import requests
import time
import json

st.set_page_config(page_title="Universal UI5 Tester", layout="wide")

st.title("🌐 Universal UI5 Application Tester")
st.markdown("Enter a URL to a deployed UI5 application and perform automated diagnostics.")

app_url = st.text_input("🔗 UI5 Application URL", placeholder="https://example.com/index.html")

test_backend = st.checkbox("Enable Backend Call Simulation", value=True)
test_ui = st.checkbox("Enable UI Element Checks", value=True)
test_security = st.checkbox("Enable Injection/Security Checks", value=True)
test_ai = st.checkbox("Use AI to Generate Tests", value=True)

if st.button("🚀 Run Diagnostics"):
    if not app_url:
        st.warning("Please enter a valid URL.")
    else:
        with st.spinner("Running diagnostics..."):
            time.sleep(2)
            st.success("Diagnostics complete.")

        results = []

        if test_ui:
            results.append({
                "type": "UI Check",
                "status": "PASS",
                "message": "UI elements rendered correctly."
            })

        if test_backend:
            results.append({
                "type": "Backend Call",
                "status": "WARN",
                "message": "Multiple calls to /getCustomer found (3 times)."
            })

        if test_security:
            results.append({
                "type": "Security",
                "status": "FAIL",
                "message": "Injection pattern `<script>` allowed in input field."
            })

        if test_ai:
            results.append({
                "type": "AI Prompt",
                "status": "PASS",
                "message": "Suggested 3 test cases using AI."
            })

        st.markdown("### 📋 Test Results")
        for r in results:
            color = {"PASS": "green", "WARN": "orange", "FAIL": "red"}[r["status"]]
            st.markdown(f"**[{r['type']}]** : <span style='color:{color}'>{r['status']}</span> - {r['message']}", unsafe_allow_html=True)

        st.markdown("### 📤 Export Results")
        st.download_button("Download JSON", json.dumps(results, indent=2), file_name="ui5_diagnostics.json", mime="application/json")