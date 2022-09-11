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





class Test_Bed_FaceBook(Common_Utilities):
    def __init__(self):
        pass

    def operate_FaceBook(self):
        facebook_csv_log_path = os.path.join(self.logger_csv_path,"FaceBook_log.csv")
        lgr_handle = logger(facebook_csv_log_path,self.config_params.get("debug_level"))
        print("-------------------------------------")
        print("FaceBook App is opened")
        print("-------------------------------------")
        os.system("adb -s "+self.adb_id+" shell am start -n com.facebook.katana/com.facebook.katana.activity.FbMainTabActivity")
        lgr_handle.info("\n")
        lgr_handle.info("FaceBook App is opened")
        sleep(2)
        try:
            #Click on Search 
            print("Click on Search ")
            lgr_handle.info("Click on Search icon")
            self.driver.find_element_by_xpath(".//android.widget.Button[contains(@content-desc,'Search')]").click()
            sleep(2)
            self.driver.find_element_by_xpath(".//android.widget.EditText").clear()
            print("Enter search criteria")
            fb_SearchVal=self.config_params.get("FaceBook_search")
            self.driver.find_element_by_xpath(".//android.widget.EditText").send_keys(fb_SearchVal)
            sleep(5)
            self.Press_Enter_MobileKeyBoard()
            print("Searched value is: '"+fb_SearchVal+"'")
            lgr_handle.info("Searched value is: '"+fb_SearchVal+"'")
            sleep(2)
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
            
            #Click on Posts tab 
            print("Click on Posts Tab on FB")
            lgr_handle.info("Click on Posts Tab on FB")
            self.driver.find_element_by_xpath("//android.view.ViewGroup[contains(@content-desc,'Posts')]").click()
            
            sleep(2)
            print("Navigating Up and Down Again for second search item")
            lgr_handle.info("Navigating Up and Down")
            self.Scroll_Down_To_UP()
            sleep(2)
            self.Scroll_Down_To_UP()
            sleep(2)
            self.Scroll_UP_To_Down()
            sleep(2)
            self.Scroll_UP_To_Down()
            print("Press Device BackButton")
            lgr_handle.info("Press Device BackButton")
            print("Exit: FaceBook")   
            print("____________________________________________________________________\n")            
            lgr_handle.info("Exit: FaceBook")
            
            for i in range(0,6):
                self.Press_Device_BackButton()
                sleep(0.1)
                i+=1
            lgr_handle.removeHandler(lgr_handle.handlers[0])
        except Exception as e:
            print(str(e))
            print(type(e))
            lgr_handle.warn(e)
            print("**Test_Bed_FaceBook**")
            lgr_handle.warn("**Test_Bed_FaceBook**")
            
            for i in range(0,6):
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

            


