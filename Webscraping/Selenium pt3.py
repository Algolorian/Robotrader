# https://selenium-python.readthedocs.io/
# https://chromedriver.chromium.org/downloads

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

PATH = 'chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")

link = driver.find_element_by_link_text("Python Programming")
link.click()

try:
    element = WebDriverWait(driver, 10).until(  # 10 is the limit to wait
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    element.click()

    element = WebDriverWait(driver, 10).until(  # 10 is the limit to wait
        EC.presence_of_element_located((By.ID, "sow-button-19310003"))
    )
    element.click()

    element = WebDriverWait(driver, 10).until(  # 10 is the limit to wait
        EC.presence_of_element_located((By.ID, "main"))
    )
    print('waited')

    time.sleep(10)
    for _ in range(3):
        driver.back()
        time.sleep(1)

    driver.forward()

except:
    for _ in range(10):
        print("GAVE UP")
finally:
    driver.quit()
