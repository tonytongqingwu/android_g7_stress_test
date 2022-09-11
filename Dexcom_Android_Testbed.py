#!/usr/bin/env python3

#Ver1.0.0

"""
Modules to be imported for running this script
"""
import sys

sys.path.append('../Common_Utilities/')
from Common_Utilities.Common_Utilities import Common_Utilities

sys.path.append('../TestBed')
from TestBed.Test_Bed_CGM import Test_Bed_CGM
from TestBed.Test_Bed_Flipkart import Test_Bed_Flipkart
from TestBed.Test_Bed_Amazon import Test_Bed_Amazon
from TestBed.Test_Bed_Youtube import Test_Bed_Youtube
from TestBed.Test_Bed_YouTubeMusic import Test_Bed_YouTubeMusic
from TestBed.Test_Bed_Chrome_Browser import Test_Bed_Chrome_Browser
from TestBed.Test_Bed_FaceBook import Test_Bed_FaceBook
from TestBed.Test_Bed_OpenCamera_CapturePhoto import Test_Bed_OpenCamera_CapturePhoto
from TestBed.TestBed_Services import TestBed_Services
from TestBed.Test_Bed_LaunchGame import Test_Bed_LaunchGame
from TestBed.Test_Bed_MakeCall_DisconnectCall import Test_Bed_MakeCall_DisconnectCall
from TestBed.TestBed_BatteryLevel import TestBed_BatteryLevel
from TestBed.Test_Bed_Guardian import Test_Bed_Guardian
from TestBed.Test_Bed_Instagram import Test_Bed_Instagram
from TestBed.Test_Bed_GoogleMaps import Test_Bed_GoogleMaps
from TestBed.Test_Bed_Youtube_Download import Test_Bed_Youtube_Download
from TestBed.Test_Bed_BLE_Doctor_Dexcom import Test_Bed_BLE_Doctor_Dexcom
from TestBed.Test_Bed_SendSMS import Test_Bed_SendSMS
from TestBed.Test_Bed_Contacts import Test_Bed_Contacts
from TestBed.Test_Bed_Settings import Test_Bed_Settings
from TestBed.Test_Bed_BLE_G7 import Test_Bed_BLE_G7





import csv
import os
import psutil
import ctypes
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter import *
from PIL import ImageTk,Image 
from tkinter import messagebox
from time import sleep
import argparse
import re
import threading
from threading import Thread, Event
from multiprocessing import Process
import datetime
#import winsound
#from datetime import datetime, timedelta
import subprocess
sys.path.append('../Logger/')
from Logger.Dexcom_Logger import logger
# os.system('color')



class Testbed_Timer_Thread(threading.Thread):
    def __init__(self):
        super(Testbed_Timer_Thread, self).__init__()
        self.iterations = 0
        self.daemon = True  # Allow main to exit even if still running.
        self.paused = True  # Start out paused.
        self.state = threading.Condition()

    def run(self,invoke_testbed):
        self.resume()
        while True:
            with self.state:
                if self.paused:
                    self.state.wait()  # Block execution until notified.
            invoke_testbed()
            self.iterations += 1

    def pause(self):
        with self.state:
            self.paused = True  # Block self.

    def resume(self):
        with self.state:
            self.paused = False
            self.state.notify()  # Unblock self if waiting.



