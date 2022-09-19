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


class Test_Bed_BLE_G7(Common_Utilities):
    def __init__(self):
        pass

    def launch_BLE_G7(self):

        BLE_G7_csv_log_path = os.path.join(self.logger_csv_path, "BLE_G7_log.csv")
        lgr_handle = logger(BLE_G7_csv_log_path, self.config_params.get("debug_level"))
        print("-------------------------------------")
        print("Launch Test_Bed_BLE_G7")
        print("-------------------------------------")
        lgr_handle.info("\n")
        try:
            lgr_handle.info("Launching BLE_G7 App")
            print("Launching BLE_G7 App")
            sleep(2)
            os.system("adb -s " + self.adb_id + " shell am start -n com.dexcom.g7/com.dexcom.phoenix.ui.SplashActivity")
            sleep(8)
            self.Press_Device_Home_Button()
            lgr_handle.info("Press Home Button")
            print("Press Device Home Button")
            print("Exit: BLE_G7")
            print("____________________________________________________________________\n")
            lgr_handle.info("Exit: BLE_G7")
            lgr_handle.removeHandler(lgr_handle.handlers[0])

        except Exception as e:
            print(str(e))
            print(type(e))
            lgr_handle.warn(e)
            lgr_handle.warn("**Test_Bed_BLE_G7**")
            print("**Test_Bed_BLE_G7**")
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

    def g7_Events_Blood_Glucose(self):
        BLE_G7_csv_log_path = os.path.join(self.logger_csv_path, "BLE_G7_log.csv")
        lgr_handle = logger(BLE_G7_csv_log_path, self.config_params.get("debug_level"))
        os.system("adb -s " + self.adb_id + " shell am start -n com.dexcom.g7/com.dexcom.phoenix.ui.SplashActivity")
        sleep(5)
        print("__________________________________________")
        print("Dexcom G7 App Launched: Events_Blood_Glucose")
        print("__________________________________________")
        lgr_handle.info("Dexcom G7 App Launched: Events_Blood_Glucose")
        sleep(2)

        try:
            print("Click on Events")
            lgr_handle.info("Click on Events")
            self.driver.find_element_by_xpath(".//android.widget.TextView[@text='Events']").click()
            sleep(2)

            # Glucose event
            print("Click on Add Events button")
            lgr_handle.info("Click on Events button")
            self.driver.find_element_by_id("com.dexcom.g7:id/id_events_add_event_button").click()
            sleep(2)

            print("Click on Add Events icon")
            lgr_handle.info("Click on Add Events icon")
            self.driver.find_element_by_id("com.dexcom.g7:id/id_add_event_icon").click()
            sleep(2)

            print("Select Log Blood Glucose")  #
            lgr_handle.info("Select Log Blood Glucose")
            self.driver.find_element_by_id("com.dexcom.g7:id/id_bg_entry_type_log_blood_glucose").click()
            sleep(4)

            # Enter a BG meter value between 1.1 and 33.3 mmol/L.
            bloodGlucose = "20"
            self.driver.find_element_by_xpath(".//android.widget.EditText").send_keys(
                bloodGlucose)  # com.dexcom.g7:id/id_bg_meter_value_edit_text
            print("Blood Glucose Value entered", bloodGlucose)
            lgr_handle.info("Blood Glucose Value entered")
            sleep(4)
            self.driver.find_element_by_xpath(
                "//android.widget.Button[@text='Save']").click()  # com.dexcom.g7:id/id_bg_save_button
            sleep(4)
            self.driver.find_element_by_xpath(
                "//android.widget.Button[@text='Confirm']").click()  # com.dexcom.g7:id/id_confirmation_confirm_button
            sleep(4)
            print("Press Save-Confirm Button")
            lgr_handle.info("Press Save-Confirm Button")
            self.driver.find_element_by_xpath(".//android.widget.TextView[@text='Events']").click()
            sleep(1)

            # Glucose event
            print("Click on Add Events button")
            lgr_handle.info("Click on Events button")
            self.driver.find_element_by_id("com.dexcom.g7:id/id_events_add_event_button").click()
            sleep(2)

            print("Click on Add Events icon")
            lgr_handle.info("Click on Add Events icon")
            self.driver.find_element_by_id("com.dexcom.g7:id/id_add_event_icon").click()
            sleep(2)

            print("Select Log Blood Glucose")  #
            lgr_handle.info("Select Log Blood Glucose")
            self.driver.find_element_by_id("com.dexcom.g7:id/id_bg_entry_type_log_blood_glucose").click()
            sleep(4)

            # Enter a BG meter value between 1.1 and 33.3 mmol/L.
            bloodGlucose = "2"
            self.driver.find_element_by_xpath(".//android.widget.EditText").send_keys(
                bloodGlucose)  # com.dexcom.g7:id/id_bg_meter_value_edit_text
            print("Blood Glucose Value entered", bloodGlucose)
            lgr_handle.info("Blood Glucose Value entered")
            sleep(4)
            self.driver.find_element_by_xpath(
                "//android.widget.Button[@text='Save']").click()  # com.dexcom.g7:id/id_bg_save_button
            sleep(4)
            self.driver.find_element_by_xpath(
                "//android.widget.Button[@text='Confirm']").click()  # com.dexcom.g7:id/id_confirmation_confirm_button
            sleep(4)
            print("Press Save-Confirm Button")
            lgr_handle.info("Press Save-Confirm Button")
            self.driver.find_element_by_xpath(".//android.widget.TextView[@text='Events']").click()
            sleep(1)

            lgr_handle.info("Press Home Button")
            print("Press Device Home Button")
            self.Press_Device_Home_Button()
            print("Added Events_Blood_Glucose")
            lgr_handle.info("Added Events_Blood_Glucose")
            print("__________________________________________")
            lgr_handle.removeHandler(lgr_handle.handlers[0])

        except Exception as e:
            print(str(e))
            print(type(e))
            lgr_handle.warn(e)
            lgr_handle.warn("**Events_Carbs**")
            print("**Events_Carbs**")
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

    def g7_delete_Event_Type(self):
        BLE_G7_csv_log_path = os.path.join(self.logger_csv_path, "BLE_G7_log.csv")
        lgr_handle = logger(BLE_G7_csv_log_path, self.config_params.get("debug_level"))
        os.system("adb -s " + self.adb_id + " shell am start -n com.dexcom.g7/com.dexcom.phoenix.ui.SplashActivity")
        sleep(5)
        print("__________________________________________")
        print("Dexcom G7 App Launched: Delete_Events")
        print("__________________________________________")
        lgr_handle.info("Dexcom G7 App Launched : Delete_Events")
        sleep(5)

        try:
            print("Click on Events")
            lgr_handle.info("Click on Events")
            self.driver.find_element_by_xpath(".//android.widget.TextView[@text='Events']").click()
            sleep(8)
            try:
                i = 0
                while True:
                    print("Select and Delete Events")
                    lgr_handle.info("Select and Delete Events")
                    Select_item = self.driver.find_element_by_id("com.dexcom.g7:id/id_event_title")
                    Select_item.click()
                    sleep(2)
                    i += 1
                    print("Click DELETE EVENT")
                    lgr_handle.info("Click DELETE EVENT")
                    self.driver.find_element_by_id("com.dexcom.g7:id/id_event_delete_text").click()
                    sleep(8)
                    print("Confirm DELETE EVENT")
                    lgr_handle.info("Confirm DELETE EVENT")
                    self.driver.find_element_by_xpath(".//android.widget.Button[contains(@text,'DELETE')]").click()
                    print("Deleted Event: " + str(i))
                    lgr_handle.info("Deleted Event: " + str(i))
            except Exception as e:
                # print(e)
                pass
                self.driver.find_element_by_xpath(".//android.widget.TextView[@text='Events']").click()
                sleep(2)
                print("No Events to Delete")
                lgr_handle.info("No Events to Delete")
                self.Press_Device_Home_Button()
            lgr_handle.removeHandler(lgr_handle.handlers[0])
        except Exception as e:
            print(str(e))
            print(type(e))
            lgr_handle.warn(e)
            lgr_handle.warn("**Delete_Events**")
            print("**Delete_Events**")
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

    def g7_settings_alerts(self):
        BLE_G7_csv_log_path = os.path.join(self.logger_csv_path, "BLE_G7_log.csv")
        lgr_handle = logger(BLE_G7_csv_log_path, self.config_params.get("debug_level"))
        os.system("adb -s " + self.adb_id + " shell am start -n com.dexcom.g7/com.dexcom.phoenix.ui.SplashActivity")
        sleep(5)
        print("__________________________________________")
        print("Dexcom G7 App Launched: Settings-->Alerts")
        print("__________________________________________")
        lgr_handle.info("Dexcom App G7 Launched: Settings-->Alerts")
        try:
            print("Click on Settings")
            lgr_handle.info("Click on Settings")
            sleep(2)
            self.driver.find_element_by_xpath(".//android.widget.TextView[@text='Settings']").click()
            sleep(2)
            print("Click on Alerts")
            lgr_handle.info("Click on Alerts")
            self.driver.find_element_by_id("com.dexcom.g7:id/id_settings_alerts_icon").click()

            # steps to select Urgent Low Soon alerts.
            print("__________________________________________")
            print("Alerts: Urgent Low Soon")
            print("__________________________________________")
            lgr_handle.info("Alerts: Urgent Low Soon")
            sleep(2)
            self.driver.find_element_by_id("com.dexcom.g7:id/id_settings_alerts_urgent_low_soon_title_label").click()
            sleep(2)
            self.driver.find_element_by_id("com.dexcom.g7:id/id_settings_urgent_low_soon_alert_switch").click()
            sleep(2)
            self.Press_Device_BackButton()

            # steps to select Low alerts.
            sleep(2)
            print("__________________________________________")
            print("Alerts: Low")
            print("__________________________________________")
            lgr_handle.info("Alerts: Low")
            self.driver.find_element_by_id("com.dexcom.g7:id/id_settings_alerts_low_title_label").click()
            sleep(2)
            # Select Level
            self.driver.find_element_by_id("com.dexcom.g7:id/id_settings_alert_level_title_label").click()
            sleep(2)

            lowVal = "4.0"
            self.driver.find_element_by_android_uiautomator("new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView\
    (new UiSelector().textContains(\"" + lowVal + "\").instance(0))").click()
            print("mmol/L Value selected : " + lowVal)
            lgr_handle.info("mmol/L Value selected : " + lowVal)
            sleep(2)
            self.driver.find_element_by_xpath("//android.widget.Button[@text='SAVE']").click()
            sleep(2)
            self.Press_Device_BackButton()

            # steps to select High alerts.
            sleep(2)
            print("__________________________________________")
            print("Alerts: High")
            print("__________________________________________")
            lgr_handle.info("Alerts: High")
            self.driver.find_element_by_id("com.dexcom.g7:id/id_settings_alerts_high_title_label").click()
            sleep(2)
            # Select Level
            self.driver.find_element_by_id("com.dexcom.g7:id/id_settings_alert_level_title_label").click()
            sleep(2)

            highVal = "10.0"
            self.driver.find_element_by_android_uiautomator("new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView\
    (new UiSelector().textContains(\"" + highVal + "\").instance(0))").click()
            print("mmol/LValue selected : " + highVal)
            lgr_handle.info("mmol/LValue selected : " + highVal)
            sleep(2)
            self.driver.find_element_by_xpath("//android.widget.Button[@text='SAVE']").click()
            sleep(2)
            self.Press_Device_BackButton()

            # steps to select Rising Fast alerts.
            sleep(2)
            print("__________________________________________")
            print("Alerts: Rising Fast")
            print("__________________________________________")
            lgr_handle.info("Alerts: Rising Fast")
            self.driver.find_element_by_id("com.dexcom.g7:id/id_settings_alerts_rising_fast_title_label").click()
            sleep(2)
            toggle_Switch = self.driver.find_element_by_xpath("//android.widget.Switch").text
            if toggle_Switch == "Off":
                self.driver.find_element_by_xpath("//android.widget.Switch").click()
                sleep(2)
                print("Toggling is turned ON")
            # Select Level
            self.driver.find_element_by_id("com.dexcom.g7:id/id_settings_rising_falling_alert_level_text").click()
            sleep(2)

            riseFastVal = "2.2"
            self.driver.find_element_by_android_uiautomator(
                "new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains(\"" + riseFastVal + "\").instance(0))").click()
            print("mmol/L Value selected : " + riseFastVal)
            lgr_handle.info("mmol/LValue selected : " + riseFastVal)
            sleep(2)
            self.driver.find_element_by_xpath("//android.widget.Button[@text='SAVE']").click()
            sleep(2)
            self.Press_Device_BackButton()

            # steps to select Falling Fast alerts.
            sleep(2)
            print("__________________________________________")
            print("Alerts: Falling Fast")
            print("__________________________________________")
            lgr_handle.info("Alerts: Falling Fast")
            self.driver.find_element_by_id("com.dexcom.g7:id/id_settings_alerts_falling_fast_title_label").click()
            sleep(2)
            toggle_Switch = self.driver.find_element_by_xpath("//android.widget.Switch").text
            if toggle_Switch == "Off":
                self.driver.find_element_by_xpath("//android.widget.Switch").click()
                sleep(2)
                print("Toggling is turned ON")
                # Select Level
            self.driver.find_element_by_id("com.dexcom.g7:id/id_settings_rising_falling_alert_level_text").click()
            sleep(2)

            fallRateVal = "5.2"
            self.driver.find_element_by_android_uiautomator(
                "new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains(\"" + fallRateVal + "\").instance(0))").click()
            print("mmol/L Value selected : " + fallRateVal)
            lgr_handle.info("mmol/LValue selected : " + fallRateVal)
            sleep(2)
            self.driver.find_element_by_xpath("//android.widget.Button[@text='SAVE']").click()
            sleep(2)
            self.Press_Device_BackButton()

            # steps to select Reset Alert Settings.
            sleep(5)
            print("Alerts: Reset Alert Settings")
            lgr_handle.info("Alerts: Reset Alert Settings")
            sleep(2)
            # Bottom to Top swipe
            print("Scrolling down")
            self.Scroll_Down_To_UP()
            sleep(2)
            self.Scroll_Down_To_UP()
            sleep(2)
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='Reset Alert Settings']").click()
            sleep(2)
            self.driver.find_element_by_xpath("//android.widget.Button[@text='CONFIRM']").click()
            sleep(2)
            lgr_handle.info("Dexcom App: Settings Alerts completed")
            print("Dexcom App: Settings Alerts completed")
            self.Press_Device_BackButton()
            sleep(0.1)
            self.driver.find_element_by_xpath(".//android.widget.TextView[@text='Glucose']").click()
            lgr_handle.info("Dexcom Main Page")
            print("__________________________________________")
            lgr_handle.removeHandler(lgr_handle.handlers[0])

        except Exception as e:
            print(str(e))
            print(type(e))
            lgr_handle.warn(e)
            lgr_handle.warn("**Settings-->Alerts**")
            print("**Settings-->Alerts**")
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
