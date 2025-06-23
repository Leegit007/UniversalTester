import asyncio
from playwright.async_api import async_playwright

def run_ui_test_with_injector(url: str, js_injector_path: str = "static/js/injector.js"):
    return asyncio.run(_run_ui_test(url, js_injector_path))

async def _run_ui_test(url: str, js_injector_path: str):
    results = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--no-sandbox"])
        page = await browser.new_page()
        await page.goto(url)

        with open(js_injector_path, "r") as js_file:
            injector_script = js_file.read()
        await page.add_script_tag(content=injector_script)

        fields = await page.evaluate("() => window.__uiTester.getFields && window.__uiTester.getFields()")
        if not fields:
            return [{
                "field": "UI Scan",
                "value": "",
                "status": "FAIL",
                "issue": "No fields detected on the page",
                "suggestion": "Check if your injector.js defines `window.__uiTester.getFields` properly"
            }]

        for field in fields:
            selector = field.get("selector")
            field_type = field.get("type", "text")
            mock_value = generate_mock_value(field_type)
            result = {
                "field": selector,
                "value": mock_value,
                "status": "PASS",
                "issue": "",
                "suggestion": ""
            }
            try:
                await page.fill(selector, mock_value)
            except Exception as e:
                result["status"] = "FAIL"
                result["issue"] = f"Cannot fill field: {e}"
                result["suggestion"] = "Check field selector or visibility/accessibility"
            results.append(result)

        try:
            await page.click("button[type='submit'], input[type='submit']")
        except:
            pass

        try:
            messages = await page.evaluate("() => window.__uiTester.getMessages && window.__uiTester.getMessages()")
            if messages:
                for msg in messages:
                    results.append({
                        "field": "System Message",
                        "value": msg.get("text", ""),
                        "status": msg.get("type", "INFO").upper(),
                        "issue": msg.get("issue", ""),
                        "suggestion": msg.get("suggestion", "")
                    })
        except:
            pass

        await browser.close()
        return results

def generate_mock_value(field_type):
    field_type = field_type.lower()
    if "email" in field_type:
        return "test@example.com"
    elif "number" in field_type:
        return "42"
    elif "date" in field_type:
        return "2024-12-31"
    elif "password" in field_type:
        return "Secret123"
    elif "phone" in field_type:
        return "+911234567890"
    else:
        return "SampleValue"