def terminate_thread(thread):
    """Terminates a python thread from another thread.

    :param thread: a threading.Thread instance
    """
    if not thread.is_alive():
        return

    exc = ctypes.py_object(SystemExit)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
        ctypes.c_long(thread.ident), exc)
    if res == 0:
        raise ValueError("nonexistent thread id")
    elif res > 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(thread.ident, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")




class android_testbed(Common_Utilities):
    def __init__(self,adb_id,port_num,dexcom_app_type,testbed_scenario,logger_flag,mobile_no):
        super().__init__(adb_id,port_num,dexcom_app_type,testbed_scenario,logger_flag,mobile_no)
        self.logcat_restart_handle = True
        self.dexcom_app_type = dexcom_app_type
      

    
    def logcat_fire(self):
        current_date_and_time = datetime.datetime.now()
        time=current_date_and_time.strftime("%Y-%m-%d")
        if ":" in adb_id:
            adb_id_rename = adb_id.replace(":","_")
            self.logcat_file_path = os.path.join(os.getcwd(),"Logs_"+adb_id_rename+"/")
        else:
            self.logcat_file_path = os.path.join(os.getcwd(),"Logs_"+adb_id+"/")
            
        if not self.logcat_file_path:
            os.makedirs(self.logcat_file_path)
            sleep(2)
        self.logcat_file = self.logcat_file_path+"Logcat_"+str(time)+".log"
        self.logcat_filter = self.logcat_file_path+"Realtime_Missing_EGVs_Logcat_Analysis.csv"
        file = open(self.logcat_file, 'a')
        file_filter = open(self.logcat_filter, 'a')

        while True:
            order = "adb -s "+self.adb_id+" logcat"
            pi = subprocess.Popen(order, shell=True, stdout=subprocess.PIPE, creationflags=0x00000200) #creationflags=0x00000200 to ignore keyboard interrupt signal on logcat thread
            t = 0
            conn_count = 0
            prev_time = 0
            curr_time = 0
            FMT = '%m-%d %H:%M:%S.%f'
            
            if self.dexcom_app_type == "G6":
                try:
                    for i in iter(pi.stdout.readline, 'b'): 
                        if i == b'' and self.logcat_restart_handle == True:
                            print("start logcat again")
                            file_filter.write("Starting Logcat Again, probably due to loose wired connection/loss of adb server")
                            file_filter.write("\n")
                            break
                        if i != b'':   
                            file.write(str(i))
                            file.write("\n")

                        if "Force stopping com.dexcom.g6" in str(i):
                            line = str(i)
                            line = line.split(" ")
                            line_0 = str(line[0]).replace("b\'","")
                            curr_time = line_0 + " " + str(line[1])
                            print("\033[91mDexcom G6 App forced kill at: \033[0m"+curr_time)
                            file_filter.write("Dexcom G6 App forced kill at: "+curr_time)
                      
                        if "TransmitterBLE: Connected" in str(i):  
                            conn_count+=1
                            line = str(i)
                            subs1 = re.findall('\Dexcom.*',line)
                            subs1 = str(subs1[0])
                            TX_ADDRESS = subs1.replace(r"\r\n'", " ")
                            
                            
                            line = line.split(" ")
                            line_0 = str(line[0]).replace("b\'","")
                            curr_time = line_0 + " " + str(line[1])                        
                            print("\033[96mBLE Connection Established at \033[0m"+str(curr_time))
                            file_filter.write("***Connection Established at ***"+str(curr_time))
                            file_filter.write("\n")
                            
                        
                            if conn_count>1:
                                tdelta = datetime.datetime.strptime(str(curr_time), FMT) - datetime.datetime.strptime(str(prev_time), FMT)
                                prev_time_list= (prev_time.split("."))
                                curr_time_list = (curr_time.split("."))
                                if str(prev_time_list[0]) == str(curr_time_list[0]):
                                    elapsed_time = int((tdelta.microseconds / 1000))
                                else:
                                    elapsed_time = int((tdelta.seconds * 1000) + (tdelta.microseconds / 1000))
                                    
                                comm_interval_gap = float(elapsed_time/1000)
                                print("\033[96mcommunication_interval_diff(seconds}: \033[0m"+str(comm_interval_gap))
                                if (comm_interval_gap) >= 320:
                                    print("\033[91mConnection took more than 5 mins to establish..\033[0m")
                                    file_filter.write("Connection took more than 5 mins to establish between "+prev_time+" and "+curr_time)
                                    file_filter.write("\n")
                                    pkts_lost = round(comm_interval_gap/300 - 1)
                                    print("\033[91mNo of packets lost is \033[0m"+str(pkts_lost))
                                    file_filter.write("No of packets lost is "+str(pkts_lost))
                                    file_filter.write("\n")
                                    if pkts_lost>=3:
                                        print("\033[91m###Signal loss could be detected at \033[0m"+curr_time)
                                        file_filter.write("###Signal loss could be detected between "+prev_time+" and "+curr_time)
                                        file_filter.write("\n")
                                        frequency = 2500  # in Hz
                                        duration = 20  # in seconds
                                        # winsound.Beep(frequency, duration*1000)
                                        #print("Exiting Testbed loop and cleaning up...")
                                    
                            prev_time = curr_time
                            
                        if "TransmitterBLE:   \"rssi\":" in str(i):
                        
                            line = str(i)
                            line = line.split("   ")
                            time = str(line[0])
                            time = time.split(" ")
                            rssi = str(line[1])
                            rssi = rssi.split(",")
                            rssi = str(rssi[0])
                            rssi = rssi.split(":")
                            rssi = str(rssi[1])
                            file_filter.write("RSSI: "+str(rssi)+" at time: "+str(time[1]))
                            file_filter.write("\n")
                            print("\033[93mRSSI: \033[0m"+str(rssi)+" at time: "+str(time[1]))
                            
                            
                        t = t+1
                        if t == 10:
                            t = 0
                            file.flush()
                            file_filter.flush()
                                            
                except BaseException as e:
                    print(e)
                    

            if self.dexcom_app_type == "Always Connected":
                try:
                    for i in iter(pi.stdout.readline, 'b'): 
                        if i == b'' and self.logcat_restart_handle == True:
                            print("start logcat again")
                            file_filter.write("Starting Logcat Again, probably due to loose wired connection/loss of adb server")
                            file_filter.write("\n")
                            break
                        if i != b'':   
                            file.write(str(i))
                            file.write("\n")

                      
                        if "PredictedEGVReceived" in str(i):  
                            conn_count+=1
                            line = str(i)
                            line = line.split(" ")
                            line_0 = str(line[0]).replace("b\'","")
                            curr_time = line_0 + " " + str(line[1])                        
                            print("\033[96mBLE Connection Established at \033[0m"+str(curr_time))
                            file_filter.write("***Connection Established at ***"+str(curr_time))
                            file_filter.write("\n")
                          
                            
                        
                            if conn_count>1:
                                tdelta = datetime.datetime.strptime(str(curr_time), FMT) - datetime.datetime.strptime(str(prev_time), FMT)
                                prev_time_list= (prev_time.split("."))
                                curr_time_list = (curr_time.split("."))
                                if str(prev_time_list[0]) == str(curr_time_list[0]):
                                    elapsed_time = int((tdelta.microseconds / 1000))
                                else:
                                    elapsed_time = int((tdelta.seconds * 1000) + (tdelta.microseconds / 1000))
                                    
                                comm_interval_gap = float(elapsed_time/1000)
                                print("\033[96mcommunication_interval_diff(seconds}: \033[0m"+str(comm_interval_gap))
                                if (comm_interval_gap) >= 320:
                                    print("\033[91mConnection took more than 5 mins to establish..\033[0m")
                                    file_filter.write("Connection took more than 5 mins to establish between "+prev_time+" and "+curr_time)
                                    file_filter.write("\n")
                                    pkts_lost = round(comm_interval_gap/300 - 1)
                                    print("\033[91mNo of packets lost is \033[0m"+str(pkts_lost))
                                    file_filter.write("No of packets lost is "+str(pkts_lost))
                                    file_filter.write("\n")
                                    if pkts_lost>=3:
                                        print("\033[91m###Signal loss could be detected at \033[0m"+curr_time)
                                        file_filter.write("###Signal loss could be detected between "+prev_time+" and "+curr_time)
                                        file_filter.write("\n")
                                        frequency = 2500  # in Hz
                                        duration = 20  # in seconds
                                        # winsound.Beep(frequency, duration*1000)
                            prev_time = curr_time
                            
                            
                        t = t+1
                        if t == 10:
                            t = 0
                            file.flush()
                            file_filter.flush()
                                            
                except BaseException as e:
                    print(e)
        
                        
         
        
    def execute_test_bed(self):
        loop_count = 0
        if testbed_scenario == "Scenario-1":
            dynamic_flag = False
            while True:
                if self.dexcom_app_type == "Always Connected":
                    Test_Bed_BLE_Doctor_Dexcom.launch_BLE_Doctor_Dexcom(self)
                elif self.dexcom_app_type == "G6":
                    Test_Bed_CGM.launch_dexcom_app(self)
                    Test_Bed_CGM.settings_alerts(self)
                    Test_Bed_CGM.g6_Events_Exercise(self)
                    Test_Bed_CGM.g6_Events_Health(self)
                    Test_Bed_CGM.g6_Events_Carbs(self)
                    Test_Bed_CGM.g6_Events_FastActInsulin(self)
                    Test_Bed_CGM.g6_Events_LongActInsulin(self)
                    Test_Bed_CGM.g6_delete_Event_Type(self)
                elif self.dexcom_app_type == "G7":
                    Test_Bed_BLE_G7.launch_BLE_G7(self)
                    Test_Bed_BLE_G7.g7_settings_alerts(self)
                    Test_Bed_BLE_G7.g7_Events_Blood_Glucose(self)
                    Test_Bed_BLE_G7.g7_delete_Event_Type(self)
                    
                else:
                    pass
                
                Test_Bed_Youtube.operate_Youtube(self,dynamic_flag,None)
                Test_Bed_Flipkart.operate_flipkart(self)
                Test_Bed_Amazon.operate_Amazon(self)
                Test_Bed_YouTubeMusic.operate_YouTubeMusic(self,dynamic_flag,None)
                Test_Bed_Chrome_Browser.operate_Chrome_Browser(self)
                Test_Bed_FaceBook.operate_FaceBook(self)
                Test_Bed_OpenCamera_CapturePhoto.operate_Camera(self)
                loop_count+=1
                
                if DEXCOM_TIMER == False:
                    break
                
                print("\033[92mTestbed Loop Completed\033[0m")
                print("\033[92mTotal Loop count is\033[0m",loop_count)
              
               

        elif testbed_scenario == "Scenario-2":
            dynamic_flag = False
            if self.dexcom_app_type == "Always Connected":
                Test_Bed_BLE_Doctor_Dexcom.launch_BLE_Doctor_Dexcom(self)
                    
            elif self.dexcom_app_type == "G6":
                Test_Bed_CGM.launch_dexcom_app(self)
                Test_Bed_CGM.settings_alerts(self)
                Test_Bed_CGM.g6_Events_Exercise(self)
                Test_Bed_CGM.g6_Events_Health(self)
                Test_Bed_CGM.g6_Events_Carbs(self)
                Test_Bed_CGM.g6_Events_FastActInsulin(self)
                Test_Bed_CGM.g6_Events_LongActInsulin(self)
                Test_Bed_CGM.g6_delete_Event_Type(self)
                
            elif self.dexcom_app_type == "G7":
                Test_Bed_BLE_G7.launch_BLE_G7(self)
                Test_Bed_BLE_G7.g7_settings_alerts(self)
                Test_Bed_BLE_G7.g7_Events_Blood_Glucose(self)
                Test_Bed_BLE_G7.g7_delete_Event_Type(self)
                
            else:
                pass
                
            while True:
                Test_Bed_Youtube.operate_Youtube(self,dynamic_flag,None)
                Test_Bed_Flipkart.operate_flipkart(self)
                Test_Bed_Amazon.operate_Amazon(self)
                Test_Bed_YouTubeMusic.operate_YouTubeMusic(self,dynamic_flag,None)
                Test_Bed_Chrome_Browser.operate_Chrome_Browser(self)
                Test_Bed_FaceBook.operate_FaceBook(self)
                Test_Bed_OpenCamera_CapturePhoto.operate_Camera(self)
                
                  
                loop_count+=1
                
                if DEXCOM_TIMER == False:
                    break
                
                print("\033[92mTestbed Loop Completed\033[0m")
                print("\033[92mTotal Loop count is\033[0m",loop_count)
                
        
        elif testbed_scenario == "Scenario-3":
            dynamic_flag = False
            while True:
                if self.dexcom_app_type == "Always Connected":
                    Test_Bed_BLE_Doctor_Dexcom.launch_BLE_Doctor_Dexcom(self)
                if self.dexcom_app_type == "G6":
                    Test_Bed_CGM.launch_dexcom_app(self)
                    Test_Bed_CGM.settings_alerts(self)
                elif self.dexcom_app_type == "G7":
                    Test_Bed_BLE_G7.launch_BLE_G7(self)
                    Test_Bed_BLE_G7.g7_settings_alerts(self)
                    
                Test_Bed_Youtube.operate_Youtube(self,dynamic_flag,None)
                Test_Bed_Flipkart.operate_flipkart(self)
                self.disable_WiFi()
                TestBed_Services.wifi_Disable(self)
                
                if self.dexcom_app_type == "G6":
                    Test_Bed_CGM.launch_dexcom_app(self)
                    Test_Bed_CGM.g6_Events_Exercise(self)
                    Test_Bed_CGM.g6_Events_Health(self)
                    Test_Bed_CGM.g6_Events_Carbs(self)
                    Test_Bed_CGM.g6_Events_FastActInsulin(self)
                elif self.dexcom_app_type == "Always Connected":
                    Test_Bed_BLE_Doctor_Dexcom.launch_BLE_Doctor_Dexcom(self)
                elif self.dexcom_app_type == "G7":
                    Test_Bed_BLE_G7.g7_Events_Blood_Glucose(self)
                    
                self.enable_WiFi()
                TestBed_Services.wifi_Enable(self)
                Test_Bed_Amazon.operate_Amazon(self)
                Test_Bed_YouTubeMusic.operate_YouTubeMusic(self,dynamic_flag,None)
                TestBed_Services.wifi_Disable(self)
                Test_Bed_OpenCamera_CapturePhoto.operate_Camera(self)
                
                if self.dexcom_app_type == "G6":
                    Test_Bed_CGM.launch_dexcom_app(self)
                    Test_Bed_CGM.settings_alerts(self)
                    Test_Bed_CGM.g6_delete_Event_Type(self)
                elif self.dexcom_app_type == "Always Connected":
                    Test_Bed_BLE_Doctor_Dexcom.launch_BLE_Doctor_Dexcom(self)
                elif self.dexcom_app_type == "G7":
                    Test_Bed_BLE_G7.launch_BLE_G7(self)
                    Test_Bed_BLE_G7.g7_settings_alerts(self)
                    Test_Bed_BLE_G7.g7_delete_Event_Type(self)    
                
                TestBed_Services.wifi_Enable(self)
                Test_Bed_Chrome_Browser.operate_Chrome_Browser(self)
                Test_Bed_FaceBook.operate_FaceBook(self)
                  
                loop_count+=1
                
                if DEXCOM_TIMER == False:
                    break
                
                print("\033[92mTestbed Loop Completed\033[0m")
                print("\033[92mTotal Loop count is\033[0m",loop_count)
                
                
        elif testbed_scenario == "Scenario-4":
            dynamic_flag = False
            while True:
                if self.dexcom_app_type == "G6":
                    Test_Bed_CGM.launch_dexcom_app(self)
                elif self.dexcom_app_type == "Always Connected":
                    Test_Bed_BLE_Doctor_Dexcom.launch_BLE_Doctor_Dexcom(self)
                elif self.dexcom_app_type == "G7":
                    Test_Bed_BLE_G7.launch_BLE_G7(self)  
                    
                Test_Bed_OpenCamera_CapturePhoto.operate_Camera(self)
                Test_Bed_LaunchGame.launch_Game(self)
                
                if self.dexcom_app_type == "G6":
                    Test_Bed_CGM.launch_dexcom_app(self)
                elif self.dexcom_app_type == "Always Connected":
                    Test_Bed_BLE_Doctor_Dexcom.launch_BLE_Doctor_Dexcom(self)
                elif self.dexcom_app_type == "G7":
                    Test_Bed_BLE_G7.launch_BLE_G7(self)    
                    
                Test_Bed_OpenCamera_CapturePhoto.operate_Camera(self)
                Test_Bed_LaunchGame.launch_Game(self)
                Test_Bed_Youtube.operate_Youtube(self,dynamic_flag,None)
                Test_Bed_Flipkart.operate_flipkart(self)
                Test_Bed_YouTubeMusic.operate_YouTubeMusic(self,dynamic_flag,None)
                
                if self.dexcom_app_type == "G6":
                    Test_Bed_CGM.launch_dexcom_app(self)
                elif self.dexcom_app_type == "Always Connected":
                    Test_Bed_BLE_Doctor_Dexcom.launch_BLE_Doctor_Dexcom(self)
                elif self.dexcom_app_type == "G7":
                    Test_Bed_BLE_G7.launch_BLE_G7(self)   
                    
                Test_Bed_Youtube.operate_Youtube(self,dynamic_flag,None)
                Test_Bed_Flipkart.operate_flipkart(self)
                Test_Bed_YouTubeMusic.operate_YouTubeMusic(self,dynamic_flag,None)
                Test_Bed_OpenCamera_CapturePhoto.operate_Camera(self)
                Test_Bed_LaunchGame.launch_Game(self)
                
                if self.dexcom_app_type == "G6":
                    Test_Bed_CGM.launch_dexcom_app(self)
                elif self.dexcom_app_type == "Always Connected":
                    Test_Bed_BLE_Doctor_Dexcom.launch_BLE_Doctor_Dexcom(self)
                elif self.dexcom_app_type == "G7":
                    Test_Bed_BLE_G7.launch_BLE_G7(self)  
                    
                Test_Bed_OpenCamera_CapturePhoto.operate_Camera(self)
                Test_Bed_LaunchGame.launch_Game(self)
                Test_Bed_Youtube.operate_Youtube(self,dynamic_flag,None)
                Test_Bed_Flipkart.operate_flipkart(self)
                Test_Bed_YouTubeMusic.operate_YouTubeMusic(self,dynamic_flag,None)
                
                if self.dexcom_app_type == "G6":
                    Test_Bed_CGM.launch_dexcom_app(self)
                elif self.dexcom_app_type == "Always Connected":
                    Test_Bed_BLE_Doctor_Dexcom.launch_BLE_Doctor_Dexcom(self)
                elif self.dexcom_app_type == "G7":
                    Test_Bed_BLE_G7.launch_BLE_G7(self)   
                    
                Test_Bed_Youtube.operate_Youtube(self,dynamic_flag,None)
                Test_Bed_Flipkart.operate_flipkart(self)
                Test_Bed_YouTubeMusic.operate_YouTubeMusic(self,dynamic_flag,None)
                Test_Bed_Guardian.operate_Guardian(self)

                loop_count+=1
                
                if DEXCOM_TIMER == False:
                    break
                
                print("\033[92mTestbed Loop Completed\033[0m")
                print("\033[92mTotal Loop count is\033[0m",loop_count)
                

        elif testbed_scenario == "Scenario-5":
            dynamic_flag = False
            while True:
                if self.dexcom_app_type == "G6":
                    Test_Bed_CGM.launch_dexcom_app(self)
                    Test_Bed_CGM.settings_alerts(self)
                elif self.dexcom_app_type == "Always Connected":
                    Test_Bed_BLE_Doctor_Dexcom.launch_BLE_Doctor_Dexcom(self)
                elif self.dexcom_app_type == "G7":
                    Test_Bed_BLE_G7.launch_BLE_G7(self)
                    Test_Bed_BLE_G7.g7_settings_alerts(self)   
                
                Test_Bed_Youtube.operate_Youtube(self,dynamic_flag,None)
                Test_Bed_Flipkart.operate_flipkart(self)
                Test_Bed_MakeCall_DisconnectCall.operate_Call_on_Mobile(self,dynamic_flag,None)
                Test_Bed_SendSMS.operate_sendSMS_on_Mobile(self)
                
                
                if self.dexcom_app_type == "G6":
                    Test_Bed_CGM.launch_dexcom_app(self)
                    Test_Bed_CGM.g6_Events_Exercise(self)
                    Test_Bed_CGM.g6_Events_Carbs(self)
                elif self.dexcom_app_type == "Always Connected":
                    Test_Bed_BLE_Doctor_Dexcom.launch_BLE_Doctor_Dexcom(self)
                elif self.dexcom_app_type == "G7":
                    Test_Bed_BLE_G7.launch_BLE_G7(self)   
                    Test_Bed_BLE_G7.g7_Events_Blood_Glucose(self)
                Test_Bed_YouTubeMusic.operate_YouTubeMusic(self,dynamic_flag,None)
                Test_Bed_FaceBook.operate_FaceBook(self)
                Test_Bed_Youtube.operate_Youtube(self,dynamic_flag,None)
                Test_Bed_Guardian.operate_Guardian(self)
                Test_Bed_SendSMS.operate_sendSMS_on_Mobile(self)

                
                if self.dexcom_app_type == "G6":
                    Test_Bed_CGM.g6_Events_FastActInsulin(self)
                elif self.dexcom_app_type == "Always Connected":
                    Test_Bed_BLE_Doctor_Dexcom.launch_BLE_Doctor_Dexcom(self)
                elif self.dexcom_app_type == "G7":
                    Test_Bed_BLE_G7.g7_Events_Blood_Glucose(self)
                    
                Test_Bed_YouTubeMusic.operate_YouTubeMusic(self,dynamic_flag,None)
                Test_Bed_Amazon.operate_Amazon(self)
                Test_Bed_YouTubeMusic.operate_YouTubeMusic(self,dynamic_flag,None)
                Test_Bed_Youtube.operate_Youtube(self,dynamic_flag,None)
                
                if self.dexcom_app_type == "G6":
                    Test_Bed_CGM.launch_dexcom_app(self)
                    Test_Bed_CGM.g6_delete_Event_Type(self)
                elif self.dexcom_app_type == "Always Connected":
                    Test_Bed_BLE_Doctor_Dexcom.launch_BLE_Doctor_Dexcom(self)
                elif self.dexcom_app_type == "G7":
                    Test_Bed_BLE_G7.launch_BLE_G7(self)
                    Test_Bed_BLE_G7.g7_delete_Event_Type(self)    
                
                Test_Bed_MakeCall_DisconnectCall.operate_Call_on_Mobile(self,dynamic_flag,None)
                Test_Bed_Youtube.operate_Youtube(self,dynamic_flag,None)
                Test_Bed_Instagram.operate_Instagram(self)
                Test_Bed_YouTubeMusic.operate_YouTubeMusic(self,dynamic_flag,None)
                Test_Bed_GoogleMaps.operate_GoogleMaps(self)
                Test_Bed_Guardian.operate_Guardian(self)

                loop_count+=1
                
                if DEXCOM_TIMER == False:
                    break
                
                print("\033[92mTestbed Loop Completed\033[0m")
                print("\033[92mTotal Loop count is\033[0m",loop_count)

                
        elif testbed_scenario == "Scenario-6":
            dynamic_flag = False
            while True:
                if self.dexcom_app_type == "G6":
                    Test_Bed_CGM.launch_dexcom_app(self)
                elif self.dexcom_app_type == "Always Connected":
                    Test_Bed_BLE_Doctor_Dexcom.launch_BLE_Doctor_Dexcom(self)
                elif self.dexcom_app_type == "G7":
                    Test_Bed_BLE_G7.launch_BLE_G7(self)
                    
                Test_Bed_Youtube.operate_Youtube(self,dynamic_flag,None)
                Test_Bed_OpenCamera_CapturePhoto.operate_Camera(self)
                Test_Bed_YouTubeMusic.operate_YouTubeMusic(self,dynamic_flag,None)
                Test_Bed_FaceBook.operate_FaceBook(self)
                Test_Bed_Youtube.operate_Youtube(self,dynamic_flag,None)
                Test_Bed_GoogleMaps.operate_GoogleMaps(self)
                Test_Bed_Youtube.operate_Youtube(self,dynamic_flag,None)
                Test_Bed_Instagram.operate_Instagram(self)
                Test_Bed_Youtube.operate_Youtube(self,dynamic_flag,None)
                Test_Bed_GoogleMaps.operate_GoogleMaps(self)
                Test_Bed_Youtube.operate_Youtube(self,dynamic_flag,None)
                Test_Bed_Instagram.operate_Instagram(self)
                Test_Bed_YouTubeMusic.operate_YouTubeMusic(self,dynamic_flag,None)
                Test_Bed_GoogleMaps.operate_GoogleMaps(self)
                Test_Bed_Youtube.operate_Youtube(self,dynamic_flag,None)
                Test_Bed_FaceBook.operate_FaceBook(self)
                Test_Bed_Youtube.operate_Youtube(self,dynamic_flag,None)
                Test_Bed_OpenCamera_CapturePhoto.operate_Camera(self)
                Test_Bed_Youtube.operate_Youtube(self,dynamic_flag,None)
                Test_Bed_GoogleMaps.operate_GoogleMaps(self)
                Test_Bed_Youtube.operate_Youtube(self,dynamic_flag,None)
                Test_Bed_GoogleMaps.operate_GoogleMaps(self)
                Test_Bed_YouTubeMusic.operate_YouTubeMusic(self,dynamic_flag,None)
                Test_Bed_FaceBook.operate_FaceBook(self)
                Test_Bed_Youtube.operate_Youtube(self,dynamic_flag,None)
                Test_Bed_GoogleMaps.operate_GoogleMaps(self)
                Test_Bed_Youtube.operate_Youtube(self,dynamic_flag,None)
                Test_Bed_Instagram.operate_Instagram(self)
                Test_Bed_Youtube.operate_Youtube(self,dynamic_flag,None)
                Test_Bed_GoogleMaps.operate_GoogleMaps(self)
                Test_Bed_Youtube.operate_Youtube(self,dynamic_flag,None)

                loop_count+=1
                
                if DEXCOM_TIMER == False:
                    break
                print("\033[92mTestbed Loop Completed\033[0m")
                print("\033[92mTotal Loop count is\033[0m",loop_count)
        
        elif testbed_scenario == "Scenario-7":
            dynamic_flag = False
            while True:
                if self.dexcom_app_type == "G6":
                    Test_Bed_CGM.launch_dexcom_app(self)
                    Test_Bed_CGM.settings_alerts(self)
                elif self.dexcom_app_type == "Always Connected":
                    Test_Bed_BLE_Doctor_Dexcom.launch_BLE_Doctor_Dexcom(self)
                elif self.dexcom_app_type == "G7":
                    Test_Bed_BLE_G7.launch_BLE_G7(self)
                    Test_Bed_BLE_G7.g7_settings_alerts(self)   
                
                TestBed_Services.airplaneMode_Enable(self)
                TestBed_Services.bluetooth_ON(self)
                
                if self.dexcom_app_type == "G6":    
                    Test_Bed_CGM.g6_Events_Exercise(self)
                    Test_Bed_CGM.g6_Events_Health(self)
                    Test_Bed_CGM.g6_Events_Carbs(self)
                    Test_Bed_CGM.g6_Events_FastActInsulin(self)
                    Test_Bed_CGM.g6_Events_LongActInsulin(self)
                elif self.dexcom_app_type == "Always Connected":
                    Test_Bed_BLE_Doctor_Dexcom.launch_BLE_Doctor_Dexcom(self)
                elif self.dexcom_app_type == "G7":
                    Test_Bed_BLE_G7.g7_Events_Blood_Glucose(self)
                
                Test_Bed_Youtube_Download.operate_Youtube(self,dynamic_flag,None)
                Test_Bed_GoogleMaps.operate_GoogleMaps(self)
                Test_Bed_OpenCamera_CapturePhoto.operate_Camera(self)
                Test_Bed_Settings.open_Settings(self)
                Test_Bed_Contacts.open_Contacts(self)
                TestBed_Services.airplaneMode_Disable(self)
                
                if self.dexcom_app_type == "G6":    
                    Test_Bed_CGM.g6_delete_Event_Type(self)
                elif self.dexcom_app_type == "Always Connected":
                    Test_Bed_BLE_Doctor_Dexcom.launch_BLE_Doctor_Dexcom(self)
                elif self.dexcom_app_type == "G7":
                    Test_Bed_BLE_G7.g7_delete_Event_Type(self)    
                
                loop_count+=1
                
                if DEXCOM_TIMER == False:
                    break
                print("\033[92mTestbed Loop Completed\033[0m")
                print("\033[92mTotal Loop count is\033[0m",loop_count)
        
                
        elif testbed_scenario == "Dynamic":
            import xlrd
            loc = ("Dynamic_Scenarios_config.xlsx")
            wb = xlrd.open_workbook(loc)
            sheet = wb.sheet_by_name("Create_Dynamic_Scenarios")
            sheet.cell_value(0, 0)
            dynamic_flag = True

            Dexcom_flag = False
            Amazon_flag = False
            disbale_wifi_flag = False
            Flipkart_flag = False
            enable_wifi_flag = False
            Youtube_flag = False
            Youtube_music_flag = False
            Facebook_flag = False
            Camera_flag = False
            Chrome_flag = False
            GuardianApp_flag = False
            Instagram_flag = False
            GoggleMap_flag = False
            Airplane_Mode_Enable_flag = False
            Airplane_Mode_Disable_flag = False
            Make_Call_flag = False
            End_Call_flag = False
            Bluetooth_Enable_flag = False
            Bluetooth_Disable_flag = False
            BLEDoctor_flag = False

            
            
            while True:
                for i in range(sheet.nrows):
                    try:
                        a = sheet.row_values(i)
                        if a[0] == "Dexcom_G6" and Dexcom_flag == False:
                            print("invoke Dexcom_G6")
                            Test_Bed_CGM.launch_dexcom_app(self)
                            Test_Bed_CGM.settings_alerts(self)
                            Test_Bed_CGM.g6_Events_Exercise(self)
                            Test_Bed_CGM.g6_Events_Health(self)
                            Test_Bed_CGM.g6_Events_Carbs(self)
                            Test_Bed_CGM.g6_Events_FastActInsulin(self)
                            Test_Bed_CGM.g6_Events_LongActInsulin(self)
                            Test_Bed_CGM.g6_delete_Event_Type(self)
                            Dexcom_flag = True
                        elif a[0] == "Amazon" and Amazon_flag == False:
                            print("invoke Amazon")
                            Test_Bed_Amazon.operate_Amazon(self)
                            Amazon_flag = True
                        elif a[0] == "Wifi disable" and disbale_wifi_flag == False:
                            print("disable wifi")
                            TestBed_Services.wifi_Disable(self)
                            disbale_wifi_flag = True
                        elif a[0] == "Flipkart" and Flipkart_flag == False:
                            print("invoke Flipkart")
                            Test_Bed_Flipkart.operate_flipkart(self)
                            Flipkart_flag = True
                        elif a[0] == "Youtube" and Youtube_flag == False:
                            print("invoke Youtube and play video for:"+str(a[1])+" seconds")
                            Test_Bed_Youtube.operate_Youtube(self,dynamic_flag,a[1])
                            Youtube_flag = True
                        elif a[0] == "Wifi enable" and enable_wifi_flag == False:
                            print("enable wifi")
                            TestBed_Services.wifi_Enable(self)
                            enable_wifi_flag = True
                        elif a[0] == "Youtube Music" and Youtube_music_flag == False:
                            print("invoke Youtube Music")
                            Test_Bed_YouTubeMusic.operate_YouTubeMusic(self,dynamic_flag,a[1])
                            Youtube_music_flag = True
                        elif a[0] == "Facebook"and Facebook_flag == False:
                            print("Invoke Facebook")
                            Test_Bed_FaceBook.operate_FaceBook(self)
                            Facebook_flag = True
                        elif a[0] == "Camera" and Camera_flag == False:
                            print("Invoke Camera")
                            Test_Bed_OpenCamera_CapturePhoto.operate_Camera(self)
                            Camera_flag = True
                        elif a[0] == "Chrome" and Chrome_flag == False:
                            print("Invoke Chrome")
                            Test_Bed_Chrome_Browser.operate_Chrome_Browser(self)
                            Chrome_flag = True
                        elif a[0] == "GuardianApp" and GuardianApp_flag == False:
                            print("Invoke GuardianApp")
                            Test_Bed_Guardian.operate_Guardian(self)
                            GuardianApp_flag = True
                        elif a[0] == "Instagram" and Instagram_flag == False:
                            print("Invoke Instagram")
                            Test_Bed_Instagram.operate_Instagram(self)
                            Instagram_flag = True
                        elif a[0] == "GoggleMap" and GoggleMap_flag == False:
                            print("Invoke GoggleMap")
                            Test_Bed_GoogleMaps.operate_GoogleMaps(self)
                            GoggleMap_flag = True
                        elif a[0] == "Airplane_Mode_Enable" and Airplane_Mode_Enable_flag == False:
                            print("Invoke Airplane_Mode_Enable")
                            TestBed_Services.airplaneMode_Enable(self)
                            Airplane_Mode_Enable_flag = True
                        elif a[0] == "Airplane_Mode_Disable" and Airplane_Mode_Disable_flag == False:
                            print("Invoke Airplane_Mode_Disable")
                            TestBed_Services.airplaneMode_Disable(self)
                            Airplane_Mode_Disable_flag = True
                        elif a[0] == "Make_Call" and Make_Call_flag == False:
                            print("Invoke Mobile callinf for:"+str(a[1])+" seconds")
                            Test_Bed_MakeCall_DisconnectCall.operate_Call_on_Mobile(self,dynamic_flag,a[1])
                            Make_Call_flag = True   
                        elif a[0] == "Bluetooth_Enable" and Bluetooth_Enable_flag == False:
                            print("Invoke Bluetooth_Enable")
                            TestBed_Services.bluetooth_ON(self)
                            Bluetooth_Enable_flag = True
                        elif a[0] == "Bluetooth_Disable" and Bluetooth_Disable_flag == False: 
                            print("Invoke Bluetooth_Disable")
                            TestBed_Services.bluetooth_OFF(self)
                            Bluetooth_Disable_flag = True
                        elif a[0] == "BLEDoctor" and BLEDoctor_flag == False:
                            print("Invoke BLE-Doctor Always connected App")
                            Test_Bed_BLE_Doctor_Dexcom.launch_BLE_Doctor_Dexcom(self)
                            BLEDoctor_flag = True       
                            
                    except IndexError:
                        continue

                    try:
                        wb = xlrd.open_workbook(loc)
                        sheet = wb.sheet_by_name("Create_Dynamic_Scenarios")
                        sheet.cell_value(0, 0)
                    except Exception as e:
                        break
                    
                loop_count+=1 
                
                Dexcom_flag = False
                Amazon_flag = False
                disbale_wifi_flag = False
                Flipkart_flag = False
                enable_wifi_flag = False
                Youtube_flag = False
                Youtube_music_flag = False
                Facebook_flag = False
                Camera_flag = False
                Chrome_flag = False
                GuardianApp_flag = False
                Instagram_flag = False
                GoggleMap_flag = False
                Airplane_Mode_Enable_flag = False
                Airplane_Mode_Disable_flag = False
                Make_Call_flag = False
                End_Call_flag = False
                Bluetooth_Enable_flag = False
                Bluetooth_Disable_flag = False
                BLEDoctor_flag = False
                
                            
                if DEXCOM_TIMER == False:
                    break
                

        else:
            print("\033[91mScenario not created or doesn't exist\033[0m")
            
        

    """
    ### Method@android_testbed_setup: This method is used for setting up eneviornment/getting pre-requisties ready for running
    the test case.
    ###

    """



    def monitor_testbed_timer(self,end_time,current_process_pid):
        while True:
            if datetime.datetime.now() >= end_time:
                print("\033[91mTestbed Timer set by user is about to expire, time to collect HCI/snoop logs, post which Testbed application will exit\033[0m")
                self.android_testbed_cleanup(current_process_pid)
                break
        
            

    def android_testbed_setup(self):
        print("Starting adb server..")
        os.system("adb -s "+self.adb_id+" start-server")
        sleep(5)
        print("Starting up session")
        self.logcat_thread = Thread(target=self.logcat_fire)

        
        



    """
    ### Method@android_testbed_execute: This method is used for implementing the main logic of a worker script.
    """
        
    def android_testbed_execute(self,current_process_pid):
        if logcat_flag == "Yes":
            os.system("adb -s "+self.adb_id+" logcat -c")
            sleep(2)
            self.logcat_thread.start()
            
        self.concur = Testbed_Timer_Thread()
        
            
        if DEXCOM_TIMER == True:
            end_time = datetime.datetime.now() + datetime.timedelta(seconds=int(testbed_duration))
            application_end_time = datetime.datetime.now() + datetime.timedelta(seconds=int(testbed_duration)+240)
            self.monitor_testbed_timer_thread = Thread(target = self.monitor_testbed_timer, args=(end_time,current_process_pid,))
            self.monitor_testbed_timer_thread.start()
            print("\033[92mTestbed application is expected to expire around\033[0m", application_end_time)
            gui_logger.info("Testbed applicationis expected to expire around "+str(application_end_time))
            gui_logger.info("\n")
            gui_logger.removeHandler(gui_logger.handlers[0])
            while True:
                try:
                    print("Starting Testbed Thread .. .... .......")
                    self.concur.run(self.execute_test_bed)
                 
                    
                except KeyboardInterrupt:
                    self.concur.pause()
                    print('\n\033[91mPausing...  (Hit ENTER to continue, type quit to exit testbed.)\033[0m')
                    try:
                        response = input()
                        if response == 'quit':
                            self.android_testbed_cleanup(current_process_pid)
                            break
                        #print ('Resuming Testbed...') 
                    except KeyboardInterrupt:
                        print ('Resuming Testbed...')
                        continue
                
        if DEXCOM_TIMER == False:
            try:
                print("\033[92mTestbed will execute once\033[0m")
                gui_logger.info("Testbed will execute once")
                gui_logger.info("\n")
                gui_logger.removeHandler(gui_logger.handlers[0])
                self.execute_test_bed()
                self.android_testbed_cleanup(current_process_pid)
            except KeyboardInterrupt as e:
                print(e)
                print("\033[91mPause & Play Feature can be used only when Testbed Timer is enabled\033[0m")
                #self.execute_test_bed()
                self.android_testbed_cleanup(current_process_pid)
                
            
        
     
              

    """
    ### Method@android_testbed_cleanup: This method is used for cleaning the enviornment after test case is executed.
   
    """
    
    def android_testbed_cleanup(self,current_process_pid):  
        if HCI_flag == "Yes":
            self.Generate_HCILogs()
            print("\033[92mHCI Logs collected\033[0m")

        self.logcat_restart_handle = False
        if logcat_flag == "Yes":
            terminate_thread(self.logcat_thread)
            sleep(1)
            os.system("adb -s "+adb_id+" shell killall -2 logcat")
        sleep(0.5)
        
        print("\033[92mTestbed application to exit,cleaning up session\033[0m")
        #os.system("taskkill /F /PID "+str(current_process_pid))
        print("\033[92mSession Closed..\033[0m")
        os._exit(0)

        

    
        
    """
    ### Method@test_entry: entry point of worker class

    """
    def test_entry(self,current_process_pid):
        self.android_testbed_setup()
        self.android_testbed_execute(current_process_pid)


        
   
def appium_server_logs(port_num,adb_id):
    cmd = "appium -a 127.0.0.1 -p "+str(port_num)
    if ":" in str(adb_id):
        adb_id_rev = adb_id.split(":")
        adb_id_rev = str(adb_id_rev[0])
        appium_server_file = open("appium_server_file_"+adb_id_rev,'a')
    else:
        appium_server_file = open("appium_server_file_"+adb_id,'a')
        
    pi = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, creationflags=0x00000200)
    sleep(2)
    for i in iter(pi.stdout.readline, 'b'):
        appium_server_file.write(str(i))
        appium_server_file.write("\n")
        

