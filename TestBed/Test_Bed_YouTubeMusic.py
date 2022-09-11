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





class Test_Bed_YouTubeMusic(Common_Utilities):
    def __init__(self):
        pass



    def operate_YouTubeMusic(self,dynamic_flag,dynamic_music_play_time):
        youtubemusic_csv_log_path = os.path.join(self.logger_csv_path,"YouTubeMusic_log.csv")
        lgr_handle = logger(youtubemusic_csv_log_path,self.config_params.get("debug_level"))
        print("-------------------------------------")
        print("YouTubeMusic App is opened")
        print("-------------------------------------")
        os.system("adb -s "+self.adb_id+" shell am start -n com.google.android.apps.youtube.music/com.google.android.apps.youtube.music.activities.MusicActivity")
        lgr_handle.info("\n")
        lgr_handle.info("YouTubeMusic App is opened")
        sleep(2)
        try:
            #Click on Search 
            print("Click on Search")
            lgr_handle.info("Click on Search")
            #Search icon 
            self.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='Search']").click()
            print("Enter Song name ")
            lgr_handle.info("Entering Song on Youtube Music")
            #self.driver.find_element_by_xpath(".//android.widget.EditText").clear()
            songVal=self.config_params.get("Music_Search")
            self.driver.find_element_by_xpath(".//android.widget.EditText").send_keys(songVal)
            sleep(3)
            self.Press_Enter_MobileKeyBoard()
            sleep(2)
            print("Click on song")
            self.driver.find_element_by_id("com.google.android.apps.youtube.music:id/contextual_menu_anchor").click()
            sleep(2)
            self.driver.find_element_by_id("com.google.android.apps.youtube.music:id/text").click()
            print("Clicked on Play Button")
            lgr_handle.info("Clicked on Play Button on YouTube Music")
            
            #WAIT FOR SOME TIME TO PLAY MUSIC
            if dynamic_flag == True:
                timeOut = dynamic_music_play_time
            else:
                timeOut=self.config_params.get("Music_Timer")
            print("Music will Start playing, song searched as '"+songVal+"'"+" will be played for '"+str(timeOut)+"' seconds")
            lgr_handle.info("Music will Start playing, song searched as '"+songVal+"'"+" will be played for '"+str(timeOut)+"' seconds")
            sleep(timeOut)
            print("Click on Stop/Pause Button")
            lgr_handle.info("Click on Stop/Pause Button on YouTube Music")
            #self.Press_Play_Button(self)
            self.driver.find_element_by_id("com.google.android.apps.youtube.music:id/player_control_play_pause_replay_button").click() 
            
            sleep(2)
            print("Press Device BackButton")
            lgr_handle.info("Press Back Button")
            self.Press_Device_BackButton()
            self.Press_Device_BackButton()
            self.Press_Device_BackButton()
            sleep(2)
            self.driver.find_element_by_xpath(".//android.widget.TextView[@text='Home']").click()
            print("Played Music on YouTubeMusic, song searched as '"+songVal+"'"+" played for '"+str(timeOut)+"' seconds")
            lgr_handle.info("Played Music on YouTubeMusic, song searched as '"+songVal+"'"+" for '"+str(timeOut)+"' seconds")
            lgr_handle.info("Exit: YouTubeMusic")
            print("Exit: YouTubeMusic") 
            print("____________________________________________________________________\n")            
            for i in range(0,2):
                self.Press_Device_BackButton()
                sleep(0.2)
                i+=1
            lgr_handle.removeHandler(lgr_handle.handlers[0])

                
        except Exception as e:
            print(str(e))
            print(type(e))
            lgr_handle.warn(e)
            print("**Test_Bed_YouTubeMusic**")
            lgr_handle.warn("**Test_Bed_YouTubeMusic**")
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
           
            

