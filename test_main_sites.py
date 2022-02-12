import csv
import os
import smtplib
import ssl
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from seleniumbase import BaseCase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
# EMAIL_ADDRESS = 'balwinderhayer@gmail.com'
# EMAIL_PASSWORD = 'cold24gnosis'
EMAIL_TO = 'balwinderhayer@wdc.com'

context = ssl.create_default_context()


def notify_user():
    with smtplib.SMTP('mailrelay.wdc.com', 25) as smtp:
        smtp.connect('mailrelay.wdc.com', 25)
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        subject = 'Your Site is Down'
        body = 'Following Test Case Failed'
        msg = f'Subject: {subject}\n\n{body}'
        smtp.sendmail(EMAIL_ADDRESS, 'balwinder.hayer@wdc.com', msg)
        smtp.quit()
        '''
        def test_notify_user():
            msg = "Subject: This is the message"
            with smtplib.SMTP_SSL("smtp.wdc.com") as smtp:
                # smtp.starttls()
                # smtp.ehlo()
                # smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

                # smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.sendmail(EMAIL_ADDRESS, EMAIL_TO, msg)
                print("Done")

                # smtp.sendmail(EMAIL_ADDRESS, 'balwinderhayer@gmail.com', msg)
        '''


class test_sites(unittest.TestCase):
    def test_csv_readerChrome(self, url_chrome):
        self.url_chrome = url_chrome
        self.reader = csv.DictReader(url_chrome, delimiter=',')
        options = webdriver.ChromeOptions()
        self.Chrome = Service(r'C:\chromedriver')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(service=self.Chrome, options=options)
        self.driver.maximize_window()
        # print("------------Chrome Browser Summary------------")
        for line in self.reader:
            self.url = line["Site URL"]
            self.title = line["Site Name"]
            # print(' Site Name: ', self.title)
            time.sleep(2)
            try:
                cat_1 = self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.COMMAND + 't')
                if self.driver.find_element(By.CLASS_NAME, 'applogo'):
                        # if self.driver.find_element.execute_script("return document.querySelector('.applogo')"):
                        time.sleep(5)
                        assert True
                        print("# -- ", self.title, "--")
                        print("Name: ")
                        print("LoadTime: ")
                        print("Chrome: Chrome")
                        print("Status: PASS")
                else:
                        pass
                        print("---")
                # else:
                #     pass
                #     print("down")
            except NoSuchElementException:
                print("# -- ", self.title, "--")
                print("Name: ")
                print("LoadTime: ")
                print("Chrome: Chrome")
                print("Status: FAIL")
                pass
                time.sleep(5)
                # notify_user()
            self.driver.get(self.url)
            time.sleep(4)
        self.driver.quit()


if __name__ == '__main__':
    with open("Web_URL_List.csv") as url_chrome:
        # unittest.main()

        elem_ff = test_sites()
        elem_ff.test_csv_readerChrome(url_chrome)
        time.sleep(4)

