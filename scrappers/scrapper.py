from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from django.conf import settings # correct way
import os
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NUMBER_DICT = {"১":"1", "২":"2", "৩":"3", "৪":"4", "৫":"5", "৬":"6", "৭":"8", "৮":"9", "৯":"9", "০":"0" }


class BDScrapper:
    def __init__(self):
        self._url = "https://corona.gov.bd/"
        self._chrome_driver_path, self._webdriver = "", None
       
        self._get_ready_browser()
    

    def _get_ready_browser(self):
        try:
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            self._chrome_driver_path = base_dir +"/driver/chromedriver"

            self._webdriver = webdriver.Chrome(
                executable_path=self._chrome_driver_path,
                options = chrome_options
                )
        except:
            print("Driver not found!")

    
    def _change_number(self, number):
        num = ""
        for n in number:
            num += NUMBER_DICT[n]
        
        return num
    

    def get_data(self):
        try:
            wait = WebDriverWait(self._webdriver, 10)
            print("Mission started! Wait...")
            self._webdriver.get(self._url)
            wait.until(presence_of_element_located((By.CSS_SELECTOR, ".live-update")))
            # get fields
            live_updates = self._webdriver.find_elements_by_class_name("live-update-box")
            data = []
            for update in live_updates:
                h1_tags = update.find_elements_by_css_selector("h1")
                d = (self._change_number(h1_tags[0].text), self._change_number(h1_tags[1].text))
                data.append(d)
            
            self._webdriver.close()
            return data

        except:
            print("Check login url, try again!")

obj = BDScrapper()