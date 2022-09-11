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





class Test_Bed_LaunchGame(Common_Utilities):
    def __init__(self):
        pass


    def launch_Game(self):
        launchGame_csv_log_path = os.path.join(self.logger_csv_path,"launchGame_log.csv")
        lgr_handle = logger(launchGame_csv_log_path,self.config_params.get("debug_level"))
        print("-------------------------------------")
        print("Launch Game")
        print("-------------------------------------")
        
        lgr_handle.info("\n")
        try:
            lgr_handle.info("Launching Game App")
            print("Launching Game App")
            sleep(2)
            os.system("adb -s "+self.adb_id+" shell am start -n com.kiloo.subwaysurf/com.sybogames.chili.multidex.ChiliMultidexSupportActivity")
            sleep(8)
            lgr_handle.info("Press Back Button")
            print("Press Device BackButton")
            for i in range(0,8):
                self.Press_Device_BackButton()
                sleep(0.2)
                i+=1
            self.Press_Device_Home_Button()
            sleep(4)
            os.system("adb -s "+self.adb_id+" shell am start -n com.king.candycrushsaga/com.king.candycrushsaga.CandyCrushSagaActivity")
            sleep(8)
            lgr_handle.info("Press Back Button")
            print("Press Device BackButton")
            for i in range(0,3):
                self.Press_Device_BackButton()
                sleep(0.2)
                i+=1
            self.Press_Device_Home_Button()
            print("Exit: launch_Game")    
            print("____________________________________________________________________\n")   
            lgr_handle.info("Exit: launch_Game") 
            
            lgr_handle.removeHandler(lgr_handle.handlers[0])
            
        except Exception as e:
            print(str(e))
            print(type(e))
            lgr_handle.warn(e)
            lgr_handle.warn("**Test_Bed_LaunchGame**")
            print("**Test_Bed_LaunchGame**")
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