def find_current_processID(processName):
    listOfProcessObjects = []
    a = []
    for proc in psutil.process_iter():
        try:
           pinfo = proc.as_dict(attrs=['pid', 'name', 'create_time'])
           if pinfo['name'] is not None:
            if processName.lower() in pinfo['name'].lower() :
               listOfProcessObjects.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess) :
            pass   
    if len(listOfProcessObjects) > 0:
       for elem in listOfProcessObjects:
           processID = elem['pid']
           a.append(processID)
           processCreationTime = elem['create_time']
           a.append(processCreationTime)
    else :
       #print('No Running Process found with given text')
       return

    print(a)
    n = 0
    maxx = -1
    for i in range(0,len(a)-1):
        if a[i+1]> maxx:
            maxx = a[i+1]
            n = i+1
            i+=2
    pid = a[n-1]
    
    return pid
        
        
def main_window():
    global DEXCOM_TIMER
    global testbed_duration
    global testbed_scenario
    global dexcom_app_type
    global logcat_flag
    global logger_flag
    global HCI_flag
    global adb_id
    global port_num
    global gui_logger
    global mobile_no

    adb_id = adb_device_id_var.get()
    port_num = appium_port_number_var.get()
    sleep(1)
    mobile_no = mobile_number_var.get()
    if ":" in adb_id:
        adb_id_rename = adb_id.split(":")
        adb_id_rename = str(adb_id_rename[0])
        gui_logger = logger("GUI_details_"+adb_id_rename+".csv",1)
    else:
        gui_logger = logger("GUI_details_"+adb_id+".csv",1)
    
    print("\033[92mADB device id entered by user is: \033[0m"+ adb_id)
    gui_logger.info("ADB device id entered by user is: "+ adb_id)
    print("\033[92mAppium port number entered by user is: \033[0m"+ port_num)
    gui_logger.info("Appium port number entered by user is: "+ port_num)   
    
    install_packages = install_packages_var.get()
    testbed_timer = testbed_timer_var.get()
    testbed_duration = duration_entry.get()
    testbed_scenario = testbed_scenario_var.get()
    dexcom_app_type = dexcomApp_var.get()
    logcat_flag = logcat_var.get()
    logger_flag = logger_var.get()
    HCI_flag = HCI_var.get()


    if var1.get() == 1:
        DEXCOM_TIMER = True
        print("\033[92mTestbed Timer is enabled\033[0m")
        gui_logger.info("Testbed Timer is enabled")
        print("\033[92mTestbed duration(in seconds)is : \033[0m" + testbed_duration)
        gui_logger.info("Testbed duration(in seconds)is : " + testbed_duration)
    else:
        DEXCOM_TIMER = False
        testbed_duration = False
        print("\033[91mTestbed timer not enabled, hence testbed will run only once\033[0m")
        print("\033[91mPause and Play Feature cannot be used here. Do not give keybaordinterrupt to pause the Testbed..!![0m")
        gui_logger.info("Testbed timer not enabled hence testbed will run only once")

    if logcat_flag == "Yes":
        print("\033[92mLogcat enabled\033[0m")
        gui_logger.info("Logcat enabled")

    if logger_flag == "All":
        print("\033[92mTestbed logger level set to 1,will log all messages/info\033[0m")
        gui_logger.info("Testbed logger level set to 1 ---> will log all messages/info")

    if logger_flag == "Warn/Error":
        print("\033[92mTestbed logger level set to 2, will log only warning and error messages\033[0m")
        gui_logger.info("Testbed logger level set to 2 ---> will log only warning and error messages")

    if HCI_flag == "Yes":
        print("\033[92mHCI/snoop log generation enabled\033[0m")
        gui_logger.info("HCI/snoop log generation enabled")

    print("\033[92mDexcom App type Chosen is: \033[0m"+ dexcom_app_type)
    gui_logger.info("Dexcom App type Chosen is: "+ dexcom_app_type)
    
    print("\033[92mTestbed Scenario Chosen is: \033[0m"+ testbed_scenario)
    gui_logger.info("Testbed Scenario Chosen is: "+ testbed_scenario)

       
    testbed_timer_var.set("")
    duration_var.set("")
    testbed_scenario_var.set("")
    root.destroy()
    #print("\033[92mstarting appium server....\033[0m")
    #appium_server_thread = Thread(target=appium_server_logs,args=(str(port_num),str(adb_id),))
    #appium_server_thread.start()
    #sleep(1) ## delay is required to let appium process start
	
    current_process_pid = find_current_processID('node')        
    #print("\033[92mCurrent Appium Process ID: \033[0m",current_process_pid)
    #if current_process_pid is None:
        #print("\033[91mAppium process ID couldn't be retrieved\033[0m")
    
    obj = android_testbed(adb_id,port_num,dexcom_app_type,testbed_scenario,logger_flag,mobile_no)
    obj.test_entry(current_process_pid)
    
    
