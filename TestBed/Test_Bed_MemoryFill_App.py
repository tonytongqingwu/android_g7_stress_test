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


class Test_Bed_MemoryFill_App(Common_Utilities):
    def __init__(self):
        pass

    def operate_MemoryFill_App(self):
        MemoryFill_App_csv_log_path = os.path.join(self.logger_csv_path, "MemoryFill_App_log.csv")
        lgr_handle = logger(MemoryFill_App_csv_log_path, self.config_params.get("debug_level"))
        print("-------------------------------------")
        print("Memory Fill App is opened")
        print("-------------------------------------")
        os.system(
            "adb -s " + self.adb_id + " shell am start -n com.rektgames.memoryfill/com.rektgames.memoryfill.Views.TabbedActivity")
        lgr_handle.info("\n")
        lgr_handle.info("Simple_MemoryAll App is opened")
        sleep(4)
        try:
            # Wait until progress bar id full #res id : com.rektgames.memoryfill:id/progressText, txt:25%,class:android.widget.TextView,pkg:com.rektgames.memoryfill
            print("Click on ++100MB Button")
            lgr_handle.info("Click on ++100MB Button")
            for i in range(0, 8):
                self.driver.find_element_by_id("com.rektgames.memoryfill:id/more").click()
                sleep(0.1)
                i += 1
            sleep(10)

            print("Click on Fill Button")
            lgr_handle.info("Click on Fill Button")
            for i in range(0, 8):
                self.driver.find_element_by_id("com.rektgames.memoryfill:id/allocate").click()
                sleep(0.1)
                i += 1
            sleep(10)

            # print("Click on Free UP Button")
            # lgr_handle.info("Click on Free UP Button")
            # self.driver.find_element_by_id("com.rektgames.memoryfill:id/deallocate").click()
            # for i in range(0,50):
            # self.driver.find_element_by_id("com.rektgames.memoryfill:id/allocate").click()
            # sleep(0.1)
            # i+=1
            # sleep(10)

            print("Press Device BackButton")
            self.Press_Device_BackButton()
            lgr_handle.info("Exit: MemoryFill_App")
            print("Exit: MemoryFill_App")
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
            lgr_handle.warn("**Test_Bed_MemoryFill_App**")
            print("**Test_Bed_MemoryFill_App**")
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
