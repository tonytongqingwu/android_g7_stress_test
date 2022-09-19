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


class Test_Bed_GoogleMaps(Common_Utilities):
    def __init__(self):
        pass

    def operate_GoogleMaps(self):
        GoogleMaps_csv_log_path = os.path.join(self.logger_csv_path, "GoogleMaps_log.csv")
        lgr_handle = logger(GoogleMaps_csv_log_path, self.config_params.get("debug_level"))
        print("-------------------------------------")
        print("GoogleMaps App is opened")
        print("-------------------------------------")
        os.system(
            "adb -s " + self.adb_id + " shell am start -n  com.google.android.apps.maps/com.google.android.maps.MapsActivity")
        lgr_handle.info("\n")
        lgr_handle.info("GoogleMaps App is opened")
        sleep(4)
        try:

            # Click on 1st tab
            print("Click on First Tab")
            lgr_handle.info("Click on First Tab")
            self.driver.find_element_by_xpath("//android.widget.Button[@index='0']").click()
            sleep(2)
            print("Navigating Up and Down")
            self.Scroll_Down_To_UP()
            self.Scroll_Down_To_UP()
            sleep(2)
            self.Scroll_UP_To_Down()
            self.Scroll_UP_To_Down()
            lgr_handle.info("Press Back Button")
            print("Press Device BackButton")
            for i in range(0, 3):
                self.Press_Device_BackButton()
                sleep(0.2)
                i += 1
            lgr_handle.info("Exit: GoogleMaps")
            print("Exit: GoogleMaps")
            print("____________________________________________________________________\n")
            for i in range(0, 5):
                self.Press_Device_BackButton()
                sleep(0.1)
                i += 1
            lgr_handle.removeHandler(lgr_handle.handlers[0])


        except Exception as e:
            print(str(e))
            print(type(e))
            lgr_handle.warn(e)
            lgr_handle.warn("**Test_Bed_GoogleMaps**")
            print("**Test_Bed_GoogleMaps**")
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
