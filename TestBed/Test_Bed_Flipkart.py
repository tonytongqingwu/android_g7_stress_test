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

class Test_Bed_Flipkart(Common_Utilities):
    def __init__(self):
        pass



    def operate_flipkart(self):
        flipkart_csv_log_path = os.path.join(self.logger_csv_path,"Flipkart_log.csv")
        lgr_handle = logger(flipkart_csv_log_path,self.config_params.get("debug_level"))
        print("-------------------------------------")
        print("Flipkart App is opened")
        print("-------------------------------------")
        os.system("adb -s "+self.adb_id+" shell am start -n com.flipkart.android/com.flipkart.android.activity.HomeFragmentHolderActivity")
        lgr_handle.info("\n")
        lgr_handle.info("Flipkart App is opened")
        sleep(4)
        try:
            #Click on Search Icon
            print("Click on Search icon ")
            lgr_handle.info("Click on Search icon")
            self.driver.find_element_by_xpath(".//android.widget.TextView[contains(@text,'Search')]").click()
            sleep(5)
            print("Enter first search criteria")
            searchVal_1=self.config_params.get("Shopping_search_1")
            self.driver.find_element_by_xpath(".//android.widget.EditText").send_keys(searchVal_1)
            sleep(5)
            lgr_handle.info("Launched shopping app, second searched value is: '"+searchVal_1+"'")
            print("Launched shopping app, first searched value is: '"+searchVal_1+"'")
            self.driver.find_element_by_id("com.flipkart.android:id/img_product").click()
            sleep(2)
            print("Navigating Up and Down")
            self.Scroll_Down_To_UP()
            sleep(2)
            self.Scroll_Down_To_UP()
            sleep(2)
            self.Scroll_UP_To_Down()
            sleep(2)
            self.Scroll_UP_To_Down()
            lgr_handle.info("Press Back Button")
            print("Press Device BackButton")
            for i in range(0,3):
                self.Press_Device_BackButton()
                sleep(0.2)
                i+=1
            
            #Click on Search Icon
            lgr_handle.info("Click on Search icon")
            print("Click on Search icon again for second search item")
            self.driver.find_element_by_xpath(".//android.widget.TextView[contains(@text,'Search')]").click()
            sleep(5)
            print("Enter second search criteria")
            searchVal_2=self.config_params.get("Shopping_search_2")
            self.driver.find_element_by_xpath(".//android.widget.EditText").send_keys(searchVal_2)
            sleep(5)
            #self.ScreenShort()
            lgr_handle.info("Launched shopping app, second searched value is: '"+searchVal_2+"'")
            print("Launched shopping app, second searched value is: '"+searchVal_2+"'")
            self.driver.find_element_by_id("com.flipkart.android:id/img_product").click()
            sleep(2)
            print("Navigating Up and Down Again for second search item")
            self.Scroll_Down_To_UP()
            sleep(2)
            self.Scroll_Down_To_UP()
            sleep(2)
            self.Scroll_UP_To_Down()
            sleep(2)
            self.Scroll_UP_To_Down()
            
            print("Press Device BackButton")
            lgr_handle.info("Press Back Button")
            for i in range(0,5):
                self.Press_Device_BackButton()
                sleep(0.1)
                i+=1
            lgr_handle.info("Exit: Flipkart")
            print("Exit: Flipkart") 
            print("____________________________________________________________________\n")
            lgr_handle.removeHandler(lgr_handle.handlers[0]) 
                       
                
        except Exception as e:
            print(str(e))
            print(type(e))
            lgr_handle.warn(e)
            lgr_handle.warn("**Test_Bed_Flipkart**")
            print("**Test_Bed_Flipkart**")
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
           
            
