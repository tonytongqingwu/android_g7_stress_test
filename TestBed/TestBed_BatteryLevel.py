#!/usr/bin/env python3



"""
Modules to be imported for running this script
"""
import sys
# import winsound
from playsound import playsound
sys.path.append('../Common_Utilities/')
from Common_Utilities.Common_Utilities import Common_Utilities
import csv
import os
from time import sleep
sys.path.append('../Logger/')
from Logger.Dexcom_Logger import logger
from appium.webdriver.common.touch_action import TouchAction
# os.system('color')








class TestBed_BatteryLevel (Common_Utilities):
    def __init__(self):
        super().__init__()
        pass



    def battery_Level(self):
        BatteryLevel_csv_log_path = os.path.join(self.logger_csv_path,"BatteryLevel_Log.csv")
        lgr_handle = logger(BatteryLevel_csv_log_path,self.config_params.get("debug_level"))
        print("_________________________")
        print("Get Battery Level")
        print("_________________________")
        batteryLevel=self.getBatteryPercentage()
        lgr_handle.info("Device Battery Level: "+batteryLevel)
        
        # if (batteryLevel<str(70)):
            # print("Low Battery")
            # #frequency = 2500  # in Hz
            # #duration = 10  # in seconds
            # #winsound.Beep(frequency, duration*1000)
            # playsound("beep2.wav")
            # #winsound.MessageBeep(winsound.MB_ICONQUESTION)#
            # try:
                # os.system("adb -s "+self.adb_id+" shell am start -n com.tplink.kasa_android/com.tplink.hellotp.activity.SplashScreenActivity")
                # sleep(4)
                # if (self.driver.find_element_by_xpath("//android.widget.ImageView[contains(@resource-id,'com.tplink.kasa_android:id/device_switch')]").is_displayed()):
                    # self.driver.find_element_by_xpath("//android.widget.ImageView[contains(@resource-id,'com.tplink.kasa_android:id/device_switch')]").click()
                    # sleep(4)
                    # print("Clicked on Smart Plug.....")
            # except Exception as e:
                # print("No Smart Plug Found")
        print("Exit: battery_Level") 
        print("____________________________________________________________________\n")   
        lgr_handle.info("Exit: battery_Level")     
        lgr_handle.removeHandler(lgr_handle.handlers[0])
        
    
