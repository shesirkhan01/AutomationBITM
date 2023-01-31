from selenium import webdriver
import time


def navigate():
    driver = webdriver.Firefox(executable_path="C:\\Users\\shesi\\Downloads\\geckodriver-v0.32.0-win64\\geckodriver.exe")
    driver.set_window_size(768,1024)

    driver.get("https://demo.opencart.com/")
    time.sleep(5)

    driver.get("https://www.google.com/")
    time.sleep(5)

    driver.back()
    time.sleep(5)

    driver.forward()
    time.sleep(5)

    driver.refresh()
    time.sleep(5)

    driver.close()

navigate()