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





class Test_Bed_Contacts(Common_Utilities):
    def __init__(self):
        pass


    def open_Contacts(self):
        openContacts_csv_log_path = os.path.join(self.logger_csv_path,"openContacts_log.csv")
        lgr_handle = logger(openContacts_csv_log_path,self.config_params.get("debug_level"))
        print("-------------------------------------")
        print("Open Contacts on Mobile Device")
        print("-------------------------------------")
        sleep(2)
        lgr_handle.info("\n")
        try:
            lgr_handle.info("Open Contacts ")
            print("Open Contacts")
            os.system("adb -s "+self.adb_id+"  shell input keyevent 207")
            sleep(4)
            print("Navigating Up and Down")
            self.Scroll_Down_To_UP()
            sleep(2)
            self.Scroll_UP_To_Down()
            lgr_handle.info("Scroll Up and Down")
            print("Scroll Up and Down")
            lgr_handle.info("Press Home Button")
            print("Press Device Home Button")
            self.Press_Device_Home_Button()
            lgr_handle.info("Exit: openContacts_on_Mobile")
            print("Exit: openContacts_on_Mobile")    
            print("____________________________________________________________________\n")   
            lgr_handle.removeHandler(lgr_handle.handlers[0])
            
        except Exception as e:
            print(str(e))
            print(type(e))
            lgr_handle.warn(e)
            lgr_handle.warn("**Test_Bed_Contacts**")
            print("**Test_Bed_Contacts**")
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
