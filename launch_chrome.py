import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

# Create a reports directory if it doesn't exist
report_dir = "reports"
os.makedirs(report_dir, exist_ok=True)

# Set Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Initialize Chrome WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open a webpage
url = "https://www.google.com"
driver.get(url)

# Capture screenshot
screenshot_path = os.path.join(report_dir, "screenshot.png")
driver.save_screenshot(screenshot_path)

# Get page title
page_title = driver.title

# Close the browser
driver.quit()

# Generate HTML report
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
html_report = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chrome Launch Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; padding: 20px; }}
        h1 {{ color: #2c3e50; }}
        .screenshot {{ margin-top: 20px; }}
    </style>
</head>
<body>
    <h1>Chrome Launch Test Report</h1>
    <p><strong>Test Run:</strong> {timestamp}</p>
    <p><strong>Page Title:</strong> {page_title}</p>
    <p><strong>URL:</strong> {url}</p>
    <div class="screenshot">
        <h2>Screenshot</h2>
        <img src="screenshot.png" alt="Screenshot" width="600">
    </div>
</body>
</html>
"""

# Save HTML report
report_path = os.path.join(report_dir, "report.html")
with open(report_path, "w", encoding="utf-8") as file:
    file.write(html_report)

print(f"Report generated: {report_path}")
