import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "http://localhost:8000/site/login.html"
VALID_USER = "demo@site.com"
VALID_PASS = "Demo@123"
INVALID_PASS = "sai123"

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

def shot(driver, name):
    driver.save_screenshot(f"./screenshots/{name}.png")

def test_login_success(driver):
    driver.get(BASE_URL)
    driver.find_element(By.ID, "username").send_keys(VALID_USER)
    driver.find_element(By.ID, "password").send_keys(VALID_PASS)
    driver.find_element(By.ID, "submit").click()
    time.sleep(1)
    shot(driver, "login_success")
    assert "dashboard" in driver.current_url.lower()

def test_login_wrong_password(driver):
    driver.get(BASE_URL)
    driver.find_element(By.ID, "username").send_keys(VALID_USER)
    driver.find_element(By.ID, "password").send_keys(INVALID_PASS)
    driver.find_element(By.ID, "submit").click()
    time.sleep(1)
    shot(driver, "wrong_password")
    assert "sai tài khoản" in driver.page_source.lower()

def test_login_empty_fields(driver):
    driver.get(BASE_URL)
    driver.find_element(By.ID, "submit").click()
    time.sleep(1)
    shot(driver, "empty_fields")
    assert "vui lòng" in driver.page_source.lower()

def test_forgot_password_link(driver):
    driver.get(BASE_URL)
    driver.find_element(By.LINK_TEXT, "Forgot password?").click()
    time.sleep(1)
    shot(driver, "forgot_password")
    assert "forgot" in driver.current_url.lower()

def test_signup_link(driver):
    driver.get(BASE_URL)
    driver.find_element(By.LINK_TEXT, "SIGN UP").click()
    time.sleep(1)
    shot(driver, "signup_link")
    assert "signup" in driver.current_url.lower()

def test_social_buttons(driver):
    driver.get(BASE_URL)
    socials = driver.find_elements(By.CSS_SELECTOR, ".circle")
    shot(driver, "social_buttons")
    assert len(socials) == 3
