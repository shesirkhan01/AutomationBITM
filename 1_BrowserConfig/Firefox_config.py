from selenium import webdriver


def firefox_launch():
    driver=webdriver.Firefox(executable_path="C:\\Users\\shesi\\Downloads\\geckodriver-v0.32.0-win64\\geckodriver.exe")
    driver.close()


firefox_launch()