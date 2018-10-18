import sys
from cx_Freeze import setup, Executable
import datetime,os,json,sys,webbrowser,calendar
import bangumiInfoHandler,bangumiSystemTray,config,content,mainWindow,perBangumiEl,timeNowLabel,timeOpreat,timeTodayLabel


# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {'packages': [], 'excludes': []}

setup(  name = '追番桌面工具',
        version = '0.9',
        description = '追番工具',
        options = {'build_exe': build_exe_options},
        executables = [Executable('bangumi.py')])
