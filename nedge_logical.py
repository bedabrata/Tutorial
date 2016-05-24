# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class nedge_logical(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://10.3.31.102:3000/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_case(self):
        driver = self.driver
        driver.get(self.base_url + "/login")
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("nexenta")
        driver.find_element_by_css_selector("button.btn").click()
        driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/div/div/a[2]/span").click()
        
        driver.find_element_by_xpath("//div[@id='app']/div/div[3]/div/section[2]/div/div/div[2]/button").click()
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys("cluster01")
        driver.find_element_by_css_selector("button.Button---btn.Button---btn-success").click()
        driver.find_element_by_xpath("//div[@id='app']/div/div[3]/div/section[2]/div/div[2]/div/div/div[3]/div/div/div/div[2]/div/div/div/div/div/div/span[2]").click()
        driver.find_element_by_xpath("//div[@id='app']/div/div[3]/div/section[2]/div/div/div[3]/button").click()
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys("tenant01")
        driver.find_element_by_css_selector("button.Button---btn.Button---btn-success").click()
        driver.find_element_by_css_selector("div.TenantsTable---deleteIcon.TenantsTable---iconOverlay").click()
        driver.find_element_by_css_selector("button.Button---btn.Button---btn-danger").click()
        driver.find_element_by_css_selector("li > a > span").click()
        driver.find_element_by_css_selector("i.fa.fa-trash").click()
        driver.find_element_by_css_selector("button.Button---btn.Button---btn-danger").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