def create_testbed_instance(adb_id,port_num,testbed_scenario,logger_flag,mobile_no):
    obj = android_testbed(adb_id,port_num,testbed_scenario,logger_flag,mobile_no)
    obj.test_entry()

    
def save_button():
    if var1.get() == 1:
        duration_entry.configure(state="enabled")
    else:
        duration_entry.configure(state="disabled")
        

def disable_button():
    duration_entry.configure(state="disabled")
        

def Test_Bed_Scenarios_Info(testbed_scenario):
    if testbed_scenario == "Scenario-1":
        messagebox.showinfo("Scenario_1", "List of Applications to be executed : \n\nLaunch_Operate Dexcom App\nLaunch Youtube\nLaunch Flipkart\nLaunchAmazon\nLaunch YouTubeMusic\nLaunch Chrome_Browser\nLaunch FaceBook\nLaunch Camera and capture photo\n\n [30 Sec Default Timer for apps like Youtube, MusicApp]")
    elif testbed_scenario == "Scenario-2":  
       messagebox.showinfo("Scenario_2", "(Dexcom app to be launched and executed only Once)\n\nList of Applications to be executed :\n\nLaunch_Operate Dexcom App\nLaunch Youtube\nLaunch Flipkart\nLaunchAmazon\nLaunch YouTubeMusic\nLaunch Chrome_Browser\nLaunch FaceBook\nLaunch Camera and capture photo\n\n [1 Hour Default Timer for apps like Youtube, MusicApp]")
    elif testbed_scenario == "Scenario-3":  
        messagebox.showinfo("Scenario_3", "List of Applications to be executed : \n\nLaunch_Operate Dexcom App\nLaunch Youtube\nLaunch Flipkart\nDisable_Wifi\nLaunch_Operate Dexcom App\nEnable_Wifi\nLaunch Amazon\nLaunch YouTubeMusic\nDisable_Wifi\nLaunch Camera and capture photo\nLaunch_Operate Dexcom App\nEnable_Wifi\nLaunch Chrome_Browser\nLaunch FaceBook\n\n [30 Mins default Timer for apps like Youtube, MusicApp]\n\n**Initial Settings: Wi-Fi Should be Enabled**") 
    elif testbed_scenario == "Scenario-4":
        messagebox.showinfo("Scenario_4", "List of Applications to be executed : \n\nLaunch_Operate Dexcom App\nLaunch Camera and capture photo\nLaunch Game\nLaunch_Operate Dexcom App\nLaunch Camera and capture photo\nLaunch Game\nLaunch Youtube\nLaunch Flipkart\nLaunch YouTube Music\nLaunch_Operate Dexcom App\nLaunch Youtube\nLaunch Flipkart\nLaunch YouTube Music\nLaunch Camera and capture photo\nLaunch Game\nLaunch_Operate Dexcom App\nLaunch Camera and capture photo\nLaunch Game\nLaunch Youtube\nLaunch Flipkart\nLaunch YouTube Music\nLaunch_Operate Dexcom App\nLaunch Youtube\nLaunch Flipkart\nLaunch YouTubeMusic\nLaunch Guardian app\n\n [30 mins Default Timer for Music app and 2 hours for YouTube]")
    
    elif testbed_scenario == "Scenario-5":
        messagebox.showinfo("Scenario_5", "List of Applications to be executed : \n\nLaunch_Operate Dexcom App\nLaunch Youtube\nLaunchFlipkart\nMake call for specified time and then disconnect\nLaunch_Operate Dexcom App\nLaunch YouTube Music\nLaunch FaceBook\nLaunch Youtube\nLaunch News Reading app\nLaunch_Operate Dexcom App\nLaunch YouTubeMusic\nLaunch Amazon\nLaunch YouTubeMusic\nLaunch Youtube \nLaunch_Operate Dexcom App\nMake call for specified time and then disconnect\nLaunch Youtube\nLaunch Instagram\nLaunch YouTubeMusic\nLaunch Maps\nLaunch News Reading app\n\n [1 hour 30 mins Default Timer for apps like Youtube, Music app and 30 mins for Calling on mobile number}\n\n Note**Preferred/Default Calling should be set to any one sim for devices with Dual sim cards")
    
    elif testbed_scenario == "Scenario-6":
        messagebox.showinfo("Scenario_6", "List of Applications to be executed : \n\nLaunch_Operate Dexcom App\nLaunch Youtube\nLaunch Camera and capture photo\nLaunch YouTube Music\nLaunch FaceBook\nLaunch Youtube\nLaunch Maps\nLaunch Youtube\nLaunch Instagram\nLaunch Youtube\nLaunch Maps\nLaunch Youtube\nLaunch Instagram\nLaunch YouTubeMusic\nLaunch Maps\nLaunch Youtube\nLaunch FaceBook\nLaunch Youtube\nLaunch Camera and capture photo\nLaunch Youtube\nLaunch Maps\nLaunch Youtube\nLaunch Maps\nLaunch YouTubeMusic\nLaunch FaceBook\nLaunch Youtube\nLaunch Maps\nLaunch Youtube\nLaunch Instagram\nLaunch Youtube\nLaunch Maps\nLaunch Youtube\n\n [10 mins Default Timer for apps like Youtube, Music]")
    
    elif testbed_scenario == "Scenario-7":  
        messagebox.showinfo("Scenario_7", "List of Applications to be executed : \n\nLaunch_Operate Dexcom App\nOpen/Edit settings_alerts \nEnable Aliplane Mode\nEnable Bluetooth\nLaunch_Operate Dexcom App\nLaunch Youtube and play video from Downloads\nLaunch Maps\Open Camera and take photos\n\n Open Settings and navigate\n Open Contacts and navigate \nDisable Aliplane Mode\nDelete g6_Alerts[60 mins Default Timer for apps like Youtube]") 
    

