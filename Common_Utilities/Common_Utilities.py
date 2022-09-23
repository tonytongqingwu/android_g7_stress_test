#!/usr/bin/env python3


"""
Modules to be imported for running this script
"""

from appium import webdriver
import os
import sys
import subprocess
import datetime
import base64
# import winsound
from time import sleep

from datetime import datetime
from appium.webdriver.common.touch_action import TouchAction


class Common_Utilities:
    def __init__(self, adb_id, port_num, dexcom_app_type, testbed_scenario, logger_flag, mobile_no):
        self.adb_id = adb_id
        self.port_num = port_num
        self.dexcom_app_type = dexcom_app_type
        self.testbed_scenario = testbed_scenario
        self.mobile_no = mobile_no
        if logger_flag == "All":
            self.logger_flag = 1
        elif logger_flag == "Warn/Error":
            self.logger_flag = 2
        # self.logger_flag = logger_flag
        print("Getting Setup Ready for session to start.... .. .... ......")

        # Common desired capibilties and driver creation
        self.common_desired_cap = {
            "platformName": "Android",
            "udid": self.adb_id,
            "automationName": "UiAutomator2",
            "adbExecTimeout": 60000,
            "appWaitDuration": 60000,
            "uiautomator2ServerLaunchTimeout": 90000,
            "uiautomator2ServerInstallTimeout": 60000,
            "androidInstallTimeout": 180000,
            "disableWindowAnimation": True
        }
        print(self.common_desired_cap)
        print("appium server port number :", self.port_num)
        # self.driver = webdriver.Remote("http://localhost:4723/wd/hub",self.common_desired_cap)
        self.driver = webdriver.Remote("http://localhost:" + self.port_num + "/wd/hub", self.common_desired_cap)
        self.driver.update_settings({
            "waitForIdleTimeout": 3000,  # 3 seconds
        })

        if self.testbed_scenario == "Scenario-1":
            self.Youtube_Timer = 30
            self.Browser_Timer = 30
            self.Music_Timer = 30
            self.Calling_Timer = 20
            self.app_BG_Timer = 30

        elif self.testbed_scenario == "Scenario-2":
            self.Youtube_Timer = 3600
            self.Browser_Timer = 3600
            self.Music_Timer = 3600
            self.Calling_Timer = 3600
            self.app_BG_Timer = 3600

        elif self.testbed_scenario == "Scenario-3":
            self.Youtube_Timer = 1800
            self.Browser_Timer = 1800
            self.Music_Timer = 1800
            self.Calling_Timer = 1800
            self.app_BG_Timer = 1800

        elif self.testbed_scenario == "Scenario-4":
            self.Youtube_Timer = 7200
            self.Browser_Timer = 3600
            self.Music_Timer = 1800
            self.Calling_Timer = 1800
            self.app_BG_Timer = 1800

        elif self.testbed_scenario == "Scenario-5":
            self.Youtube_Timer = 20
            self.Browser_Timer = 10
            self.Music_Timer = 20
            self.Calling_Timer = 18
            self.app_BG_Timer = 5400

        elif self.testbed_scenario == "Scenario-6":
            self.Youtube_Timer = 600
            self.Browser_Timer = 600
            self.Music_Timer = 600
            self.Calling_Timer = 600
            self.app_BG_Timer = 600
        elif self.testbed_scenario == "Scenario-7":
            self.Youtube_Timer = 3600
            self.Browser_Timer = 10
            self.Music_Timer = 10
            self.Calling_Timer = 10
            self.app_BG_Timer = 10
        else:
            self.Youtube_Timer = None
            self.Browser_Timer = None
            self.Music_Timer = None
            self.Calling_Timer = None
            self.app_BG_Timer = None

            # enter the configurable paramters to be used throughout framework
        self.config_params = {
            "debug_level": self.logger_flag,
            "User_Name": "tejashri_debgug",
            "Password": "Dexcom*1212",
            "TX_id": "8NQEPQ",
            "Sensor_code": "7171",
            "Youtube_search": "two hours soulful medidation",
            "Youtube_Timer": self.Youtube_Timer,
            "Browser_URL_1": "www.Dexcom.com",
            "Browser_URL_2": "www.Google.com",
            "Browser_Timer": self.Browser_Timer,
            "Browser_Search": "CGM",
            "Shopping_search_1": "Laptop",
            "Shopping_search_2": "Mobile",
            "Music_Search": "two hours soulful medidation",
            "Music_Timer": self.Music_Timer,
            "MobileNumber": self.mobile_no,
            "Calling_Timer": self.Calling_Timer,
            "FaceBook_search": "Dexcom G7",
            "Instagram_search": "Dexcom G6",
            "app_BG_Timer": self.app_BG_Timer,
            "Teams_CallName": "Godse, Tejashri",
            "BatteryPercentage": "5"
        }

        if ":" in adb_id:
            adb_id_rename = self.adb_id.replace(":", "_")
            self.logger_csv_path = os.path.join(os.getcwd(), "Logs_" + adb_id_rename + "/Test_Bed_Logs")
        else:
            self.logger_csv_path = os.path.join(os.getcwd(), "Logs_" + self.adb_id + "/Test_Bed_Logs")
        if not os.path.exists(self.logger_csv_path):
            os.makedirs(self.logger_csv_path)
            sleep(1)

        if ":" in adb_id:
            adb_id_rename = self.adb_id.replace(":", "_")
            self.logger_HCI_path = os.path.join(os.getcwd(), "Logs_" + adb_id_rename + "/HCI_Logs")
        else:
            self.logger_HCI_path = os.path.join(os.getcwd(), "Logs_" + self.adb_id + "/HCI_Logs")
        if not os.path.exists(self.logger_HCI_path):
            os.makedirs(self.logger_HCI_path)
            sleep(1)

        """self.logger_Screenshot_path = os.path.join(os.getcwd(),"Logs/Screenshots")
        if not os.path.exists(self.logger_Screenshot_path):
            os.makedirs(self.logger_Screenshot_path)
            sleep(1)"""

        """self.logger_VideoRecording_path = os.path.join(os.getcwd(),"Logs/VideoRecording")
        if not os.path.exists(self.logger_VideoRecording_path):
            os.makedirs(self.logger_VideoRecording_path)
            sleep(1)"""

    def server_error_recovery(self):
        print("Server Error Recovery .... .. .... ......")
        os.system("adb -s " + self.adb_id + " uninstall io.appium.uiautomator2.server")
        sleep(2)
        os.system("adb -s " + self.adb_id + " uninstall io.appium.uiautomator2.server.test")
        sleep(2)
        os.system("adb -s " + self.adb_id + " uninstall io.appium.settings")
        sleep(2)
        self.driver = webdriver.Remote("http://localhost:" + self.port_num + "/wd/hub", self.common_desired_cap)

    def Scroll_UP_To_Down(self):
        try:
            touch = TouchAction(self.driver)
            touch.long_press(x=500, y=550).move_to(x=500, y=1300).release().perform()
            sleep(3)
        except Exception as e:
            print(e)
            print("Unable to Scroll up to down")
            for i in range(0, 5):
                self.Press_Device_BackButton()
                sleep(0.1)

    def Scroll_Down_To_UP(self):
        try:
            touch = TouchAction(self.driver)
            touch.long_press(x=500, y=1300).move_to(x=500, y=550).release().perform()
            sleep(3)
        except Exception as e:
            print(e)
            print("Unable to Scroll down to up")
            for i in range(0, 5):
                self.Press_Device_BackButton()
                sleep(0.2)

    def Press_Device_BackButton(self):
        try:
            os.system("adb -s " + self.adb_id + " shell input keyevent 4")
        except Exception as e:
            print(e)
            print("Unable to click on back button")
            for i in range(0, 5):
                self.Press_Device_Home_Button()
                sleep(0.2)

    def Press_Device_Home_Button(self) -> object:
        try:
            os.system("adb -s " + self.adb_id + " shell input keyevent 3")
            print("Pressed Home Button")
        except Exception as e:
            print(e)
            print("Unable to click on back button")
            for i in range(0, 5):
                self.Press_Device_BackButton()
                sleep(0.2)

    def Press_Enter_MobileKeyBoard(self):
        try:
            os.system("adb -s " + self.adb_id + " shell input keyevent KEYCODE_ENTER")
        except Exception as e:
            print(e)
            print("Unable to click on Enter")
            for i in range(0, 5):
                self.Press_Device_BackButton()
                sleep(0.2)

    def makeaCall(self):
        try:
            self.Press_Device_Home_Button()
            os.system(
                "adb -s " + self.adb_id + " shell am start -a android.intent.action.CALL -d tel:'" + self.config_params.get(
                    "MobileNumber") + "'")
            sleep(8)
            try:
                if (self.driver.find_element_by_id("android:id/message").is_displayed()):
                    sleep(4)
                    # self.driver.find_element_by_id("android:id/button1").click()
                    self.driver.find_element_by_xpath(
                        "//android.widget.Button[contains(@resource-id,'button1')]").click()
                    sleep(2)
                    print("\033[95m** Seems there is No SIM Card in Mobile **\033[0m")
                    return False
                    # return 0 end call button : com.android.incallui:id/end_button
            except Exception as e:
                print("Calling on Mobile Number : " + self.mobile_no)
                return True
                # print(self.mobile_no)
                # return 1
        except Exception as e:
            print(e)
            print("Unable to make a call")
            for i in range(0, 5):
                self.Press_Device_BackButton()
                sleep(0.2)

    def sendSMS(self):
        try:
            self.Press_Device_Home_Button()
            sleep(4)
            os.system(
                "adb -s " + self.adb_id + " shell am start -a android.intent.action.SENDTO -d sms:" + self.mobile_no + "  --es  sms_body 'This is TestBed Generated message for testing purpose' --ez exit_on_sent true")
            sleep(4)
            self.driver.find_element_by_xpath("//*[contains(@content-desc,'Send')]").click()
            sleep(5)
            print("SMS Sent")
            self.Press_Device_Home_Button()
        except Exception as e:
            print(e)
            print("Unable to send SMS")
            for i in range(0, 5):
                self.Press_Device_BackButton()
                sleep(0.2)

    def setBatteryPercentage(self):
        try:
            os.system("adb -s " + self.adb_id + " shell dumpsys battery set level '" + self.config_params.get(
                "BatteryPercentage") + "'")
        except Exception as e:
            print(e)
            print("Unable set Battery Percentage")
            for i in range(0, 5):
                self.Press_Device_BackButton()
                sleep(0.2)

    def getBatteryPercentage(self):
        try:
            command = "adb -s " + self.adb_id + " shell dumpsys battery | grep level"
            p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = p.communicate()
            if (stdout != ""):
                batteryLevel = str(stdout).split(":")[1].strip()
                batteryLevel = batteryLevel.replace("b'", "").replace(r"\r\n'", " ")
                if (batteryLevel < str(10)):
                    print("LOW BATTERY")
                    frequency = 257  # in Hz
                    duration = 2  # in seconds
                    for i in range(0, 8):
                        # winsound.Beep(frequency, duration*1000)
                        print('beep')

                    print("\033[31mLOW Battery....Level:", batteryLevel + "\033[0m")
                    return batteryLevel
                print("\033[95mBattery Level:", batteryLevel + "\033[0m")
                return batteryLevel
        except Exception as e:
            print(e)
            print("Unable get Battery Percentage")
            for i in range(0, 5):
                self.Press_Device_BackButton()
                sleep(0.2)

    def endCall(self):
        try:
            os.system("adb -s " + self.adb_id + " shell input keyevent KEYCODE_ENDCALL")
        except Exception as e:
            print(e)
            print("Unable to disconnect a call")
            for i in range(0, 5):
                self.Press_Device_BackButton()
                sleep(0.2)

    def toggle_WiFi(self):
        # self.driver.toggle_wifi()   # adb wifi is needed, so not test it .
        print("wifi toggling")

    def toggle_set_network_connection(self):
        # self.driver.set_network_connection(1)
        print("Airplane toggling ")

    def enable_WiFi(self):
        os.system("adb -s " + self.adb_id + " shell svc wifi enable")
        print("\033[95mWiFi Enabled\033[0m")

    def disable_WiFi(self):
        # os.system("adb -s "+self.adb_id+" shell svc wifi disable")
        print("\033[95mWiFi Disabled\033[0m")

    def enable_AirplaneMode(self):
        # os.system("adb -s "+self.adb_id+" shell settings put global airplane_mode_on 1")
        print("\033[95mAirplane Mode Enabled\033[0m")

    def disable_AirplaneMode(self):
        os.system("adb -s " + self.adb_id + " shell settings put global airplane_mode_on 0")
        print("\033[95mAirplane Mode Disabled\033[0m")

    def enable_Bluetooth(self):
        os.system("adb -s " + self.adb_id + " shell am start -a android.bluetooth.adapter.action.REQUEST_ENABLE")
        sleep(2)
        try:
            self.driver.find_element_by_id("android:id/button1").click()
            print("\033[95mBlueTooth Enabled\033[0m")
        except Exception as e:
            print(e)
            print("Unable to Enable Bluetooth")
            for i in range(0, 5):
                self.Press_Device_BackButton()
                sleep(0.2)
                break

    def disable_Bluetooth(self):
        os.system("adb -s " + self.adb_id + " shell am start -a android.bluetooth.adapter.action.REQUEST_DISABLE")
        sleep(2)
        try:
            self.driver.find_element_by_id("android:id/button1").click()
            print("\033[95mBlueTooth Disabled\033[0m")
        except Exception as e:
            print(e)
            print("Unable to Enable Bluetooth")
            for i in range(0, 5):
                self.Press_Device_BackButton()
                sleep(0.2)
                break

    def runAppinBackgroung(self):
        try:
            self.driver.background_app("app_BG_Timer")
            print("App is in Background, time", self.app_BG_Timer)
        except Exception as e:
            print(e)
            for i in range(0, 5):
                self.Press_Device_BackButton()
                sleep(0.2)

    def Close_RecentApps(self):
        try:
            os.system("adb -s " + self.adb_id + " shell input keyevent KEYCODE_APP_SWITCH")
            sleep(4)
            self.driver.find_element_by_id("com.sec.android.app.launcher:id/clear_all").click()
            sleep(4)
            os.system("adb -s " + self.adb_id + " shell input keyevent KEYCODE_ENTER")
            print("Closed All Recent Opened Apps.")
        except Exception as e:
            print(e)
            for i in range(0, 5):
                self.Press_Device_BackButton()
                sleep(0.2)

    def Generate_HCILogs(self):
        if ":" in self.adb_id:
            adb_id_rename = self.adb_id.replace(":", "_")
            command = "adb -s " + self.adb_id + " bugreport anewbugreportfolder_" + adb_id_rename
        else:
            command = "adb -s " + self.adb_id + " bugreport anewbugreportfolder_" + self.adb_id

        destinationPath = self.logger_HCI_path
        print("\033[92mHCI Logs are getting generated: This process takes few mins .......\033[0m")
        logFolderPath = ""
        p = subprocess.Popen(command, shell=True,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             creationflags=0x00000200)  # creationflags=0x00000200 to ignore keyboard interrupt signal
        stdout, stderr = p.communicate()
        if (stdout != ""):
            logPath = str(stdout).split(":")[0].strip()
            logFolderPath = logPath.replace("b'", "")
        adbPullCommand = "adb -s " + self.adb_id + " pull " + logFolderPath + " " + destinationPath
        os.system(adbPullCommand)
        print("Log file :: " + logFolderPath + " is copied at " + destinationPath)
        sleep(1)
        if ":" in self.adb_id:
            adb_id_rename = self.adb_id.replace(":", "_")
            os.system("del anewbugreportfolder_" + adb_id_rename + ".zip")
        else:
            os.system("del anewbugreportfolder_" + self.adb_id + ".zip")

    def OpenCamera_Capture_Photo(self):
        try:
            os.system("adb -s " + self.adb_id + " shell input keyevent 27")
            sleep(4)

            for i in range(0, 16):
                os.system("adb -s " + self.adb_id + " shell input keyevent 27")

            print("\033[95mCaptured Multiple Photos, Total Captured Photos are \033[0m", i)
        except Exception as e:
            print(e)
            for i in range(0, 2):
                self.Press_Device_Home_Button()
                sleep(0.2)

    def ScreenShot(self, screenName):
        try:
            current_date_and_time = datetime.now()
            time = current_date_and_time.strftime("%Y-%m-%d-%H-%M-%S")
            path = self.logger_Screenshot_path
            filenm = path + '/' + screenName + '_' + time + '.png'
            self.driver.save_screenshot(filenm)
            print("Screenshot generated :" + filenm)
        except Exception as e:
            print(e)
            for i in range(0, 5):
                self.Press_Device_BackButton()
                sleep(0.2)

    def Start_Recording_screen(self):
        self.driver.start_recording_screen()
        print("Video Recoding Started")

    def Stop_Recording_screen(self):
        videoFileRaw = self.driver.stop_recording_screen()
        self.driver.stop_recording_screen()
        current_date_and_time = datetime.now()
        time = current_date_and_time.strftime("%Y-%m-%d-%H-%M-%S")
        path = self.logger_VideoRecording_path
        videofilenm = path + '/Myvideo_' + time + '.mp4'
        videoFile = os.path.join(videofilenm)
        with open(videoFile, "wb") as vd:
            vd.write(base64.b64decode(videoFileRaw))
        print("Video generated :" + videofilenm)

    def Notification_Bar(self):
        try:
            self.driver.open_notifications()
            # Expand adb shell service call statusbar 1
            # Collapse adb shell service call statusbar 2
            print("Opened Notification Bar")
        except Exception as e:
            print(e)
            for i in range(0, 5):
                self.Press_Device_BackButton()
                sleep(0.2)

    def isApp_Installed(self):
        if (self.driver.is_app_installed('com.myntra.android')):
            print("App is Installed")
            print(self.driver.is_app_installed('com.myntra.android'))
            return 1
        else:
            print("App is NOT Installed")
            print(self.driver.is_app_installed('com.myntra.android'))
            return 0

    def Detailed_Memory(self):
        try:
            path = self.logger_MemoryDtls_path
            current_date_and_time = datetime.now()
            time = current_date_and_time.strftime("%Y-%m-%d-%H-%M-%S")
            os.system("adb -s " + self.adb_id + " shell dumpsys meminfo >" + path + "\DetailedMemory_" + time + ".txt")
            print("Detailed_Memory File Generated @ Path : " + path + "/DetailedMemory_" + time + ".txt")
        except Exception as e:
            print(e)
            for i in range(0, 5):
                self.Press_Device_BackButton()
                sleep(0.2)

    def Detailed_Memory_Dexcom(self):
        try:
            path = self.logger_MemoryDtls_path
            current_date_and_time = datetime.now()
            time = current_date_and_time.strftime("%Y-%m-%d-%H-%M-%S")
            os.system(
                "adb -s " + self.adb_id + " shell dumpsys meminfo com.dexcom.g6 >" + path + "\DetailedMemory_G6_" + time + ".txt")
            print("Detailed_Memory_Dexcom File Generated @ Path : " + path + "/DetailedMemory_G6_" + time + ".txt")
        except Exception as e:
            print(e)
            for i in range(0, 5):
                self.Press_Device_BackButton()
                sleep(0.2)

    def Current_Memory(self):
        try:
            path = self.logger_MemoryDtls_path
            current_date_and_time = datetime.now()
            time = current_date_and_time.strftime("%Y-%m-%d-%H-%M-%S")
            os.system(
                "adb -s " + self.adb_id + " shell cat /proc/meminfo > " + path + "\CurrentMemoryUsage_" + time + ".txt")
            print("Current_Memory File Generated @ Path : " + path + "/CurrentMemoryUsage_" + time + ".txt")
        except Exception as e:
            print(e)
            for i in range(0, 5):
                self.Press_Device_BackButton()
                sleep(0.2)

    def List_of_AppsRunning(self):
        try:
            path = self.logger_MemoryDtls_path
            current_date_and_time = datetime.now()
            time = current_date_and_time.strftime("%Y-%m-%d-%H-%M-%S")
            os.system("adb -s " + self.adb_id + " shell ps | grep u0_ > " + path + "\RunningAppsList_" + time + ".txt")
            print(
                "\033[95mList_of_AppsRunning File Generated @ Path : " + path + "/RunningAppsList_" + time + ".txt \033[0m")
        except Exception as e:
            print(e)
            for i in range(0, 5):
                self.Press_Device_BackButton()
                sleep(0.2)

    def Appium_Server_logs(self):
        try:
            path = self.logger_MemoryDtls_path
            current_date_and_time = datetime.now()
            time = current_date_and_time.strftime("%Y-%m-%d-%H-%M-%S")
            cmdlogs = self.driver.get_log('server')
            f = open(path + "/AppiumServerLogs_" + time + ".txt", "a")
            f.writelines(str(cmdlogs))
            f.writelines(str(cmdlogs).replace('[', '[\n'))
            f.close()
            print("Appium Server Logs File Generated @ Path : " + path + "/AppiumServerLogs_" + time + ".txt")
        except Exception as e:
            print(e)
            for i in range(0, 5):
                self.Press_Device_BackButton()
                sleep(0.2)

    def Press_Play_Button(self):
        try:
            os.system("adb -s " + self.adb_id + " shell input keyevent 85")
        except Exception as e:
            print(e)
            print("Unable to click on Play Button")
            for i in range(0, 5):
                self.Press_Device_BackButton()
                sleep(0.2)

    def Press_Stop_Pause_Button(self):
        try:
            os.system("adb -s " + self.adb_id + " shell input keyevent 86")
        except Exception as e:
            print(e)
            print("Unable to click on Stop/Pause Button")
            for i in range(0, 5):
                self.Press_Device_BackButton()
                sleep(0.2)
