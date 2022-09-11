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





class Test_Bed_MakeCall_DisconnectCall(Common_Utilities):
    def __init__(self):
        pass


    def operate_Call_on_Mobile(self,dynamic_flag,dynamic_call_time):
        callonMobile_csv_log_path = os.path.join(self.logger_csv_path,"CallonMobile_log.csv")
        lgr_handle = logger(callonMobile_csv_log_path,self.config_params.get("debug_level"))
        print("-------------------------------------")
        print("Placing and Disconnecting Call on Mobile device")
        print("-------------------------------------")
        sleep(2)
        lgr_handle.info("\n")
        try:
            lgr_handle.info("Placing a Call")
            print("Placing a call on Mobile Device")
            call=self.makeaCall()
            print(call)
            if (call==True):
                #PASS TIMER
                if dynamic_flag == True:
                    timeOut = dynamic_call_time
                else:
                    timeOut=self.config_params.get("Calling_Timer")
                lgr_handle.info("Call will continute for '"+str(timeOut)+"' seconds")
                print("Call Started, it will continute for '"+str(timeOut)+"' seconds")
                sleep(timeOut)
                lgr_handle.info("Disconnecting Call")
                print("Disconnecting Call")
                self.endCall()
                lgr_handle.info("Called Duration: '"+str(timeOut)+"' seconds")
                print("Called Duration: '"+str(timeOut)+"' seconds")
            print("Exit: Call_on_Mobile")    
            print("____________________________________________________________________\n")   
            lgr_handle.info("Exit: Call_on_Mobile") 
            lgr_handle.removeHandler(lgr_handle.handlers[0])
            
        except Exception as e:
            print(str(e))
            print(type(e))
            lgr_handle.warn(e)
            lgr_handle.warn("**Test_Bed_MakeCall_DisconnectCall**")
            print("**Test_Bed_MakeCall_DisconnectCall**")
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
