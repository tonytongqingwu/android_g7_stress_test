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


class TestBed_Services(Common_Utilities):
    def __init__(self):
        super().__init__()
        pass

    def wifi_Enable(self):
        MobileServices_csv_log_path = os.path.join(self.logger_csv_path, "MobileServices_Log.csv")
        lgr_handle = logger(MobileServices_csv_log_path, self.config_params.get("debug_level"))
        print("_________________________")
        print("Enabling Wi-Fi")
        print("_________________________")
        self.enable_WiFi()
        lgr_handle.info("Wi-Fi Enabled")
        sleep(2)
        print("Exit: wifi_Enable")
        print("____________________________________________________________________\n")
        lgr_handle.info("Exit: wifi_Enable")
        lgr_handle.removeHandler(lgr_handle.handlers[0])

    def wifi_Disable(self):
        MobileServices_csv_log_path = os.path.join(self.logger_csv_path, "MobileServices_Log.csv")
        lgr_handle = logger(MobileServices_csv_log_path, self.config_params.get("debug_level"))
        print("_________________________")
        print("Disabling Wi-Fi")
        print("_________________________")
        self.disable_WiFi()
        lgr_handle.info("Wi-Fi Disabled")
        sleep(2)
        print("Exit: wifi_Disable")
        print("____________________________________________________________________\n")
        lgr_handle.info("Exit: wifi_Disable")
        lgr_handle.removeHandler(lgr_handle.handlers[0])

    def airplaneMode_Enable(self):
        MobileServices_csv_log_path = os.path.join(self.logger_csv_path, "MobileServices_Log.csv")
        lgr_handle = logger(MobileServices_csv_log_path, self.config_params.get("debug_level"))
        print("_________________________")
        print("Enabling Airplane Mode")
        print("_________________________")
        self.enable_AirplaneMode()
        lgr_handle.info("Airplane Mode Enabled")
        sleep(2)
        print("Exit: airplaneMode_Enable")
        print("____________________________________________________________________\n")
        lgr_handle.info("Exit: airplaneMode_Enable")
        lgr_handle.removeHandler(lgr_handle.handlers[0])

    def airplaneMode_Disable(self):
        MobileServices_csv_log_path = os.path.join(self.logger_csv_path, "MobileServices_Log.csv")
        lgr_handle = logger(MobileServices_csv_log_path, self.config_params.get("debug_level"))
        print("_________________________")
        print("Disabling Airplane Mode")
        print("_________________________")
        self.disable_AirplaneMode()
        lgr_handle.info("Airplane Mode Disabled")
        sleep(2)
        print("Exit: airplaneMode_Disable")
        print("____________________________________________________________________\n")
        lgr_handle.info("Exit: airplaneMode_Disable")
        lgr_handle.removeHandler(lgr_handle.handlers[0])

    def bluetooth_ON(self):
        MobileServices_csv_log_path = os.path.join(self.logger_csv_path, "MobileServices_Log.csv")
        lgr_handle = logger(MobileServices_csv_log_path, self.config_params.get("debug_level"))
        print("_________________________")
        print("Turning BlueTooth ON")
        print("_________________________")
        self.enable_Bluetooth()
        lgr_handle.info("BlueTooth Enabled")
        sleep(2)
        print("Exit: bluetooth_ON")
        print("____________________________________________________________________\n")
        lgr_handle.info("Exit: bluetooth_ON")
        lgr_handle.removeHandler(lgr_handle.handlers[0])

    def bluetooth_OFF(self):
        MobileServices_csv_log_path = os.path.join(self.logger_csv_path, "MobileServices_Log.csv")
        lgr_handle = logger(MobileServices_csv_log_path, self.config_params.get("debug_level"))
        print("_________________________")
        print("Turning BlueTooth OFF")
        print("_________________________")
        self.disable_Bluetooth()
        lgr_handle.info("BlueTooth Disabled")
        sleep(2)
        print("Exit: bluetooth_OFF")
        print("____________________________________________________________________\n")
        lgr_handle.info("Exit: bluetooth_OFF")
        lgr_handle.removeHandler(lgr_handle.handlers[0])