'''
        def test_csv_readerFirefox(self, url_fox):
            self.url_fox = url_fox
            self.reader = csv.DictReader(url_fox, delimiter=',')
            # options = webdriver.FirefoxOptions()
            self.Firefox = Service(r'C:\geckodriver')
            # options.add_experimental_option('excludeSwitches', ['enable-logging'])
            self.driver = webdriver.Firefox(service=self.Firefox)
            self.driver.maximize_window()
            print("------------FireFox Browser Summary------------")
            for line in self.reader:
                url = line["Site URL"]
                title = line["Site Name"]
                print('Site URL: ', url + ' Site Name: ', title)
                time.sleep(1)
                try:
                    element = self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.COMMAND + 't')
                    assert True
                    print("STATUS: PASSED, URL Successfully Executed")
                    pass
                except NoSuchElementException:
                    print("STATUS: FAILED")
                    notify_user()
                self.driver.get(url)
                time.sleep(6)
            self.driver.quit()



    def test_csv_readerEdge(self, url_edge):
        self.url_edge = url_edge
        self.reader = csv.DictReader(url_edge, delimiter=',')
        # options = webdriver.edgeOptions()
        self.edge = Service(r'C:\msedgedriver')
        # options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Edge(service=self.edge)
        self.driver.maximize_window()
        print("------------Edge Browser Summary------------")
        for line in self.reader:
            url = line["Site URL"]
            title = line["Site Name"]
            print('Site URL: ', url + ' Site Name: ', title)
            time.sleep(1)
            try:
                element = self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.COMMAND + 't')
                assert True
                print("STATUS: PASSED, URL Successfully Executed")
                self.driver.implicitly_wait(5)
                pass
            except NoSuchElementException:
                print("STATUS: FAILED")
                notify_user()
            self.driver.get(url)
            time.sleep(6)
        self.driver.quit()



if __name__ == '__main__':
    with open("Web_URL_List.csv") as csvfile:
        # unittest.main()

        # test_sites().test_csv_readerChrome()
        # test_sites().test_csv_readerFirefox()
        # test_sites().test_csv_readerEdge()
        # unittest.main()
            # test_csv_readerChrome(unittest.TestCase)
            # test_csv_readerFirefox(unittest.TestCase)
            # test_csv_readerEdge(unittest.TestCase)

        # luke = test_sites()
        # luke.test_csv_readerChrome(csvfile)

        luke1 = test_sites()
        luke1.test_csv_readerFirefox(csvfile)

        luke2 = test_sites()
        luke2.test_csv_readerEdge(csvfile)


        # elem_ch2 = test_sites()
        # elem_ch.test_csv_readerFirefox(url_fox)


        # elem_ch3 = test_sites()
        # elem_ch.test_csv_readerEdge(url_edge)
        # unittest.main(url_chrome)

'''


class test_firefox(unittest.TestCase):
    def test_csv_readerFirefox(self, url_fox):
        self.url_fox = url_fox
        self.reader = csv.DictReader(url_fox, delimiter=',')
        # options = webdriver.FirefoxOptions()
        self.Firefox = Service(r'C:\geckodriver')
        # options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Firefox(service=self.Firefox)
        self.driver.maximize_window()
        print("------------FireFox Browser Summary------------")
        for line in self.reader:
            url = line["Site URL"]
            title = line["Site Name"]
            print('Site URL: ', url + ' Site Name: ', title)
            time.sleep(2)
            try:
                element = self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.COMMAND + 't')
                assert True
                print("STATUS: PASSED, URL Successfully Executed")
                pass
            except NoSuchElementException:
                print("STATUS: FAILED")
                notify_user()
            self.driver.get(url)
            time.sleep(4)
        self.driver.quit()


if __name__ == '__main__':
    with open("Web_URL_List.csv") as url_fox:
        # unittest.main()

        elem_ff1 = test_firefox()
        elem_ff1.test_csv_readerFirefox(url_fox)
        time.sleep(4)


class test_edge(unittest.TestCase):
    def test_csv_readerEdge(self, url_edge):
        self.url_edge = url_edge
        self.reader = csv.DictReader(url_edge, delimiter=',')
        # options = webdriver.edgeOptions()
        self.edge = Service(r'C:\msedgedriver')
        # options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Edge(service=self.edge)
        self.driver.maximize_window()
        print("------------Edge Browser Summary------------")
        for line in self.reader:
            url = line["Site URL"]
            title = line["Site Name"]
            print('Site URL: ', url + ' Site Name: ', title)
            time.sleep(2)
            try:
                element = self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.COMMAND + 't')
                assert True
                print("STATUS: PASSED, URL Successfully Executed")
                self.driver.implicitly_wait(5)
                pass
            except NoSuchElementException:
                print("STATUS: FAILED")
                notify_user()
            self.driver.get(url)
            time.sleep(4)
        self.driver.quit()


if __name__ == '__main__':
    with open("Web_URL_List.csv") as url_edge:
        # unittest.main()
        elem_ed1 = test_edge()
        elem_ed1.test_csv_readerEdge(url_edge)
        time.sleep(4)
