import time

import pytest
import os
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from utils.config_reader import get_config

import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__)).replace("\\test", "")

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(os.path.join(PROJECT_ROOT, "test.log")),
        logging.StreamHandler()
    ]
)


@pytest.fixture(scope="function")
def init_driver(request, credentials):
    logging.info("Launching new Chrome browser instance")
    options = Options()
    options.add_argument("--start-maximized")
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)

    # Navigate to base URL before every test
    base_url = credentials.get("base_url", "http://localhost:4777/login")
    driver.get(base_url)
    logging.info(f"Navigated to: {base_url}")

    request.cls.driver = driver
    yield
    logging.info("Quitting browser")
    driver.implicitly_wait(3)
    driver.quit()


@pytest.fixture(scope="session")
def credentials():
    # Navigate from test/conftest.py → ../utils/credentials.json
    # base_dir = os.path.dirname(os.path.dirname(__file__))  # i2v_qa/
    file_path = os.path.join(PROJECT_ROOT, "utils", "credentials.json")
    logging.info(f"Reading credentials from: {file_path}")
    return get_config(file_path)

# @pytest.fixture(scope="session")
# def credentials():
#     config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "utils", "credentials.json")
#     return get_config(config_path)


# =========================
# Screenshot on failure + HTML report embedding
# =========================
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call, pytest_html=None):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = getattr(item.instance, "driver", None)
        if driver:
            screenshots_dir = os.path.join(PROJECT_ROOT, "reports", "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)
            screenshot_file = os.path.join(screenshots_dir, f"{item.name}.png")
            driver.save_screenshot(screenshot_file)
            logging.error(f"Screenshot saved to {screenshot_file}")

            if "pytest_html" in item.config.pluginmanager.list_name_plugin():
                extra = getattr(report, "extra", [])
                html = (
                    f'<div><img src="{screenshot_file}" alt="screenshot" '
                    f'style="width:300px;height:auto;" '
                    f'onclick="window.open(this.src)"/></div>'
                )
                extra.append(pytest_html.extras.html(html))
                report.extra = extra


def pytest_html_report_title(report):
    report.title = "Automation Test UserManagement - i2v QA"


def pytest_configure(config):
    if hasattr(config, "_metadata"):
        config._metadata["Project Name"] = "i2v QA"
        config._metadata["Tester"] = "Lakshya"
        config._metadata["Browser"] = "Chrome (Selenium Manager)"
