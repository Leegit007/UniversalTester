# 🌐 Universal UI5 Tester (Streamlit-Based) – Intelligent Version

**Author & Designer: Muraleedharan K.S**

---

## 🆕 New Features Added

### 1. 🔗 URL-Driven Testing
- Accepts full SAP UI5 application URL (with optional parameters)
- SSO assumed for authentication – test starts **post-login screen**
- Optional credential input available (hidden, fallback only)

### 2. 🚀 Full Auto Testing
- One-click auto diagnostic across:
  - ✅ UI layout validation
  - 📡 Backend service usage simulation
  - 🔐 Injection/security checks
  - 🤖 AI-driven test case suggestions
- Colored result status (PASS/WARN/FAIL)

### 3. 💬 Prompt-Based Manual Testing
- Accepts user prompt like:
  > "Test customer creation with name John Doe and region Europe"
- Automatically generates:
  - Field selectors (`#custName`, `#custRegion`)
  - Sample values
  - Submit/validation actions
- Injects this into app via JavaScript from Streamlit
- Simulates input + submission for guided testing

### 4. 🧠 Self-Populating Form Fields
- AI generates test data for:
  - Customer/supplier names
  - Dates, quantities, IDs
  - Tax numbers, phone, email, addresses
- Auto-injected into UI5 app (via iframe JS layer)

### 5. 🔍 Smart Recording/Tracing Logic
- Recording starts **only after bypassing login** (detected via screen DOM)
- Captures:
  - Filled field names + values
  - Time of interaction
  - Triggered actions (e.g., submit clicks)
  - Backend calls simulated (if monitoring allowed)

### 6. 📤 Output & Export
- Test result JSON (detailed trace)
- (Coming soon) PDF generation
- Results tagged with session ID and timestamp

---

## 🔐 Security & Safeguards

- Only user-provided domains tested (not hardcoded)
- Credentials not stored
- Local recording, no backend logging by default
- CORS-safe iframe injection (within permitted domains)

---

## 📦 Usage

### Streamlit Cloud

1. Upload repo to GitHub
2. Deploy via https://streamlit.io/cloud

### Local

```bash
pip install streamlit requests
streamlit run universal_ui5_tester.py
```

---

## 📊 Data Generation (LLM Examples)

| Field Type | Sample Generated Value |
|------------|------------------------|
| Customer Name | "Zenovia Ltd" |
| GST Number | "27ABCDE1234F2Z6" |
| Email | "test@zenovia.com" |
| Region | "Europe" |
| Material Code | "ZMAT-2024-01" |
| Contact | "+91-9876543210" |

All values are generated per prompt intent.

---

## 📁 Project Structure

```
/universal_ui5_tester/
 ├── universal_ui5_tester.py
 ├── README.md
 ├── requirements.txt
 └── (Future) static/js/injector.js
```

------

## 🌍 Not Just for SAP UI5 — Works with Any Web App

This tool is designed to test **any browser-accessible application**, not just SAP UI5 apps.

### ✅ Supported Targets:
- SAP UI5 / Fiori Apps
- SAP BTP Deployed UIs (CAP/RAP)
- React, Angular, Vue apps
- Web Portals and Admin Consoles
- Chatbots (SAP CAI, OpenAI widgets, Dialogflow, etc.)
- Embedded browser-based tools

### ⚙️ How It Works:
- Uses **standard URL loading** in iframe
- Performs **JavaScript injection** to simulate form inputs and actions
- Leverages **prompt engineering** and LLMs to drive dynamic testing

> ⚠️ Note: For highly restricted apps (CSP/CORS-blocked), additional browser extension or proxy support may be needed for deeper control.

This makes the tester a **Universal Streamlit-based QA Assistant** for front-end quality assurance.---

## ⚙️ Configurable Output: Issues Only vs. Issues + Solutions

The tester now supports a configurable setting in the UI:

- **🔘 Show Only Issues**: Display only the list of failed checks (status + element).
- **🔘 Show Issues + Solutions** *(default)*: Display failed checks along with explanations and recommended fixes.

This setting can be toggled via a checkbox or radio button in the Streamlit UI.

### Example:

| Setting | Displayed Output |
|--------|------------------|
| Show Only Issues | ❌ Email field exposes data |
| Show Issues + Solutions | ❌ Email field exposes data  
💡 Use data masking or restrict via backend role check |

This helps developers focus on **debugging quickly**, while testers and auditors can view **remediation guidance** when needed.---

## 🎨 Auto Theming & 🧾 PDF Export Support

### 🌗 Auto Theming
The app detects browser/system theme preference and adjusts UI colors accordingly:
- Light mode for bright environments
- Dark mode for night-friendly contrast
This is handled using Streamlit’s theming settings or dynamic CSS injection.

### 🧾 PDF Export
Each test session can now be exported to a formatted PDF with:
- Timestamp
- Application URL
- Session ID
- List of issues (and solutions, if enabled)
- Summary statistics (Pass/Fail counts)

Export Options:
- 📄 **PDF** to user's Downloads folder (or custom path)
- 📦 **JSON** for machine-readable integration

> These features improve usability in enterprise QA and compliance reporting environments.