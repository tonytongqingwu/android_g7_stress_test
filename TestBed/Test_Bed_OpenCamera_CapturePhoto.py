#!/usr/bin/env python3


"""
Modules to be imported for running this script
"""
import sys

from selenium.webdriver import ActionChains

sys.path.append('../Common_Utilities/')
from Common_Utilities.Common_Utilities import Common_Utilities
import csv
import os
import datetime
import base64

from time import sleep
from datetime import datetime
from appium.webdriver.common.touch_action import TouchAction

sys.path.append('../Logger/')
from Logger.Dexcom_Logger import logger

# os.system('color')


class Test_Bed_OpenCamera_CapturePhoto(Common_Utilities):
    def __init__(self):
        pass

    def operate_Camera(self):

        openCamera_csv_log_path = os.path.join(self.logger_csv_path, "openCamera_log.csv")
        lgr_handle = logger(openCamera_csv_log_path, self.config_params.get("debug_level"))
        print("-------------------------------------")
        print("Opening Camera Capture Photo")
        print("-------------------------------------")
        sleep(2)
        lgr_handle.info("\n")
        try:
            lgr_handle.info("Open Camera capture photo")
            # self.driver.start_recording_screen()
            print("Open Camera capture photo")
            self.OpenCamera_Capture_Photo()
            sleep(2)
            # self.ScreenShort()
            self.Press_Device_Home_Button()
            print("Exit: Open_Camera")
            print("____________________________________________________________________\n")
            lgr_handle.info("Exit: Open_Camera")
            lgr_handle.removeHandler(lgr_handle.handlers[0])

            # opens camera app
            # os.system("adb -s "+self.adb_id+" shell am start -n com.sec.android.app.camera/com.sec.android.app.camera.Camera")
            # or
            # os.system("adb -s "+self.adb_id+" shell am start -a android.media.action.STILL_IMAGE_CAMERA --ei android.intent.extras.CAMERA_FACING 0")
            # sleep(4)
            # Captures photo after camera is opened
            # os.system("adb -s "+self.adb_id+"  shell input keyevent KEYCODE_CAMERA")


        except Exception as e:
            print(str(e))
            print(type(e))
            lgr_handle.warn(e)
            lgr_handle.warn("**Test_Bed_OpenCamera_CapturePhoto**")
            print("**Test_Bed_OpenCamera_CapturePhoto**")
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

    def openCamera_Capture_BurstPhoto(self):
        openCamera_csv_log_path = os.path.join(self.logger_csv_path, "openCamera_log.csv")
        lgr_handle = logger(openCamera_csv_log_path, self.config_params.get("debug_level"))
        print("-------------------------------------")
        print("OpenCamera_Capture_BurstPhoto")
        print("-------------------------------------")
        sleep(2)
        lgr_handle.info("\n")
        try:
            os.system("adb -s " + self.adb_id + " shell input keyevent 27")
            sleep(2)
            #os.system("adb -s "+self.adb_id+" shell input swipe 550 1920 550 2000")
            #e = self.driver.find_element_by_xpath("//*[contains(@content-desc,'Take picture') or contains(@text,'Take picture')]")
            # for i in range(0,4):
                # t = TouchAction(self.driver)
                # t.press(x=540,y=1920)
                # t.move_to(x=540,y=2000)
                # #t.wait(10000)
                # t.release()
                # t.perform()
            devicesize= self.driver.get_window_size()

            print("Device Width and Height : ", devicesize)
            screenWidth = devicesize['width']
            screenHeight = devicesize['height']
            print("Width : ", screenWidth)
            print("Height : ", screenHeight)
            startx = screenWidth/2
            endx = screenWidth/2
            starty = screenHeight*0.98
            endy = screenHeight*0.93
            print("sX : ", startx)
            print("eY : ", endx)
            print("sX : ", starty)
            print("eY : ", endy)
            t = TouchAction(self.driver)
            t.press(startx, starty).move_to(endx, endy).wait(10000).release().perform()

            # starty = (int)(size.height * 0.70);
            # endy = (int)(size.height * 0.20);
            # startx = size.width / 2;

            #self.driver.swipe(start_x=550, start_y=1930, end_x=550, end_y=2090, duration=2000)
            self.Press_Device_Home_Button()
            print("Exit: Open_Camera")
            print("____________________________________________________________________\n")
            lgr_handle.info("Exit: Open_Camera")
            lgr_handle.removeHandler(lgr_handle.handlers[0])

        except Exception as e:
            print(str(e))
            print(type(e))
            lgr_handle.warn(e)
            lgr_handle.warn("**Test_Bed_OpenCamera_CapturePhoto**")
            print("**Test_Bed_OpenCamera_CapturePhoto**")
            for i in range(0, 5):
                self.Press_Device_BackButton()
                sleep(0.2)
                
            if "A session is either terminated or not started" in str(e):
                self.server_error_recovery()
            if "An unknown server-side error" in str(e):
                self.driver.quit()
                sleep(2)
                self.server_error_recovery()
            lgr_handle.removeHandler(lgr_handle.handlers[0])