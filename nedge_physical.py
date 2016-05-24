#################################################################
##                                                             ##
##------------NEXENTA EDGE UI AUTOMATION FRAMEWORK-------------##
##                                                             ##
#################################################################

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
from json_parser import json_parser

import unittest, sys


class nedge_physical(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = NEDGE_UI_URL
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_case(self):
        sid = ""
        vid = ""
        driver = self.driver
        driver.get(self.base_url + "/login")
        
        # verification of browser title
        try:
            self.assertEqual("Nexenta Edge", driver.title)
            print ("verification of browser title - SUCCESS")
        except AssertionError as e:
            print ("verification of browser title - FAILURE")
            self.verificationErrors.append("verification of browser title - FAILURE")
            self.verificationErrors.append(str(e))
        
        # verification of nexenta logo in login page
        try:
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "img[alt=\"Nexenta\"]"))
            print ("verification of nexenta logo in login page - SUCCESS")
        except AssertionError as e:
            print ("verification of nexenta logo in login page - FAILURE")
            self.verificationErrors.append("verification of nexenta logo in login page - FAILURE")
            self.verificationErrors.append(str(e))
        
        # verification of username field
        try:
            self.assertEqual("", driver.find_element_by_name("username").get_attribute("value"))
            print ("verification of username field in login page - SUCCESS")
        except AssertionError as e:
            print ("verification of username field in login page - FAILURE")
            self.verificationErrors.append("verification of username field in login page - FAILURE")
            self.verificationErrors.append(str(e))
        
        # verification of password field
        try:
            self.assertEqual("", driver.find_element_by_name("password").get_attribute("value"))
            print ("verification of password field in login page - SUCCESS")
        except AssertionError as e:
            print ("verification of password field in login page - FAILURE")
            self.verificationErrors.append("verification of password field in login page - FAILURE")
            self.verificationErrors.append(str(e))
        
        # verification of login button
        try:
            self.assertEqual("Login", driver.find_element_by_css_selector("button.btn").text)
            print ("verification of login button in login page - SUCCESS")
        except AssertionError as e:
            print ("verification of login button in login page - FAILURE")
            self.verificationErrors.append("verification of login button in login page - FAILURE")
            self.verificationErrors.append(str(e))
        
        # verification of login functionality
        try:
            driver.find_element_by_name("username").clear()
            driver.find_element_by_name("username").send_keys("admin")
            driver.find_element_by_name("password").clear()
            driver.find_element_by_name("password").send_keys("nexenta")
            driver.find_element_by_css_selector("button.btn").click()
            print ("verification of login functionality - SUCCESS")
        except:
            print ("verification of login functionality - FAILURE")
            self.verificationErrors.append("verification of login functionality - FAILURE")
        
        # verification of browser title post login
        try:
            self.assertEqual("Nexenta Edge", driver.title)
            print ("verification of browser title post login - SUCCESS")
        except AssertionError as e:
            print ("verification of browser title post login - FAILURE")
            self.verificationErrors.append("verification of browser title post login - FAILURE")
            self.verificationErrors.append(str(e))

        # verification of logo in login page post login
        try:
            self.assertEqual("", driver.find_element_by_css_selector("div.AppBar---logo").text)
            print ("verification of nexenta logo in login page post login - SUCCESS")
        except AssertionError as e:
            print ("verification of nexenta logo in login page post login - FAILURE")
            self.verificationErrors.append("verification of nexenta logo in login page post login - FAILURE")
            self.verificationErrors.append(str(e))        

        # verification of physical tab in nedgeui post login
        try: self.assertEqual("Physical", driver.find_element_by_link_text("Physical").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        # verification of logical tab in nedgeui post login
        try: self.assertEqual("Logical", driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/div/div/a[2]/span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        
        # verification of search field in nedgeui post login
        try: self.assertEqual("", driver.find_element_by_css_selector("input.Search---searchInput").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        
        # verification of username dropdown in nedgeui post login
        try: self.assertEqual("Admin", driver.find_element_by_css_selector("span.Menu---menuTitle").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        # verification of cluster health display in nedgeui post login
        try: self.assertEqual("Cluster Health", driver.find_element_by_css_selector("p.HealthChart---label").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(str(json_parser.output("Cluster Health",sid,vid)), driver.find_element_by_css_selector("text.HealthChart---text").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        # verification of cluster health display in nedgeui post login
        try: self.assertEqual("Cluster Health", driver.find_element_by_css_selector("p.HealthChart---label").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(str(json_parser.output("Cluster Health",sid,vid)), driver.find_element_by_css_selector("text.HealthChart---text").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
                                                                   
        # verification of total number of nodes display in nedgeui post login
        try: self.assertEqual("Nodes", driver.find_element_by_css_selector("div.KeyValueTable---key").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(str(json_parser.output("Nodes",sid,vid)), driver.find_element_by_css_selector("div.KeyValueTable---value").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        # verification of total iops display in nedgeui post login
        try: self.assertEqual("Total IOPS", driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[1]/div/div[1]/div/div[2]/div/div[2]/div/div[1]/span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(json_parser.output("Total IOPS",sid,vid), driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[1]/div/div[1]/div/div[2]/div/div[2]/div/div[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        # verification of average latency display in nedgeui post login
        try: self.assertEqual("Average Latency", driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[1]/div/div[1]/div/div[2]/div/div[3]/div/div[1]/span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(json_parser.output("Average Latency",sid,vid), driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[1]/div/div[1]/div/div[2]/div/div[3]/div/div[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        # verification of total number of luns display in nedgeui post login
        try: self.assertEqual("LUNs", driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[1]/div/div[2]/div/div[1]/div/div[1]/span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("0", driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[1]/div/div[2]/div/div[1]/div/div[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
                                                                   
        # verification of iscsi service display in nedgeui post login
        try: self.assertEqual("iSCSI Service", driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[1]/div/div[2]/div/div[2]/div/div[1]/span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("0/0", driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[1]/div/div[2]/div/div[2]/div/div[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
                                                                   
        # verification of amazon s3 gateway display in nedgeui post login
        try: self.assertEqual("Amazon S3 Gateway", driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[1]/div/div[2]/div/div[3]/div/div[1]/span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("0/0", driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[1]/div/div[2]/div/div[3]/div/div[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        # verification of estimated reduction ratio display in nedgeui post login
        try: self.assertEqual("Estimated Reduction Ratio", driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[1]/div/div[3]/div/div[1]/div/div[1]/span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(str(json_parser.output("Estimated Reduction Ratio",sid,vid)), driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[1]/div/div[3]/div/div[1]/div/div[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        # verification of estimated capacity savings display in nedgeui post login
        try: self.assertEqual("Estimated Capacity Savings", driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[1]/div/div[3]/div/div[2]/div/div[1]/span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(str(json_parser.output("Estimated Capacity Savings",sid,vid)), driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[1]/div/div[3]/div/div[2]/div/div[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        # verification of estimated available display in nedgeui post login
        try: self.assertEqual("Estimated Available", driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[1]/div/div[3]/div/div[3]/div/div[1]/span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(str(json_parser.output("Estimated Available",sid,vid)), driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[1]/div/div[3]/div/div[3]/div/div[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        # verification of Utilization display in nedgeui post login
        try: self.assertEqual("Utilization", driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[1]/div/div[3]/div/div[4]/div/div[1]/span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(str(json_parser.output("Utilization",sid,vid)), driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[1]/div/div[3]/div/div[4]/div/div[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        # verification of Number of Objects display in nedgeui post login
        try: self.assertEqual("Number of Objects", driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[1]/div/div[4]/div/div[1]/div/div[1]/span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(str(json_parser.output("Number of Objects",sid,vid)), driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[1]/div/div[4]/div/div[1]/div/div[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        # verification of Servers Online/Degraded display in nedgeui post login
        try: self.assertEqual("Servers Online/Degraded", driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[1]/div/div[4]/div/div[2]/div/div[1]/span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(str(json_parser.output("Servers Online/Degraded",sid,vid)), driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[1]/div/div[4]/div/div[2]/div/div[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        # verification of VDEVS Online/Degraded display in nedgeui post login
        try: self.assertEqual("VDEVS Online/Degraded", driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[1]/div/div[4]/div/div[3]/div/div[1]/span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(str(json_parser.output("VDEVS Online/Degraded",sid,vid)), driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[1]/div/div[4]/div/div[3]/div/div[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        # verification of Total Raw Capacity display in nedgeui post login
        try: self.assertEqual("Total Raw Capacity", driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[1]/div/div[5]/div/div[1]/div/div[1]/span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(str(json_parser.output("Total Raw Capacity",sid,vid)), driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[1]/div/div[5]/div/div[1]/div/div[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        # verification of Physical Free display in nedgeui post login
        try: self.assertEqual("Physical Free", driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[1]/div/div[5]/div/div[2]/div/div[1]/span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(str(json_parser.output("Physical Free",sid,vid)), driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[1]/div/div[5]/div/div[2]/div/div[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        # verification of Physical Allocated display in nedgeui post login
        try: self.assertEqual("Physical Allocated", driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[1]/div/div[5]/div/div[3]/div/div[1]/span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
##        try: self.assertEqual(str(json_parser.output("Physical Allocated",sid,vid)), driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[1]/div/div[5]/div/div[3]/div/div[2]").text)
##        except AssertionError as e: self.verificationErrors.append(str(e))

        # verification of Logical Used display in nedgeui post login
        try: self.assertEqual("Logical Used", driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[1]/div/div[5]/div/div[4]/div/div[1]/span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(str(json_parser.output("Logical Used",sid,vid)), driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[1]/div/div[5]/div/div[4]/div/div[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        # verification of node details
        row = 1
        for i in range(json_parser.output("Nodes",sid,vid)):
            base_xpath = "/html/body/div/div/div[3]/div/div[2]/div[2]/div[2]/div[" + str(row) + "]/div/"
            sid = driver.find_element_by_xpath(base_xpath+"div[1]/div/div[2]/div[2]").text
            try: self.assertEqual(json_parser.output("hostname",sid,vid), driver.find_element_by_xpath(base_xpath+"div[1]/div/div[2]/div[1]").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual(json_parser.output("serverid",sid,vid), driver.find_element_by_xpath(base_xpath+"div[1]/div/div[2]/div[2]").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual("DEVs", driver.find_element_by_xpath(base_xpath+"div[2]/table/tbody/tr[1]/td[1]").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual(json_parser.output("DEVs",sid,vid), driver.find_element_by_xpath(base_xpath+"div[2]/table/tbody/tr[1]/td[2]").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual("CPU", driver.find_element_by_xpath(base_xpath+"div[2]/table/tbody/tr[1]/td[3]").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual(json_parser.output("CPU",sid,vid), driver.find_element_by_xpath(base_xpath+"div[2]/table/tbody/tr[1]/td[4]").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual("IOPS", driver.find_element_by_xpath(base_xpath+"div[2]/table/tbody/tr[2]/td[1]").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual(json_parser.output("IOPS",sid,vid), driver.find_element_by_xpath(base_xpath+"div[2]/table/tbody/tr[2]/td[2]").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual("MEM", driver.find_element_by_xpath(base_xpath+"div[2]/table/tbody/tr[2]/td[3]").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual(json_parser.output("MEM",sid,vid), driver.find_element_by_xpath(base_xpath+"div[2]/table/tbody/tr[2]/td[4]").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual("LAT", driver.find_element_by_xpath(base_xpath+"div[2]/table/tbody/tr[3]/td[1]").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual(json_parser.output("LAT",sid,vid), driver.find_element_by_xpath(base_xpath+"div[2]/table/tbody/tr[3]/td[2]").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual(json_parser.output("UTILIZATION",sid,vid), driver.find_element_by_xpath(base_xpath+"div[2]/div[2]/div[1]/div[1]/span[1]").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual("UTILIZATION", driver.find_element_by_xpath(base_xpath+"div[2]/div[2]/div[1]/div[1]/span[2]/span").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual(json_parser.output("CAPACITY",sid,vid), driver.find_element_by_xpath(base_xpath+"div[2]/div[2]/div[1]/div[2]/span[1]").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual("CAPACITY", driver.find_element_by_xpath(base_xpath+"div[2]/div[2]/div[1]/div[2]/span[2]/span").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            element = driver.find_element_by_xpath(base_xpath+"div[1]/div/div[2]/div[1]")
            hover = ActionChains(driver).move_to_element(element)
            hover.perform()
            driver.find_element_by_css_selector("div.ServerCard---detailsButton > span").click()        
            try: self.assertEqual("Node details", driver.find_element_by_css_selector("h2.ServerCardDetails---title > span").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='app']/div/div[3]/div/span/div/div/i"))
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual(json_parser.output("hostname",sid,vid), driver.find_element_by_css_selector("div.ServerCardDetails---descriptionName").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual(json_parser.output("serverid",sid,vid), driver.find_element_by_css_selector("div.ServerCardDetails---descriptionId").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual("Drive", driver.find_element_by_xpath("/html/body/div/div/div[3]/div/span/div/div[2]/div[2]/table/thead/tr/th[1]/span").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual("UTIL", driver.find_element_by_xpath("/html/body/div/div/div[3]/div/span/div/div[2]/div[2]/table/thead/tr/th[2]/span").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual("CAP", driver.find_element_by_xpath("/html/body/div/div/div[3]/div/span/div/div[2]/div[2]/table/thead/tr/th[3]/span").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual("RLAT", driver.find_element_by_xpath("/html/body/div/div/div[3]/div/span/div/div[2]/div[2]/table/thead/tr/th[4]/span").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual("WLAT", driver.find_element_by_xpath("/html/body/div/div/div[3]/div/span/div/div[2]/div[2]/table/thead/tr/th[5]/span").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            column = 1
            for i in range(json_parser.output("number_of_vdevs",sid,vid)):
                base_xpath_vdev = "/html/body/div/div/div[3]/div/span/div/div[2]/div[2]/table/tbody/tr["+str(column)+"]/"
                base_xpath_novdev = "/html/body/div/div/div[3]/div/span/div/div[2]/div[2]/table/tbody/tr/"
                vid = driver.find_element_by_xpath(base_xpath_vdev+"td[1]/div/div[2]/div[2]").text
                if vid == "00000000000000000000000000000000":
                    try: self.assertEqual(json_parser.output("vdevid",sid,vid), driver.find_element_by_xpath(base_xpath_novdev+"td[1]/div/div[2]/div[2]").text)
                    except AssertionError as e: self.verificationErrors.append(str(e))
                    try: self.assertEqual(json_parser.output("UTIL",sid,vid), driver.find_element_by_xpath(base_xpath_novdev+"td[2]").text)
                    except AssertionError as e: self.verificationErrors.append(str(e))
                    try: self.assertEqual(json_parser.output("CAP",sid,vid), driver.find_element_by_xpath(base_xpath_novdev+"td[3]").text)
                    except AssertionError as e: self.verificationErrors.append(str(e))
                    print(json_parser.output("RLAT",sid,vid))
                    print(json_parser.output("WLAT",sid,vid))
                    try: self.assertEqual(json_parser.output("RLAT",sid,vid), driver.find_element_by_xpath(base_xpath_novdev+"td[4]").text)
                    except AssertionError as e: self.verificationErrors.append(str(e))
                    try: self.assertEqual(json_parser.output("WLAT",sid,vid), driver.find_element_by_xpath(base_xpath_novdev+"td[5]").text)
                    except AssertionError as e: self.verificationErrors.append(str(e))
                else:
                    try: self.assertEqual(json_parser.output("devname",sid,vid), driver.find_element_by_xpath(base_xpath_vdev+"td[1]/div/div[2]/div[1]").text)
                    except AssertionError as e: self.verificationErrors.append(str(e))
                    try: self.assertEqual(json_parser.output("vdevid",sid,vid), driver.find_element_by_xpath(base_xpath_vdev+"td[1]/div/div[2]/div[2]").text)
                    except AssertionError as e: self.verificationErrors.append(str(e))
                    try: self.assertEqual(json_parser.output("UTIL",sid,vid), driver.find_element_by_xpath(base_xpath_vdev+"td[2]").text)
                    except AssertionError as e: self.verificationErrors.append(str(e))
                    try: self.assertEqual(json_parser.output("CAP",sid,vid), driver.find_element_by_xpath(base_xpath_vdev+"td[3]").text)
                    except AssertionError as e: self.verificationErrors.append(str(e))
                    try: self.assertEqual(json_parser.output("RLAT",sid,vid), driver.find_element_by_xpath(base_xpath_vdev+"td[4]").text)
                    except AssertionError as e: self.verificationErrors.append(str(e))
                    try: self.assertEqual(json_parser.output("WLAT",sid,vid), driver.find_element_by_xpath(base_xpath_vdev+"td[5]").text)
                    except AssertionError as e: self.verificationErrors.append(str(e))
                column = column + 1
            driver.find_element_by_xpath("//div[@id='app']/div/div[3]/div/span/div/div/i").click()
            row = row + 1

        # verification of search functionality based on serverid
        for index in range(len(json_parser.output("servers",sid,vid))):
            base_xpath = "/html/body/div/div/div[3]/div/div[2]/div[2]/div[2]/div[1]/div/"
            sid = json_parser.output("servers",sid,vid)[index]
            driver.find_element_by_css_selector("input.Search---searchInput").clear()
            driver.find_element_by_css_selector("input.Search---searchInput").send_keys("")
            driver.find_element_by_css_selector("input.Search---searchInput").clear()
            driver.find_element_by_css_selector("input.Search---searchInput").send_keys(sid)
            try: self.assertEqual(json_parser.output("hostname",sid,vid), driver.find_element_by_xpath(base_xpath+"div[1]/div/div[2]/div[1]").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual(json_parser.output("serverid",sid,vid), driver.find_element_by_xpath(base_xpath+"div[1]/div/div[2]/div[2]").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual("DEVs", driver.find_element_by_xpath(base_xpath+"div[2]/table/tbody/tr[1]/td[1]").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual(json_parser.output("DEVs",sid,vid), driver.find_element_by_xpath(base_xpath+"div[2]/table/tbody/tr[1]/td[2]").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual("CPU", driver.find_element_by_xpath(base_xpath+"div[2]/table/tbody/tr[1]/td[3]").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual(json_parser.output("CPU",sid,vid), driver.find_element_by_xpath(base_xpath+"div[2]/table/tbody/tr[1]/td[4]").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual("IOPS", driver.find_element_by_xpath(base_xpath+"div[2]/table/tbody/tr[2]/td[1]").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual(json_parser.output("IOPS",sid,vid), driver.find_element_by_xpath(base_xpath+"div[2]/table/tbody/tr[2]/td[2]").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual("MEM", driver.find_element_by_xpath(base_xpath+"div[2]/table/tbody/tr[2]/td[3]").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual(json_parser.output("MEM",sid,vid), driver.find_element_by_xpath(base_xpath+"div[2]/table/tbody/tr[2]/td[4]").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual("LAT", driver.find_element_by_xpath(base_xpath+"div[2]/table/tbody/tr[3]/td[1]").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual(json_parser.output("LAT",sid,vid), driver.find_element_by_xpath(base_xpath+"div[2]/table/tbody/tr[3]/td[2]").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual(json_parser.output("UTILIZATION",sid,vid), driver.find_element_by_xpath(base_xpath+"div[2]/div[2]/div[1]/div[1]/span[1]").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual("UTILIZATION", driver.find_element_by_xpath(base_xpath+"div[2]/div[2]/div[1]/div[1]/span[2]/span").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual(json_parser.output("CAPACITY",sid,vid), driver.find_element_by_xpath(base_xpath+"div[2]/div[2]/div[1]/div[2]/span[1]").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual("CAPACITY", driver.find_element_by_xpath(base_xpath+"div[2]/div[2]/div[1]/div[2]/span[2]/span").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            element = driver.find_element_by_xpath(base_xpath+"div[1]/div/div[2]/div[1]")
            hover = ActionChains(driver).move_to_element(element)
            hover.perform()
            driver.find_element_by_css_selector("div.ServerCard---detailsButton > span").click()        
            try: self.assertEqual("Node details", driver.find_element_by_css_selector("h2.ServerCardDetails---title > span").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='app']/div/div[3]/div/span/div/div/i"))
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual(json_parser.output("hostname",sid,vid), driver.find_element_by_css_selector("div.ServerCardDetails---descriptionName").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual(json_parser.output("serverid",sid,vid), driver.find_element_by_css_selector("div.ServerCardDetails---descriptionId").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual("Drive", driver.find_element_by_xpath("/html/body/div/div/div[3]/div/span/div/div[2]/div[2]/table/thead/tr/th[1]/span").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual("UTIL", driver.find_element_by_xpath("/html/body/div/div/div[3]/div/span/div/div[2]/div[2]/table/thead/tr/th[2]/span").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual("CAP", driver.find_element_by_xpath("/html/body/div/div/div[3]/div/span/div/div[2]/div[2]/table/thead/tr/th[3]/span").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual("RLAT", driver.find_element_by_xpath("/html/body/div/div/div[3]/div/span/div/div[2]/div[2]/table/thead/tr/th[4]/span").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual("WLAT", driver.find_element_by_xpath("/html/body/div/div/div[3]/div/span/div/div[2]/div[2]/table/thead/tr/th[5]/span").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            column = 1
            for i in range(json_parser.output("number_of_vdevs",sid,vid)):
                base_xpath_vdev = "/html/body/div/div/div[3]/div/span/div/div[2]/div[2]/table/tbody/tr["+str(column)+"]/"
                base_xpath_novdev = "/html/body/div/div/div[3]/div/span/div/div[2]/div[2]/table/tbody/tr/"
                vid = driver.find_element_by_xpath(base_xpath_vdev+"td[1]/div/div[2]/div[2]").text
                if vid == "00000000000000000000000000000000":
                    try: self.assertEqual(json_parser.output("vdevid",sid,vid), driver.find_element_by_xpath(base_xpath_novdev+"td[1]/div/div[2]/div[2]").text)
                    except AssertionError as e: self.verificationErrors.append(str(e))
                    try: self.assertEqual(json_parser.output("UTIL",sid,vid), driver.find_element_by_xpath(base_xpath_novdev+"td[2]").text)
                    except AssertionError as e: self.verificationErrors.append(str(e))
                    try: self.assertEqual(json_parser.output("CAP",sid,vid), driver.find_element_by_xpath(base_xpath_novdev+"td[3]").text)
                    except AssertionError as e: self.verificationErrors.append(str(e))
                    print(json_parser.output("RLAT",sid,vid))
                    print(json_parser.output("WLAT",sid,vid))
                    try: self.assertEqual(json_parser.output("RLAT",sid,vid), driver.find_element_by_xpath(base_xpath_novdev+"td[4]").text)
                    except AssertionError as e: self.verificationErrors.append(str(e))
                    try: self.assertEqual(json_parser.output("WLAT",sid,vid), driver.find_element_by_xpath(base_xpath_novdev+"td[5]").text)
                    except AssertionError as e: self.verificationErrors.append(str(e))
                else:
                    try: self.assertEqual(json_parser.output("devname",sid,vid), driver.find_element_by_xpath(base_xpath_vdev+"td[1]/div/div[2]/div[1]").text)
                    except AssertionError as e: self.verificationErrors.append(str(e))
                    try: self.assertEqual(json_parser.output("vdevid",sid,vid), driver.find_element_by_xpath(base_xpath_vdev+"td[1]/div/div[2]/div[2]").text)
                    except AssertionError as e: self.verificationErrors.append(str(e))
                    try: self.assertEqual(json_parser.output("UTIL",sid,vid), driver.find_element_by_xpath(base_xpath_vdev+"td[2]").text)
                    except AssertionError as e: self.verificationErrors.append(str(e))
                    try: self.assertEqual(json_parser.output("CAP",sid,vid), driver.find_element_by_xpath(base_xpath_vdev+"td[3]").text)
                    except AssertionError as e: self.verificationErrors.append(str(e))
                    try: self.assertEqual(json_parser.output("RLAT",sid,vid), driver.find_element_by_xpath(base_xpath_vdev+"td[4]").text)
                    except AssertionError as e: self.verificationErrors.append(str(e))
                    try: self.assertEqual(json_parser.output("WLAT",sid,vid), driver.find_element_by_xpath(base_xpath_vdev+"td[5]").text)
                    except AssertionError as e: self.verificationErrors.append(str(e))
                column = column + 1
            driver.find_element_by_xpath("//div[@id='app']/div/div[3]/div/span/div/div/i").click()

        # verification of search functionality based on hostname
        for index in range(len(json_parser.output("servers",sid,vid))):
            base_xpath = "/html/body/div/div/div[3]/div/div[2]/div[2]/div[2]/div[1]/div/"
            sid = json_parser.output("servers",sid,vid)[index]
            hostname = json_parser.output("hostname",sid,vid)
            driver.find_element_by_css_selector("input.Search---searchInput").clear()
            driver.find_element_by_css_selector("input.Search---searchInput").send_keys("")
            driver.find_element_by_css_selector("input.Search---searchInput").clear()
            driver.find_element_by_css_selector("input.Search---searchInput").send_keys(hostname)
            try: self.assertEqual(json_parser.output("hostname",sid,vid), driver.find_element_by_xpath(base_xpath+"div[1]/div/div[2]/div[1]").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual(json_parser.output("serverid",sid,vid), driver.find_element_by_xpath(base_xpath+"div[1]/div/div[2]/div[2]").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual("DEVs", driver.find_element_by_xpath(base_xpath+"div[2]/table/tbody/tr[1]/td[1]").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual(json_parser.output("DEVs",sid,vid), driver.find_element_by_xpath(base_xpath+"div[2]/table/tbody/tr[1]/td[2]").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual("CPU", driver.find_element_by_xpath(base_xpath+"div[2]/table/tbody/tr[1]/td[3]").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual(json_parser.output("CPU",sid,vid), driver.find_element_by_xpath(base_xpath+"div[2]/table/tbody/tr[1]/td[4]").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual("IOPS", driver.find_element_by_xpath(base_xpath+"div[2]/table/tbody/tr[2]/td[1]").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual(json_parser.output("IOPS",sid,vid), driver.find_element_by_xpath(base_xpath+"div[2]/table/tbody/tr[2]/td[2]").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual("MEM", driver.find_element_by_xpath(base_xpath+"div[2]/table/tbody/tr[2]/td[3]").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual(json_parser.output("MEM",sid,vid), driver.find_element_by_xpath(base_xpath+"div[2]/table/tbody/tr[2]/td[4]").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual("LAT", driver.find_element_by_xpath(base_xpath+"div[2]/table/tbody/tr[3]/td[1]").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual(json_parser.output("LAT",sid,vid), driver.find_element_by_xpath(base_xpath+"div[2]/table/tbody/tr[3]/td[2]").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual(json_parser.output("UTILIZATION",sid,vid), driver.find_element_by_xpath(base_xpath+"div[2]/div[2]/div[1]/div[1]/span[1]").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual("UTILIZATION", driver.find_element_by_xpath(base_xpath+"div[2]/div[2]/div[1]/div[1]/span[2]/span").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual(json_parser.output("CAPACITY",sid,vid), driver.find_element_by_xpath(base_xpath+"div[2]/div[2]/div[1]/div[2]/span[1]").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual("CAPACITY", driver.find_element_by_xpath(base_xpath+"div[2]/div[2]/div[1]/div[2]/span[2]/span").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            element = driver.find_element_by_xpath(base_xpath+"div[1]/div/div[2]/div[1]")
            hover = ActionChains(driver).move_to_element(element)
            hover.perform()
            driver.find_element_by_css_selector("div.ServerCard---detailsButton > span").click()        
            try: self.assertEqual("Node details", driver.find_element_by_css_selector("h2.ServerCardDetails---title > span").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='app']/div/div[3]/div/span/div/div/i"))
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual(json_parser.output("hostname",sid,vid), driver.find_element_by_css_selector("div.ServerCardDetails---descriptionName").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual(json_parser.output("serverid",sid,vid), driver.find_element_by_css_selector("div.ServerCardDetails---descriptionId").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual("Drive", driver.find_element_by_xpath("/html/body/div/div/div[3]/div/span/div/div[2]/div[2]/table/thead/tr/th[1]/span").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual("UTIL", driver.find_element_by_xpath("/html/body/div/div/div[3]/div/span/div/div[2]/div[2]/table/thead/tr/th[2]/span").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual("CAP", driver.find_element_by_xpath("/html/body/div/div/div[3]/div/span/div/div[2]/div[2]/table/thead/tr/th[3]/span").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual("RLAT", driver.find_element_by_xpath("/html/body/div/div/div[3]/div/span/div/div[2]/div[2]/table/thead/tr/th[4]/span").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual("WLAT", driver.find_element_by_xpath("/html/body/div/div/div[3]/div/span/div/div[2]/div[2]/table/thead/tr/th[5]/span").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            column = 1
            for i in range(json_parser.output("number_of_vdevs",sid,vid)):
                base_xpath_vdev = "/html/body/div/div/div[3]/div/span/div/div[2]/div[2]/table/tbody/tr["+str(column)+"]/"
                base_xpath_novdev = "/html/body/div/div/div[3]/div/span/div/div[2]/div[2]/table/tbody/tr/"
                vid = driver.find_element_by_xpath(base_xpath_vdev+"td[1]/div/div[2]/div[2]").text
                if vid == "00000000000000000000000000000000":
                    try: self.assertEqual(json_parser.output("vdevid",sid,vid), driver.find_element_by_xpath(base_xpath_novdev+"td[1]/div/div[2]/div[2]").text)
                    except AssertionError as e: self.verificationErrors.append(str(e))
                    try: self.assertEqual(json_parser.output("UTIL",sid,vid), driver.find_element_by_xpath(base_xpath_novdev+"td[2]").text)
                    except AssertionError as e: self.verificationErrors.append(str(e))
                    try: self.assertEqual(json_parser.output("CAP",sid,vid), driver.find_element_by_xpath(base_xpath_novdev+"td[3]").text)
                    except AssertionError as e: self.verificationErrors.append(str(e))
                    print(json_parser.output("RLAT",sid,vid))
                    print(json_parser.output("WLAT",sid,vid))
                    try: self.assertEqual(json_parser.output("RLAT",sid,vid), driver.find_element_by_xpath(base_xpath_novdev+"td[4]").text)
                    except AssertionError as e: self.verificationErrors.append(str(e))
                    try: self.assertEqual(json_parser.output("WLAT",sid,vid), driver.find_element_by_xpath(base_xpath_novdev+"td[5]").text)
                    except AssertionError as e: self.verificationErrors.append(str(e))
                else:
                    try: self.assertEqual(json_parser.output("devname",sid,vid), driver.find_element_by_xpath(base_xpath_vdev+"td[1]/div/div[2]/div[1]").text)
                    except AssertionError as e: self.verificationErrors.append(str(e))
                    try: self.assertEqual(json_parser.output("vdevid",sid,vid), driver.find_element_by_xpath(base_xpath_vdev+"td[1]/div/div[2]/div[2]").text)
                    except AssertionError as e: self.verificationErrors.append(str(e))
                    try: self.assertEqual(json_parser.output("UTIL",sid,vid), driver.find_element_by_xpath(base_xpath_vdev+"td[2]").text)
                    except AssertionError as e: self.verificationErrors.append(str(e))
                    try: self.assertEqual(json_parser.output("CAP",sid,vid), driver.find_element_by_xpath(base_xpath_vdev+"td[3]").text)
                    except AssertionError as e: self.verificationErrors.append(str(e))
                    try: self.assertEqual(json_parser.output("RLAT",sid,vid), driver.find_element_by_xpath(base_xpath_vdev+"td[4]").text)
                    except AssertionError as e: self.verificationErrors.append(str(e))
                    try: self.assertEqual(json_parser.output("WLAT",sid,vid), driver.find_element_by_xpath(base_xpath_vdev+"td[5]").text)
                    except AssertionError as e: self.verificationErrors.append(str(e))
                column = column + 1
            driver.find_element_by_xpath("//div[@id='app']/div/div[3]/div/span/div/div/i").click()
        
        # verification of about popup
        driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div[2]/div[2]/div/div/i").click()
        driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div[2]/div[2]/div[2]/ul/li/span[2]").click()
        try: self.assertEqual("About NexentaEdge", driver.find_element_by_css_selector("div.Dialog---title").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='app']/div/div/span/div/div/i"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "img[alt=\"NexentaEdge logo\"]"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Software:", driver.find_element_by_css_selector("div.KeyValueTable---key").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Nexenta Edge", driver.find_element_by_css_selector("div.KeyValueTable---value").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Version:", driver.find_element_by_xpath("/html/body/div/div/div[1]/span/div/div[2]/div/div[2]/div/div[1]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(json_parser.output("nedge-version",sid,vid), driver.find_element_by_xpath("/html/body/div/div/div[1]/span/div/div[2]/div/div[2]/div/div[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Patents:", driver.find_element_by_css_selector("div.Dialog---dialogBody > span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Multicast collaborative erasure encoding and distributed parity protection", driver.find_element_by_link_text("Multicast collaborative erasure encoding and distributed parity protection").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Object storage system with local transaction logs, a distributed namespace, and optimized support for user directories", driver.find_element_by_link_text("Object storage system with local transaction logs, a distributed namespace, and optimized support for user directories").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Scalable object storage using multicast transport", driver.find_element_by_link_text("Scalable object storage using multicast transport").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Systems and methods for scalable object storage", driver.find_element_by_link_text("Systems and methods for scalable object storage").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Scalable transport with cluster-consensus rendezvous", driver.find_element_by_link_text("Scalable transport with cluster-consensus rendezvous").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Scalable transport with client-consensus rendezvous", driver.find_element_by_link_text("Scalable transport with client-consensus rendezvous").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Scalable transport system for multicast replication", driver.find_element_by_link_text("Scalable transport system for multicast replication").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Documentation", driver.find_element_by_link_text("Documentation").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Copyright 2005-2016, Nexenta Systems, Inc. All rights reserved.", driver.find_element_by_xpath("//div[@id='app']/div/div/span/div/div[2]/span[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath("//div[@id='app']/div/div/span/div/div/i").click()

        # verification of license popup
        driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div[2]/div[2]/div/div/i").click()
        driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div[2]/div[2]/div[2]/ul/li[2]/span[2]").click()
        try: self.assertEqual("License Information", driver.find_element_by_css_selector("div.Dialog---title").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='app']/div/div/span/div/div/i"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Installation GUID:", driver.find_element_by_xpath("/html/body/div/div/div[1]/span/div/div[2]/div[1]/div[1]/div/div[1]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(json_parser.output("Installation GUID",sid,vid), driver.find_element_by_xpath("/html/body/div/div/div[1]/span/div/div[2]/div[1]/div[1]/div/div[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("License Type:", driver.find_element_by_xpath("/html/body/div/div/div[1]/span/div/div[2]/div[1]/div[2]/div/div[1]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(json_parser.output("License Type",sid,vid), driver.find_element_by_xpath("/html/body/div/div/div[1]/span/div/div[2]/div[1]/div[2]/div/div[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("License Serial Number:", driver.find_element_by_xpath("/html/body/div/div/div[1]/span/div/div[2]/div[1]/div[3]/div/div[1]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(json_parser.output("License Serial Number",sid,vid), driver.find_element_by_xpath("/html/body/div/div/div[1]/span/div/div[2]/div[1]/div[3]/div/div[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("License Base Capacity:", driver.find_element_by_xpath("/html/body/div/div/div[1]/span/div/div[2]/div[1]/div[4]/div/div[1]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(json_parser.output("License Base Capacity",sid,vid), driver.find_element_by_xpath("/html/body/div/div/div[1]/span/div/div[2]/div[1]/div[4]/div/div[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("License Expiration Date:", driver.find_element_by_xpath("/html/body/div/div/div[1]/span/div/div[2]/div[1]/div[5]/div/div[1]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(json_parser.output("License Expiration Date",sid,vid), driver.find_element_by_xpath("/html/body/div/div/div[1]/span/div/div[2]/div[1]/div[5]/div/div[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        if json_parser.output("License Status",sid,vid) == "License has expired":
            try: self.assertEqual(json_parser.output("License Status",sid,vid), driver.find_element_by_xpath("/html/body/div/div/div[1]/span/div/div[2]/div[2]/div/span").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath("//div[@id='app']/div/div/span/div/div/i").click()
        
        # verification of clear status functionality
        driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div[2]/div[2]/div/div/i").click()
        driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div[2]/div[2]/div[2]/ul/li[3]/span[2]").click()
        try: self.assertEqual("SUCCES", driver.find_element_by_css_selector("h4.ActionDialog---title").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Status cleared", driver.find_element_by_css_selector("div.ActionDialog---content").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Close", driver.find_element_by_css_selector("button.Button---btn").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_css_selector("button.Button---btn").click()
            
        # verification of logout functionality
        driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div[2]/div[2]/div/div/i").click()
        driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div[2]/div[2]/div[2]/ul/li[4]/i").click()
        

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

# JSON PARSER
json_parser = json_parser()

# URL FOR NEDGE UI
NEDGE_UI_URL = "http://10.3.31.102:3000/"
        
if __name__ == "__main__":
    unittest.main()
