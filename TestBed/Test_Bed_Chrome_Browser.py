#!/usr/bin/env python3


"""
Modules to be imported for running this script
"""
import sys

sys.path.append('../Common_Utilities/')
from Common_Utilities.Common_Utilities import Common_Utilities
import csv
import os
from time import sleep

sys.path.append('../Logger/')
from Logger.Dexcom_Logger import logger

from appium.webdriver.common.touch_action import TouchAction


# os.system('color')

class Test_Bed_Chrome_Browser(Common_Utilities):
    def __init__(self):
        pass

    def operate_Chrome_Browser(self):

        chrome_browser_csv_log_path = os.path.join(self.logger_csv_path, "Chrome_Browser_log.csv")
        lgr_handle = logger(chrome_browser_csv_log_path, self.config_params.get("debug_level"))
        print("-------------------------------------")
        print("Opening Chrome Browser")
        print("-------------------------------------")
        lgr_handle.info("\n")
        lgr_handle.info("Chrome Browser App is opened")
        sleep(2)
        try:
            os.system(
                "adb -s " + self.adb_id + " shell am start -n com.android.chrome/com.google.android.apps.chrome.Main -d " + self.config_params.get(
                    "Browser_URL_1"))
            print("First URL : " + self.config_params.get("Browser_URL_1") + " is opened in Browser")
            lgr_handle.info("First URL : " + self.config_params.get("Browser_URL_1") + " is opened in Browser")
            print("Navigating Up and Down")
            lgr_handle.info("Navigating Up and Down")
            self.Scroll_Down_To_UP()
            sleep(2)
            self.Scroll_Down_To_UP()
            sleep(2)
            self.Scroll_UP_To_Down()
            sleep(2)
            self.Scroll_UP_To_Down()

            os.system(
                "adb -s " + self.adb_id + " shell am start -n com.android.chrome/com.google.android.apps.chrome.Main -d " + self.config_params.get(
                    "Browser_URL_2"))
            print("Second URL : " + self.config_params.get("Browser_URL_2") + " is opened in Browser")
            lgr_handle.info("Second URL : " + self.config_params.get("Browser_URL_2") + " is opened in Browser")
            searchVal = self.config_params.get("Browser_Search")
            self.driver.find_element_by_xpath(".//android.widget.EditText").send_keys(searchVal)
            self.driver.find_element_by_xpath(".//android.widget.Button[@text='Google Search']").click()
            # Press Enter on Mobile keyboard
            os.system("adb -s " + self.adb_id + " shell input keyevent KEYCODE_ENTER")
            sleep(3)
            print("Navigating Up and Down")
            lgr_handle.info("Navigating Up and Down")
            self.Scroll_Down_To_UP()
            sleep(2)
            self.Scroll_Down_To_UP()
            sleep(2)
            self.Scroll_UP_To_Down()
            sleep(2)
            self.Scroll_UP_To_Down()
            sleep(2)
            # Click on Images Tab on Browser
            print("Click on Images Tab")
            lgr_handle.info("Click on Images Tab")
            self.driver.find_element_by_xpath(".//android.widget.TextView[@text='Images']").click()
            print("Navigating Up and Down")
            lgr_handle.info("Navigating Up and Down")
            self.Scroll_Down_To_UP()
            sleep(2)
            self.Scroll_Down_To_UP()
            sleep(2)
            self.Scroll_UP_To_Down()
            sleep(2)
            self.Scroll_UP_To_Down()
            # CLOSE ALL TABS
            lgr_handle.info("Click Switcher Icon--More Options--Close All")
            print("Click Switcher Icon--More Options--Close All")
            self.driver.find_element_by_id("com.android.chrome:id/tab_switcher_button").click()
            sleep(2)
            self.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='More options']").click()
            sleep(2)
            self.driver.find_element_by_xpath("//android.widget.TextView[@content-desc='Close all tabs']").click()
            lgr_handle.info("Closed all opened Tabs in Google Chrome")
            print("Closed all opened Tabs in Google Chrome")
            sleep(5)
            print("Exit: Chrome_Browser")
            print("____________________________________________________________________\n")
            lgr_handle.info("Exit: Chrome_Browser")
            lgr_handle.removeHandler(lgr_handle.handlers[0])

        except Exception as e:
            print(str(e))
            print(type(e))
            lgr_handle.warn(e)
            lgr_handle.warn("**Test_Bed_Chrome_Browser**")
            print("**Test_Bed_Chrome_Browser**")
            for i in range(0, 5):
                self.Press_Device_BackButton()
                sleep(0.2)
                i += 1
            if "A session is either terminated or not started" in str(e):
                self.server_error_recovery()
            if "An unknown server-side error" in str(e):
                self.driver.quit()
                sleep(2)
                self.server_error_recovery()
            lgr_handle.removeHandler(lgr_handle.handlers[0])