if __name__ == '__main__':
    root=tk.Tk()
    root.title("Android Appium Testbed Application 1.0.0")
    root.geometry("820x550")  # W*H
    root.resizable(0,0)
    tabControl = ttk.Notebook(root)
    global duration_entry
    global var
    var = tk.StringVar()
    style = Style(root)
    style.configure("TCheckbutton", focuscolor=style.configure(".")["background"],font = ("calibre", 10, "bold"))

    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)

    tabControl.add(tab1, text ='Device Configurations')
    tabControl.add(tab2, text ='Application Configurations')
    tabControl.pack(expand = 2, fill ="both")
    
    label_frame = LabelFrame(tab1, relief='groove',width=550,height=150)
    label_frame.pack(side='top', pady=20)
    label_frameTop = LabelFrame(tab2, relief='groove',width=480,height=110)
    label_frameTop.pack(side='top', pady=20)
    label_frameMiddle = LabelFrame(tab2, relief='groove',width=750,height=250 )
    label_frameMiddle.pack(side='top')
    
    adb_device_id_var = tk.StringVar()
    appium_port_number_var = tk.StringVar()
    mobile_number_var = tk.StringVar()
    
    install_packages_var = tk.StringVar()
    testbed_timer_var=tk.StringVar()
    duration_var=tk.StringVar()
    testbed_scenario_var = tk.StringVar()
    dexcomApp_var = tk.StringVar()
    logcat_var = tk.StringVar()
    logger_var = tk.StringVar()
    HCI_var = tk.StringVar()


    option_scenarios = [
        "Scenario-1",
        "Scenario-1",
        "Scenario-2",
        "Scenario-3",
        "Scenario-4",
        "Scenario-5",
        "Scenario-6",
	"Scenario-7",
        "Dynamic"
    ]

    options_testbedtimer = [
        "disable",
        "disable",
        "enable"
    ]

    option_boolean = [
        "Yes",
        "No",
        "Yes"
    ]

    option_verbose = [
        "All",
        "All",
        "Warn/Error"
    ]

    option_dexcom_app_type = [
        "G6",
        "G6",
        "G7",
        "Always Connected"
    ]


    adb_device_id_var.set("")
    appium_port_number_var.set("4723")
    mobile_number_var.set("Enter Phone Number")
    duration_var.set("3600")
    editor_text = tk.Text(tab2, bd=0, bg="white", fg="black", highlightthickness = 0, borderwidth=0)
    editor_text.config(highlightthickness = 0, borderwidth=0)


    adb_label = ttk.Label(tab1, text = 'Enter adb device id', font=('calibre',10, 'bold'))
    adb_entry = ttk.Entry(tab1, textvariable = adb_device_id_var, font = ('calibre',10,'normal'))
    appium_label = ttk.Label(tab1, text = 'Enter appium port number', font=('calibre',10, 'bold'))
    appium_entry = ttk.Entry(tab1, textvariable = appium_port_number_var, font = ('calibre',10,'normal'))

    
    dur_label = ttk.Label(tab2, text = '( in seconds )', font = ('calibre',10,'bold'))
    duration_entry=ttk.Entry(tab2, textvariable = duration_var, font = ('calibre',10,'normal'))
    duration_entry.configure(state="disabled")
    var1 = tk.IntVar()
    c1 = ttk.Checkbutton(tab2, text='Enable Test-Bed Timer',variable=var1, onvalue=1, offvalue=0, takefocus=False,command=save_button)
    c1.place(x=180, y=60)
    scene_label = ttk.Label(tab2, text = 'Choose Testbed Scenario', font=('calibre',10, 'bold'))
    scene_entry = ttk.OptionMenu(tab2,testbed_scenario_var, *option_scenarios,command = Test_Bed_Scenarios_Info)
    dexcomApp_label = ttk.Label(tab2, text = 'Choose Dexcom App Type', font=('calibre',10, 'bold'))
    dexcomApp_entry = ttk.OptionMenu(tab2,dexcomApp_var, *option_dexcom_app_type)
    logcat_label = ttk.Label(tab2, text = 'Enable Logcat logging', font=('calibre',10, 'bold'))
    logcat_entry = ttk.OptionMenu(tab2,logcat_var, *option_boolean)
    logger_label = ttk.Label(tab2, text = 'Set Logger Level', font=('calibre',10, 'bold'))
    logger_entry = ttk.OptionMenu(tab2,logger_var, *option_verbose)
    HCI_label = ttk.Label(tab2, text = 'Generate HCI/Snoop log', font=('calibre',10, 'bold'))
    HCI_entry = ttk.OptionMenu(tab2,HCI_var, *option_boolean)
    
    MobileNo_label = ttk.Label(tab2, text = 'Enter Mobile number', font=('calibre',10, 'bold'))
    MobileNo_entry = ttk.Entry(tab2, textvariable = mobile_number_var, font = ('calibre',10,'normal'))
    
    Note_label = ttk.Label(tab2, text = '** Note: Make sure the all mobile apps which are part of Test-Bed are pre installed and logged in before \
starting the Execution.\n { Dexcom G6 App(Warm-up Completed), YouTube, Flipkart, Amazon, Facebook, Chrome, YouTube Music etc. }', font=('calibre',10, 'bold'),foreground="dark red")    
    sub_btn=tk.Button(tab2, text = 'Submit', relief='raised', command = main_window, width=20)
    

    #Tab 1
    adb_label.place(x=200, y=50)
    adb_entry.place(x=400, y=50)
    appium_label.place(x=200, y=110)
    appium_entry.place(x=400, y=110)
    
    #Tab 2
    dur_label.place(x=350, y=60)
    duration_entry.place(x=450, y=60)
    dexcomApp_label.place(x=50,y=190)
    dexcomApp_entry.place(x=230,y=190)
    scene_label.place(x=400, y=190)
    scene_entry.place(x=600, y=190)
    logcat_label.place(x=400, y=250)
    logcat_entry.place(x=600, y=250)
    logger_label.place(x=50, y=250)
    logger_entry.place(x=230, y=250)
    HCI_label.place(x=400, y=310)
    HCI_entry.place(x=600, y=310)
    MobileNo_label.place(x=50, y=310)
    MobileNo_entry.place(x=220, y=310)
    sub_btn.place(x=320, y=360)
    Note_label.place(x=15, y=450)


    root.mainloop()

    
