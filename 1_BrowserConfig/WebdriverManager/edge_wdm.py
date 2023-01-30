from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def edge_webdriver_manager():
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    driver.maximize_window()
    driver.get("https://google.com")


edge_webdriver_manager()