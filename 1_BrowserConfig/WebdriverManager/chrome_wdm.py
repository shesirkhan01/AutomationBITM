from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def chrome_webdriver_manager():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://google.com")

chrome_webdriver_manager()