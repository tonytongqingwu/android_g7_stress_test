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


class Test_Bed_Youtube_Download(Common_Utilities):
    def __init__(self):
        pass

    def operate_Youtube(self, dynamic_flag, dynamic_video_play_time):
        youtube_csv_log_path = os.path.join(self.logger_csv_path, "YouTube_Download_log.csv")
        lgr_handle = logger(youtube_csv_log_path, self.config_params.get("debug_level"))
        print("-------------------------------------")
        print("Youtube Application Launched")
        print("-------------------------------------")
        os.system(
            "adb -s " + self.adb_id + " shell am start -n com.google.android.youtube/com.google.android.apps.youtube.app.WatchWhileActivity")
        lgr_handle.info("\n")
        lgr_handle.info("YouTubeMusic App is opened")
        sleep(3)
        try:
            print("Click on Library icon")
            lgr_handle.info("Click on Library icon")
            self.driver.find_element_by_xpath(".//android.widget.TextView[@text='Library']").click()
            sleep(3)
            print("Click on Downloads")
            lgr_handle.info("Click on Downloads")
            self.driver.find_element_by_xpath(".//android.widget.TextView[@text='Downloads']").click()
            sleep(3)
            print("Select first Video")
            lgr_handle.info("Select First Video")
            os.system("adb -s " + self.adb_id + " shell input tap 250 450")
            if dynamic_flag == True:
                timeOut = int(dynamic_video_play_time)
            else:
                timeOut = self.config_params.get("Youtube_Timer")
            lgr_handle.info("Video will Start playing on YouTube for '" + str(timeOut) + "' seconds")
            print("Video will Start playing on YouTube app for '" + str(timeOut) + "' seconds")
            sleep(timeOut)
            self.Press_Device_BackButton()
            sleep(3)
            self.driver.find_element_by_xpath(".//android.widget.TextView[@text='Home']").click()
            lgr_handle.info("Closing the Video")
            print("Closing the Video")
            # lgr_handle.info("Played video on YouTube app for '"+str(timeOut)+"' seconds")
            # print("Played video on YouTube app for '"+str(timeOut)+"' seconds")

            """self.driver.find_element_by_xpath(".//android.widget.ImageView[@content-desc='Close miniplayer']").click()
            #self.driver.find_element_by_id(".com.google.android.youtube:id/floaty_close_button").click()
            sleep(3)
            #Home button of YT
            lgr_handle.info("Clicking Home Button of YouTube app")
            print("Clicking Home Button of YouTube app")
            self.driver.find_element_by_xpath(".//android.widget.Button[@content-desc='Home']").click()
            sleep(3)"""
            print("Exit: Test_Bed_Youtube")
            print("____________________________________________________________________\n")
            lgr_handle.info("Exit: Test_Bed_Youtube")

            for i in range(0, 10):
                os.system("adb -s " + self.adb_id + " shell input keyevent 4")
                sleep(0.1)
                i += 1
            lgr_handle.removeHandler(lgr_handle.handlers[0])

        except Exception as e:
            print(str(e))
            print(type(e))
            lgr_handle.warn(e)
            lgr_handle.warn("**Test_Bed_Youtube**")
            print("**Test_Bed_Youtube**")
            for i in range(0, 10):
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
