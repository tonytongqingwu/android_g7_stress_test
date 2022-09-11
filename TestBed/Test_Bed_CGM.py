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








class Test_Bed_CGM(Common_Utilities):
    def __init__(self):
        super().__init__()
        pass



    def launch_dexcom_app(self):
        dexcomapp_csv_log_path = os.path.join(self.logger_csv_path,"DexcomApp_log.csv")
        lgr_handle = logger(dexcomapp_csv_log_path,self.config_params.get("debug_level"))
        print("_________________________")
        print("Lauching Dexcom App")
        print("_________________________")
        os.system("adb -s "+self.adb_id+" shell am start -n com.dexcom.g6/com.dexcom.cgm.activities.AppCompatabilityActivity")
        sleep(10)
        lgr_handle.info("Dexcom App is Launched")
        try:
            if (self.driver.find_element_by_id("android:id/alertTitle").is_displayed()):
                #print("Log In Again Window popped up, Handled it")
                self.driver.find_element_by_id("android:id/button2").click()
                sleep(8)
                self.Press_Device_Home_Button()
        except Exception as e:
            print(" ")
        lgr_handle.removeHandler(lgr_handle.handlers[0])
        
   
    def settings_alerts(self):
        dexcomApp_csv_log_path = os.path.join(self.logger_csv_path,"dexcomApp_log.csv")
        lgr_handle = logger(dexcomApp_csv_log_path,self.config_params.get("debug_level"))
        os.system("adb -s "+self.adb_id+" shell am start -n com.dexcom.g6/com.dexcom.cgm.activities.AppCompatabilityActivity")
        sleep(10)
        try:
            if (self.driver.find_element_by_id("android:id/alertTitle").is_displayed()):
                print("Log In Again Window popped up, Handled it")
                self.driver.find_element_by_id("android:id/button2").click()
                sleep(4)
        except Exception as e:
            print("NO Log In Again Window popped up")
        print("__________________________________________")
        print("Dexcom App Launched: Settings-->Alerts")
        print("__________________________________________")
        lgr_handle.info("Dexcom App Launched: Settings-->Alerts")
        try:
            print("Click on Settings")
            lgr_handle.info("Click on Settings")
            sleep(2)	
            self.driver.find_element_by_xpath(".//android.widget.TextView[@text='SETTINGS']").click()
            sleep(2)	
            print("Click on Alerts")
            lgr_handle.info("Click on Alerts")
            self.driver.find_element_by_xpath("//android.widget.LinearLayout[contains(@resource-id,'id_settings_alerts')]").click()

            #steps to select Urgent Low Soon alerts.
            print("Alerts: Urgent Low Soon")
            lgr_handle.info("Alerts: Urgent Low Soon")
            sleep(2)
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='Urgent Low Soon']").click()
            sleep(2)	
            self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'Repeat')]").click()
            sleep(2)				
            
            urgentLowsoonVal="15"
            self.driver.find_element_by_android_uiautomator("new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView\
    (new UiSelector().textMatches(\""+urgentLowsoonVal+"\").instance(0))").click()
            print("UrgentLow Value selected : "+urgentLowsoonVal)
            lgr_handle.info("UrgentLow Value selected : "+urgentLowsoonVal)
            sleep(2)	            
            print("Click on Save")
            lgr_handle.info("Click on Save")
            self.driver.find_element_by_xpath("//android.widget.Button[@text='SAVE']").click()
            sleep(2)	
            self.Press_Device_BackButton()

            #steps to select Low alerts.
            sleep(2)	
            print("Alerts: Low")
            lgr_handle.info("Alerts: Low")
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='Low']").click()
            sleep(2)	
            self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'Notify Me')]").click()
            sleep(2)			
            
            lowVal="95"
            self.driver.find_element_by_android_uiautomator("new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView\
    (new UiSelector().textMatches(\""+lowVal+"\").instance(0))").click()
            print("mg/dL Value selected : "+lowVal)
            lgr_handle.info("mg/dL Value selected : "+lowVal)
            sleep(2)
            self.driver.find_element_by_xpath("//android.widget.Button[@text='SAVE']").click()
            sleep(2)	
            self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'Repeat')]").click()
            
            lowValR="15"
            self.driver.find_element_by_android_uiautomator("new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView\
    (new UiSelector().textMatches(\""+lowValR+"\").instance(0))").click()
            print("Repeat Value selected : "+lowValR)
            lgr_handle.info("Repeat Value selected : "+lowValR)        
            sleep(2)            
            self.driver.find_element_by_xpath("//android.widget.Button[@text='SAVE']").click()
            sleep(2)	
            self.Press_Device_BackButton()

            #steps to select High alerts.
            sleep(2)	
            print("Alerts: High")
            lgr_handle.info("Alerts: High")
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='High']").click()
            sleep(2)	
            self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'Notify Me')]").click()

            highVal="270"
            self.driver.find_element_by_android_uiautomator("new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView\
    (new UiSelector().textMatches(\""+highVal+"\").instance(0))").click()
            print("mg/dL Value selected : "+highVal)
            lgr_handle.info("mg/dL Value selected : "+highVal)
            sleep(2)
            self.driver.find_element_by_xpath("//android.widget.Button[@text='SAVE']").click()
            sleep(2)	
            self.Press_Device_BackButton()

            #steps to select Rise Rate alerts.
            sleep(2)	
            print("Alerts: RiseRate")
            lgr_handle.info("Alerts: RiseRate")
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='Rise Rate']").click()
            sleep(2)	
            self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'Notify Me')]").click()
            sleep(2)	
            
            riseRateVal="3"
            self.driver.find_element_by_android_uiautomator("new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textMatches(\""+riseRateVal+"\").instance(0))").click()
            print("mg/dL/min Value selected : "+riseRateVal)
            lgr_handle.info("mg/dL Value selected : "+riseRateVal)
            sleep(2)				
            self.driver.find_element_by_xpath("//android.widget.Button[@text='SAVE']").click()
            sleep(2)	
            self.Press_Device_BackButton()

            #steps to select Fall Rate alerts.
            sleep(2)	
            print("Alerts: FallRate")
            lgr_handle.info("Alerts: FallRate")
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='Fall Rate']").click()
            sleep(2)	
            self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'Notify Me')]").click()
            sleep(2)	
            
            fallRateVal="3"
            self.driver.find_element_by_android_uiautomator("new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textMatches(\""+fallRateVal+"\").instance(0))").click()
            print("mg/dL/min Value selected : "+fallRateVal)
            lgr_handle.info("mg/dL Value selected : "+fallRateVal)
            sleep(2)				
            self.driver.find_element_by_xpath("//android.widget.Button[@text='SAVE']").click()
            sleep(2)	
            self.Press_Device_BackButton()

            #steps to select Reset Alert Settings.
            sleep(5)
            print("Alerts: Reset Alert Settings")
            lgr_handle.info("Alerts: Reset Alert Settings")
            sleep(2)	
            #Bottom to Top swipe
            print("Scrolling down")
            self.Scroll_Down_To_UP()
            sleep(2)
            self.Scroll_Down_To_UP()
            sleep(2)	
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='Reset Alert Settings']").click()
            sleep(2)	
            self.driver.find_element_by_xpath("//android.widget.Button[@text='RESET ALERT SETTINGS']").click()
            sleep(2)	
            lgr_handle.info("Dexcom App: Settings Alerts completed")
            print("Dexcom App: Settings Alerts completed")
            self.Press_Device_BackButton()
            sleep(0.1)
            self.Press_Device_BackButton()
            lgr_handle.info("Dexcom Main Page")
            print("__________________________________________")
            lgr_handle.removeHandler(lgr_handle.handlers[0])
            
        except Exception as e: 
            print(str(e))
            print(type(e))
            lgr_handle.warn(e)
            lgr_handle.warn("**Settings-->Alerts**")
            print("**Settings-->Alerts**")
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
            

    def g6_Events_Exercise(self):
        dexcomApp_csv_log_path = os.path.join(self.logger_csv_path,"dexcomApp_log.csv")
        lgr_handle = logger(dexcomApp_csv_log_path,self.config_params.get("debug_level"))
        os.system("adb -s "+self.adb_id+" shell am start -n com.dexcom.g6/com.dexcom.cgm.activities.AppCompatabilityActivity")
        sleep(10)
        try:
            if (self.driver.find_element_by_id("android:id/alertTitle").is_displayed()):
                print("Log In Again Window popped up, Handled it")
                self.driver.find_element_by_id("android:id/button2").click()
                sleep(4)
        except Exception as e:
            print("NO Log In Again Window popped up")
        print("__________________________________________")
        print("Dexcom App Launched: Events_Exercise")
        print("__________________________________________")
        lgr_handle.info("Dexcom App : Events_Exercise")
        sleep(5)
        
        try:
            print("Click on Events")
            lgr_handle.info("Click on Events")
            self.driver.find_element_by_xpath(".//android.widget.TextView[@text='Events']").click()
            sleep(4)
            print("Click on Add Events")
            lgr_handle.info("Click on Events")
            self.driver.find_element_by_xpath(".//android.widget.TextView[@content-desc='Add Event']").click()
            sleep(4)
            print("Select Exercise Option")
            lgr_handle.info("Select Exercise Option")
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='Exercise']").click()
            sleep(4)
            
            print("Select Exercise Intensity")
            lgr_handle.info("Select Exercise Intensity")
            
            light= self.driver.find_element_by_xpath("//android.widget.RadioButton[@text='Light']")
            light.click()
            sleep(3)
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='ADD']").click()
            sleep(5)
            self.driver.find_element_by_xpath("//android.widget.Button[@text='CONFIRM']").click()
            sleep(5)
            print("Added Exercise: Light")
            lgr_handle.info("Added Exercise: Light")
            
            #Adding Medium Intensity
            self.driver.find_element_by_xpath(".//android.widget.TextView[@content-desc='Add Event']").click()
            sleep(5)
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='Exercise']").click()
            sleep(5)
            medium= self.driver.find_element_by_xpath("//android.widget.RadioButton[@text='Medium']")
            medium.click()
            sleep(3)
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='ADD']").click()
            sleep(5)
            self.driver.find_element_by_xpath("//android.widget.Button[@text='CONFIRM']").click()
            sleep(5)
            print("Added Exercise: Medium")
            lgr_handle.info("Added Exercise: Medium")

            #Adding High Intensity
            self.driver.find_element_by_xpath(".//android.widget.TextView[@content-desc='Add Event']").click()
            sleep(5)
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='Exercise']").click()
            sleep(5)
            heavy= self.driver.find_element_by_xpath("//android.widget.RadioButton[@text='Heavy']")
            heavy.click()
            sleep(3)
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='ADD']").click()
            sleep(5)
            self.driver.find_element_by_xpath("//android.widget.Button[@text='CONFIRM']").click()
            sleep(5)
            print("Added Exercise: Heavy")
            lgr_handle.info("Added Exercise: Heavy")

            print("Press Back Button")
            lgr_handle.info("Press Back Button")
            self.Press_Device_BackButton()
            print("Added Dexcom_Events_Exercise")
            lgr_handle.info("Added Dexcom_Events_Exercise")
            print("__________________________________________")
            lgr_handle.removeHandler(lgr_handle.handlers[0])
            
        except Exception as e: 
            print(str(e))
            print(type(e))
            lgr_handle.warn(e)
            lgr_handle.warn("**Dexcom_Events_Exercise**")
            print("**Dexcom_Events_Exercise**")
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
    
    def g6_Events_Health(self):
        dexcomApp_csv_log_path = os.path.join(self.logger_csv_path,"dexcomApp_log.csv")
        lgr_handle = logger(dexcomApp_csv_log_path,self.config_params.get("debug_level"))
        os.system("adb -s "+self.adb_id+" shell am start -n com.dexcom.g6/com.dexcom.cgm.activities.AppCompatabilityActivity")
        sleep(10)
        try:
            if (self.driver.find_element_by_id("android:id/alertTitle").is_displayed()):
                print("Log In Again Window popped up, Handled it")
                self.driver.find_element_by_id("android:id/button2").click()
                sleep(4)
        except Exception as e:
            print("NO Log In Again Window popped up")
        print("__________________________________________")
        print("Dexcom App Launched: Events_Health")
        print("__________________________________________")
        lgr_handle.info("Dexcom App : Events_Health")
        
        try:        
            print("Click on Events")
            lgr_handle.info("Click on Events")
            self.driver.find_element_by_xpath(".//android.widget.TextView[@text='Events']").click()
            sleep(4)
            print("Click on Add Events")
            lgr_handle.info("Click on Events")
            self.driver.find_element_by_xpath(".//android.widget.TextView[@content-desc='Add Event']").click()
            sleep(4)
            #Health event
            print("Select Health Option")
            lgr_handle.info("Select Health Option")
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='Health']").click()
            sleep(5)
            
            #stress=self.driver.find_element_by_xpath("//android.widget.RadioButton[@text='Stress']")
            #illness=self.driver.find_element_by_xpath("//android.widget.RadioButton[@text='Illness']")
            #feelingHigh=self.driver.find_element_by_xpath("//android.widget.RadioButton[@text='Feeling High']")
            #feelingLow=self.driver.find_element_by_xpath("//android.widget.RadioButton[@text='Feeling Low']")
            #alcohol=self.driver.find_element_by_xpath("//android.widget.RadioButton[@text='Alcohol']")
            #cycle=self.driver.find_element_by_xpath("//android.widget.RadioButton[@text='Cycle']")
            
            
            print("Select Health event")
            lgr_handle.info("Select Health event")
            stress=self.driver.find_element_by_xpath("//android.widget.RadioButton[@text='Stress']")
            stress.click()
            sleep(3)
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='ADD']").click()
            sleep(5)
            self.driver.find_element_by_xpath("//android.widget.Button[@text='CONFIRM']").click()
            sleep(5)
            print("Added Health: Stress")
            lgr_handle.info("Added Health: Stress")
            
            #Adding Cycle
            self.driver.find_element_by_xpath(".//android.widget.TextView[@content-desc='Add Event']").click()
            sleep(5)
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='Health']").click()
            sleep(5)
            cycle=self.driver.find_element_by_xpath("//android.widget.RadioButton[@text='Cycle']")
            cycle.click()
            sleep(3)
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='ADD']").click()
            sleep(5)
            self.driver.find_element_by_xpath("//android.widget.Button[@text='CONFIRM']").click()
            sleep(5)
            print("Added Health: Cycle")
            lgr_handle.info("Added Health: Cycle")
            print("Press Back Button")
            lgr_handle.info("Press Back Button")
            self.Press_Device_BackButton()
            print("Added Dexcom_Events_Health")
            lgr_handle.info("Added Dexcom_Events_Health")
            print("__________________________________________")
            lgr_handle.removeHandler(lgr_handle.handlers[0])

        except Exception as e: 
            print(str(e))
            print(type(e))
            lgr_handle.warn(e)
            lgr_handle.warn("**Events_Health**")
            print("**Events_Health**")
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
    
    def g6_Events_Carbs(self):
        dexcomApp_csv_log_path = os.path.join(self.logger_csv_path,"dexcomApp_log.csv")
        lgr_handle = logger(dexcomApp_csv_log_path,self.config_params.get("debug_level"))
        os.system("adb -s "+self.adb_id+" shell am start -n com.dexcom.g6/com.dexcom.cgm.activities.AppCompatabilityActivity")
        sleep(10)
        try:
            if (self.driver.find_element_by_id("android:id/alertTitle").is_displayed()):
                print("Log In Again Window popped up, Handled it")
                self.driver.find_element_by_id("android:id/button2").click()
                sleep(4)
        except Exception as e:
            print("NO Log In Again Window popped up")
        print("__________________________________________")
        print("Dexcom App Launched: Events_Carbs")
        print("__________________________________________")
        lgr_handle.info("Dexcom App : Events_Carbs")
        sleep(5)
        
        try:        
            print("Click on Events")
            lgr_handle.info("Click on Events")
            self.driver.find_element_by_xpath(".//android.widget.TextView[@text='Events']").click()
            sleep(4)
            print("Click on Add Events")
            lgr_handle.info("Click on Events")
            self.driver.find_element_by_xpath(".//android.widget.TextView[@content-desc='Add Event']").click()
            sleep(4)
            #Carbs event
            print("Select Carbs Option")
            lgr_handle.info("Select Carbs Option")
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='Carbs']").click()
            sleep(5)
            Carbs="50"
            self.driver.find_element_by_xpath(".//android.widget.EditText").send_keys(Carbs)#enter Carbs
            sleep(5)        
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='ADD']").click()
            sleep(8)
            self.driver.find_element_by_xpath("//android.widget.Button[@text='CONFIRM']").click()
            sleep(5)
            print("Press Back Button")
            lgr_handle.info("Press Back Button")
            self.Press_Device_BackButton()
            print("Added Dexcom_Events_Carbs")
            lgr_handle.info("Added Dexcom_Events_Carbs")
            print("__________________________________________")
            lgr_handle.removeHandler(lgr_handle.handlers[0])

        except Exception as e: 
            print(str(e))
            print(type(e))
            lgr_handle.warn(e)
            lgr_handle.warn("**Events_Carbs**")
            print("**Events_Carbs**")
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
            
    def g6_Events_FastActInsulin(self):
        dexcomApp_csv_log_path = os.path.join(self.logger_csv_path,"dexcomApp_log.csv")
        lgr_handle = logger(dexcomApp_csv_log_path,self.config_params.get("debug_level"))
        os.system("adb -s "+self.adb_id+" shell am start -n com.dexcom.g6/com.dexcom.cgm.activities.AppCompatabilityActivity")
        sleep(10)
        try:
            if (self.driver.find_element_by_id("android:id/alertTitle").is_displayed()):
                print("Log In Again Window popped up, Handled it")
                self.driver.find_element_by_id("android:id/button2").click()
                sleep(4)
        except Exception as e:
            print("NO Log In Again Window popped up")
        print("__________________________________________")
        print("Dexcom App Launched: Events_FastActInsulin")
        print("__________________________________________")
        lgr_handle.info("Dexcom App : Events_FastActInsulin")
        sleep(5)
        
        try:        
            print("Click on Events")
            lgr_handle.info("Click on Events")
            self.driver.find_element_by_xpath(".//android.widget.TextView[@text='Events']").click()
            sleep(4)
            print("Click on Add Events")
            lgr_handle.info("Click on Events")
            self.driver.find_element_by_xpath(".//android.widget.TextView[@content-desc='Add Event']").click()
            sleep(4)
            #FastActInsulin event
            print("Select Fast Act Insulin Option")
            lgr_handle.info("Select Fast Act Insulin Option")
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='Fast-Acting Insulin']").click()
            sleep(5)
            insulin="20"
            self.driver.find_element_by_xpath(".//android.widget.EditText").send_keys(insulin)#enter Fast Act Insulin
            sleep(5)        
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='ADD']").click()
            sleep(8)
            self.driver.find_element_by_xpath("//android.widget.Button[@text='CONFIRM']").click()
            sleep(5)
            print("Press Back Button")
            lgr_handle.info("Press Back Button")
            self.Press_Device_BackButton()
            print("Added Dexcom_Events_Fast Act Insulin")
            lgr_handle.info("Added Dexcom_Events_Fast Act Insulin")
            print("__________________________________________")

            lgr_handle.removeHandler(lgr_handle.handlers[0])

        except Exception as e: 
            print(str(e))
            print(type(e))
            lgr_handle.warn(e)
            lgr_handle.warn("**Events_FastActInsulin**")
            print("**Events_FastActInsulin**")
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
        
    def g6_Events_LongActInsulin(self):
        dexcomApp_csv_log_path = os.path.join(self.logger_csv_path,"dexcomApp_log.csv")
        lgr_handle = logger(dexcomApp_csv_log_path,self.config_params.get("debug_level"))
        os.system("adb -s "+self.adb_id+" shell am start -n com.dexcom.g6/com.dexcom.cgm.activities.AppCompatabilityActivity")
        sleep(10)
        try:
            if (self.driver.find_element_by_id("android:id/alertTitle").is_displayed()):
                print("Log In Again Window popped up, Handled it")
                self.driver.find_element_by_id("android:id/button2").click()
                sleep(4)
        except Exception as e:
            print("NO Log In Again Window popped up")
        print("__________________________________________")
        print("Dexcom App Launched: Events_LongActInsulin")
        print("__________________________________________")
        lgr_handle.info("Dexcom App : Events_LongActInsulin")
        sleep(5)
        
        try:        
            #LongActInsulin event
            print("Click on Events")
            lgr_handle.info("Click on Events")
            self.driver.find_element_by_xpath(".//android.widget.TextView[@text='Events']").click()
            sleep(5)
            print("Click on Add Events")
            lgr_handle.info("Click on Add Events")
            self.driver.find_element_by_xpath(".//android.widget.TextView[@content-desc='Add Event']").click()
            sleep(5)
            print("Enter Long Act Insulin Option")
            lgr_handle.info("Select Long Act Insulin Option")
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='Long-Acting Insulin']").click()
            sleep(5)
            insulin="40"
            self.driver.find_element_by_xpath(".//android.widget.EditText").send_keys(insulin)#enter Long Act Insulin
            sleep(5)        
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='ADD']").click()
            sleep(8)
            self.driver.find_element_by_xpath("//android.widget.Button[@text='CONFIRM']").click()
            sleep(5)
            print("Press Back Button")
            lgr_handle.info("Press Back Button")
            self.Press_Device_BackButton()
            print("Added Dexcom_Events_Long Act Insulin")
            lgr_handle.info("Added Dexcom_Events_Long Act Insulin")
            print("__________________________________________")
            lgr_handle.removeHandler(lgr_handle.handlers[0])

        except Exception as e: 
            print(str(e))
            print(type(e))
            lgr_handle.warn(e)
            lgr_handle.warn("**Events_LongActInsulin**")
            print("**Events_LongActInsulin**")
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
    
    def g6_delete_Event_Type(self): 
        dexcomApp_csv_log_path = os.path.join(self.logger_csv_path,"dexcomApp_log.csv")
        lgr_handle = logger(dexcomApp_csv_log_path,self.config_params.get("debug_level"))
        os.system("adb -s "+self.adb_id+" shell am start -n com.dexcom.g6/com.dexcom.cgm.activities.AppCompatabilityActivity")
        sleep(10)
        try:
            if (self.driver.find_element_by_id("android:id/alertTitle").is_displayed()):
                print("Log In Again Window popped up, Handled it")
                self.driver.find_element_by_id("android:id/button2").click()
                sleep(4)
        except Exception as e:
            print("NO Log In Again Window popped up")
        print("__________________________________________")
        print("Dexcom App Launched: Delete_Events")
        print("__________________________________________")
        lgr_handle.info("Dexcom App : Delete_Events")
        sleep(5)
    
        try:
            print("Click on Events")
            lgr_handle.info("Click on Events")
            self.driver.find_element_by_xpath(".//android.widget.TextView[@text='Events']").click()
            sleep(8)
            print("Click on Edit Events")
            lgr_handle.info("Click on Edit Events")
            self.driver.find_element_by_id("com.dexcom.g6:id/id_edit").click() 
            sleep(2)
            try:
                i = 0
                while True:
                    print("Click Delete Icon")
                    lgr_handle.info("Click Delete Icon")
                    delete_icon=self.driver.find_element_by_xpath("//android.widget.ImageView[contains(@resource-id,'id_delete')]")
                    delete_icon.click()
                    sleep(2)
                    i+=1
                    print("Click DELETE EVENT")
                    lgr_handle.info("Click DELETE EVENT")
                    self.driver.find_element_by_xpath("//android.widget.Button[contains(@text,'DELETE EVENT')]").click()
                    sleep(4)
                    print("Deleted Event: "+str(i))
                    lgr_handle.info("Deleted Event: "+str(i))
            except Exception as e:
                #print(e)
                self.driver.find_element_by_id("com.dexcom.g6:id/id_done").click()
                print("Click Done Icon")
                lgr_handle.info("Click Done Icon")
            print("Press Back Button")
            lgr_handle.info("Press Back Button")
            self.Press_Device_BackButton()
            lgr_handle.removeHandler(lgr_handle.handlers[0])
        except Exception as e: 
            print(str(e))
            print(type(e))
            lgr_handle.warn(e)
            lgr_handle.warn("**Delete_Events**")
            print("**Delete_Events**")
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
    
