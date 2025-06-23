import streamlit as st
import datetime
import json
import nest_asyncio
from universal_ui5_tester_playwright import run_ui_test_with_injector

nest_asyncio.apply()

st.set_page_config(page_title="Universal UI Tester", layout="wide")
st.title("🌐 Universal UI Tester")
st.caption("Author & Designer: Muraleedharan K.S")

st.sidebar.header("Test Configurations")
test_url = st.sidebar.text_input("🔗 Application URL", placeholder="https://your-app.com")

test_mode = st.sidebar.radio(
    "🧪 Show Results As (Default: Issues + Suggestions)",
    options=["Only Issues", "Issues + Suggestions"],
    index=1
)

run_test = st.sidebar.button("🚀 Run Test")

if run_test and test_url:
    st.subheader("🧾 Test Results")

    try:
        results = run_ui_test_with_injector(test_url)
    except Exception as e:
        st.error(f"Test run failed: {e}")
        st.stop()

    for result in results:
        if test_mode == "Only Issues" and result["status"] == "PASS":
            continue

        col1, col2, col3 = st.columns([3, 2, 5])
        col1.markdown(f"**🔖 Field:** `{result['field']}`")
        col2.markdown(f"**📤 Value:** `{result['value']}`")
        col3.markdown(f"**Status:** :{'green' if result['status']=='PASS' else 'orange' if result['status']=='WARN' else 'red'}[{result['status']}]")

        if test_mode == "Issues + Suggestions" and result["status"] != "PASS":
            if result.get("issue"):
                st.markdown(f"🔍 *Issue:* {result['issue']}")
            if result.get("suggestion"):
                st.markdown(f"💡 *Suggestion:* {result['suggestion']}")
            st.markdown("---")

    export_json = st.button("⬇️ Export JSON")
    if export_json:
        file_name = f"ui_test_result_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(file_name, "w") as f:
            json.dump(results, f, indent=2)
        st.success(f"Exported results to `{file_name}`")

else:
    st.info("Enter the application URL and click **Run Test** to begin.")