# =============================================================================
#  Author & Designer : Muraleedharan K.S
#  Description      : Streamlit-based Universal UI5 Application Tester
# =============================================================================

import streamlit as st
import json
import datetime

# App Config
st.set_page_config(page_title="Universal UI Tester", layout="wide")

# App Title
st.title("🌐 Universal UI Tester")
st.caption("Author & Designer: Muraleedharan K.S")

# Sidebar Controls
st.sidebar.header("Test Configurations")
test_url = st.sidebar.text_input("🔗 Application URL", placeholder="https://your-app.com")

test_mode = st.sidebar.radio(
    "🧪 Show Results As",
    ["Only Issues", "Issues + Suggestions"],
    index=1
)

run_test = st.sidebar.button("🚀 Run Test")

# Simulated Test Execution
def run_mock_test():
    # Simulated field-wise test results
    return [
        {
            "field": "#emailInput",
            "value": "test@demo.com",
            "status": "FAIL",
            "issue": "Unmasked personal data",
            "suggestion": "Use UI5 formatter or backend masking"
        },
        {
            "field": "#materialType",
            "value": "RAW",
            "status": "PASS"
        },
        {
            "field": "#discount",
            "value": "100%",
            "status": "WARN",
            "issue": "High discount value without approval logic",
            "suggestion": "Add validation or approval check"
        }
    ]

# Run Test
if run_test and test_url:
    st.subheader("🧾 Test Results")
    results = run_mock_test()

    for result in results:
        col1, col2, col3 = st.columns([3, 2, 5])
        col1.markdown(f"**🔖 Field:** `{result['field']}`")
        col2.markdown(f"**📤 Value:** `{result['value']}`")
        col3.markdown(f"**Status:** :{'green' if result['status']=='PASS' else 'orange' if result['status']=='WARN' else 'red'}[{result['status']}]")

        if test_mode == "Issues + Suggestions" and result['status'] != "PASS":
            st.markdown(f"🔍 *Issue:* {result.get('issue', '-')}")
            st.markdown(f"💡 *Suggestion:* {result.get('suggestion', '-')}")
            st.markdown("---")

    # Export buttons
    export_json = st.button("⬇️ Export JSON")
    export_pdf = st.button("⬇️ Export PDF (coming soon)")

    if export_json:
        file_name = f"ui_test_result_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(file_name, "w") as f:
            json.dump(results, f, indent=2)
        st.success(f"Exported results to `{file_name}`")

else:
    st.info("Enter the application URL and click **Run Test** to begin.")
