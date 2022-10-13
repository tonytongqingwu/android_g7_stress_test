# android_g7_stress_test

## Source code:
The repo is ONLY modified to remove windows PC support for Mac. 

https://github.com/dexcom-inc/TestBed_Android_Python/tags

1. Random run poplular apps on Android device.
2. Check G7 app and capture screen.

## How to run: 
1. From home folder, run `pip3 install -r requirements.txt`
3. Connect device and find `adb devices` output for adb id
4. Run
`python3 Dexcom_Android_Testbed.py` 
4. Enter adb id, and go to application tab, just click submit button.

NOTE: if you have issue of tk error, just run

`brew install python-tk`

## Plan: will be replaced by VnV own apython package:

https://github.com/tonytongqingwu/apython
