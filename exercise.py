import time
from datetime import datetime
from selenium import webdriver
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r'C:\chromedriver.exe')
driver.get('http://svc-adveappsvc@wdc.com:2GpY9tx5FN7xx2@adve.wdc.com/ITRCentral/')
driver.refresh()
start1 = datetime.now()
# WebDriverWait(driver, 1).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "_siteLoadedDiv")))
# LOAD Time
N = 0
while N < 1000000000:
    try:
        # driver.refresh()
        # start1 = datetime.now()

        elem = driver.execute_script("return _siteLoaded")
        if elem == True:
            end1 = datetime.now()
            total_time1 = end1 - start1
        N = 10
        print(elem, total_time1)
        break
        N += 1
        # time.sleep(1)

    except:
        print("time")
        time.sleep(10)
        N += 10

# while True:
#     try:
#         if driver.execute_script("return _siteLoaded"):
#             print("True")
#             break
#         elif not driver.execute_script("return _siteLoaded"):
#             print("False")
#             break
#         # element2 = driver.execute_script("return _siteLoaded")
#         # element = driver.execute_script("return document.getElementsByClassName('_siteLoadDiv')")
#         # print(element)
#         # print(element2)
#     finally:
#         pass
