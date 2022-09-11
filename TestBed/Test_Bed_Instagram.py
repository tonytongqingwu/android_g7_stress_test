#!/usr/bin/env python3



"""
Modules to be imported for running this script
"""
import sys
sys.path.append('../Common_Utilities/')
from Common_Utilities.Common_Utilities import Common_Utilities
import csv
import os
sys.path.append('../Logger/')
from Logger.Dexcom_Logger import logger

from appium.webdriver.common.touch_action import TouchAction
# os.system('color')




from time import sleep

class Test_Bed_Instagram(Common_Utilities):
    def __init__(self):
        pass



    def operate_Instagram(self):
        Instagram_csv_log_path = os.path.join(self.logger_csv_path,"Instagram_log.csv")
        lgr_handle = logger(Instagram_csv_log_path,self.config_params.get("debug_level"))
        print("-------------------------------------")
        print("Instagram App is opened")
        print("-------------------------------------")
        os.system("adb -s "+self.adb_id+" shell am start -n com.instagram.android/com.instagram.mainactivity.MainActivity")
        lgr_handle.info("\n")
        lgr_handle.info("Instagram App is opened")
        sleep(4)
        try:
            print("First Navigating Up and Down")
            lgr_handle.info("First Navigating Up and Down")
            self.Scroll_Down_To_UP()
            self.Scroll_Down_To_UP()
            sleep(2)
            self.Scroll_UP_To_Down()
            self.Scroll_UP_To_Down()
            #Click on Search Icon
            print("Click on Search icon ")
            lgr_handle.info("Click on Search icon")
            self.driver.find_element_by_xpath(".//android.widget.Button[contains(@content-desc,'Search')]").click()
            sleep(5)
            print("Enter search criteria")
            self.driver.find_element_by_xpath(".//android.widget.EditText").click()
            searchVal=self.config_params.get("Instagram_search")
            self.driver.find_element_by_xpath(".//android.widget.EditText").send_keys(searchVal)
            sleep(2)
            self.Press_Enter_MobileKeyBoard()
            sleep(2)
            lgr_handle.info("Searched value is: '"+searchVal+"'")
            print("Searched value is: '"+searchVal+"'")
            sleep(2)
            self.driver.find_element_by_xpath(".//android.widget.ImageView[@index='0']").click()
            sleep(2)
            print("Navigating Up and Down")
            lgr_handle.info("Navigating Up and Down")
            self.Scroll_Down_To_UP()
            sleep(2)
            self.Scroll_UP_To_Down()
            lgr_handle.info("Press Back Button")
            print("Press Device BackButton")
            for i in range(0,3):
                self.Press_Device_BackButton()
                sleep(0.2)
            lgr_handle.info("Exit: Instagram")
            print("Exit: Instagram") 
            print("____________________________________________________________________\n")
            for i in range(0,5):
                self.Press_Device_BackButton()
                sleep(0.1)
                i+=1
            lgr_handle.removeHandler(lgr_handle.handlers[0]) 
                       
                
        except Exception as e:
            print(str(e))
            print(type(e))
            lgr_handle.warn(e)
            lgr_handle.warn("**Test_Bed_Instagram**")
            print("**Test_Bed_Instagram**")
            for i in range(0,5):
                self.Press_Device_BackButton()
                sleep(0.2)
                i+=1
            if "A session is either terminated or not started" in str(e):
                self.server_error_recovery()
            if "An unknown server-side error" in str(e):
                self.driver.quit()
                sleep(2)
                self.server_error_recovery()
            lgr_handle.removeHandler(lgr_handle.handlers[0])
           
            
