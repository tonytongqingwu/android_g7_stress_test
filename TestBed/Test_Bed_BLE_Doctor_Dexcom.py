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



class Test_Bed_BLE_Doctor_Dexcom(Common_Utilities):
    def __init__(self):
        pass


    def launch_BLE_Doctor_Dexcom(self):
        BLE_Doctor_csv_log_path = os.path.join(self.logger_csv_path,"BLE_Doctor_Dexcom_log.csv")
        lgr_handle = logger(BLE_Doctor_csv_log_path,self.config_params.get("debug_level"))
        print("-------------------------------------")
        print("Launch Test_Bed_BLE_Doctor")
        print("-------------------------------------")
        lgr_handle.info("\n")
        try:
            lgr_handle.info("Launching BLE_Doctor App")
            print("Launching BLE_Doctor App")
            sleep(2)
            os.system("adb -s "+self.adb_id+" shell am start -n com.dexcom.exg0718.BLEDoctor/com.dexcom.exg0718.BLEDoctor.MainActivity")
            sleep(8)
            self.Press_Device_Home_Button()
            lgr_handle.info("Press Home Button")
            print("Press Device Home Button")
            print("Exit: BLE_Doctor_Dexcom")    
            print("____________________________________________________________________\n")   
            lgr_handle.info("Exit: BLE_Doctor_Dexcom") 
            lgr_handle.removeHandler(lgr_handle.handlers[0])
            
        except Exception as e:
            print(str(e))
            print(type(e))
            lgr_handle.warn(e)
            lgr_handle.warn("**Test_Bed_BLE_Doctor_Dexcom**")
            print("**Test_Bed_BLE_Doctor_Dexcom**")
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
