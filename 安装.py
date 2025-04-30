import sys
import os
import winreg
import os
import tkinter as tk
from tkinter import filedialog
import shutil
#import subprocess
root = tk.Tk()
root.withdraw()
import getpass
from win32com.client import Dispatch

def create_systemc_start(lnk_name, exe_abs_path):
    '''
    :param lnk_name: 快捷方式名称
    :param exe_abs_path:  要创建的exe绝对路径
    :return: 
    '''
    
    startup_path = fr'C:\Users\{getpass.getuser()}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'
    start_list = os.listdir(startup_path)

    if lnk_name not in start_list:
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(os.path.join(startup_path, lnk_name))
        shortcut.Targetpath = exe_abs_path
        shortcut.save()

def rename(a,b):
    try:
        os.rename(a, b)
    except:pass
def remove(path):
    try:
        os.remove(path)
    except:pass
def choose_path():
    f_path = filedialog.askopenfilename()
    return f_path
def add_to_startup(name,file_path=""):
	#By IvanHanloth
    if file_path == "":
        file_path = os.path.realpath(sys.argv[0])
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run",winreg.KEY_SET_VALUE, winreg.KEY_ALL_ACCESS|winreg.KEY_WRITE|winreg.KEY_CREATE_SUB_KEY)#By IvanHanloth
    winreg.SetValueEx(key, name, 0, winreg.REG_SZ, file_path)
    winreg.CloseKey(key)

def remove_from_startup(name):
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run", winreg.KEY_SET_VALUE, winreg.KEY_ALL_ACCESS|winreg.KEY_WRITE|winreg.KEY_CREATE_SUB_KEY)#By IvanHanloth
    try:
        winreg.DeleteValue(key, name)
    except FileNotFoundError:
        print(f"{name} not found in startup.")
    else:
        print(f"{name} removed from startup.")
    winreg.CloseKey(key)
b=input('进行安装还是卸载 (i/u)')
if b=='i':
    exe_name=""
    while not exe_name=="LimbusCompany.exe":
        path_little=choose_path()
        name_list=path_little.split("/")
        exe_name=name_list[-1]
        if not exe_name=="LimbusCompany.exe":
            print("内容错误")
    path_little=path_little[:-17]
    path_now=os.getcwd()
    shutil.copyfile(path_now+'\\fix.exe',path_little+'fix.exe')
    shutil.copyfile(path_now+'\\true.exe',path_little+'true.exe')
    shutil.copyfile(path_now+'\\main.exe',path_little+'main.exe')
    rename(path_little+'main.exe',path_little+'LimbusCompany_LCTA.exe')
    shutil.copyfile(path_little+'LimbusCompany.exe',path_little+'LimbusCompany_backup.exe')
    rename(path_little+'LimbusCompany.exe',path_little+'LimbusCompany_true.exe')
    shutil.copyfile(path_little+'LimbusCompany_LCTA.exe',path_little+'LimbusCompany.exe')
    #os.startfile(path_little+"fix.exe")
    #process = subprocess.Popen(path_little+"fix.exe")
    #add_to_startup('LCTA_fix'i,path_little+'fix.exe')
elif b=='u':
    #remove_from_startup('LCTA_fix')
    exe_name=""
    while not exe_name=="LimbusCompany.exe":
        path_little=choose_path()
        name_list=path_little.split("/")
        exe_name=name_list[-1]
        if not exe_name=="LimbusCompany.exe":
            print("内容错误")
    path_little=path_little[:-17]
    #if os.path.exists(path_little+'\\fix.exe'):
    #    os.startfile(path_little+"fix.exe")
    remove(path_little+'fix.exe')
    remove(path_little+'true.exe')
    remove(path_little+'LimbusCompany.exe')
    remove(path_little+'LimbusCompany_true.exe')
    remove(path_little+'LimbusCompany_LCTA.exe')
    os.rename(path_little+'LimbusCompany_backup.exe',path_little+'LimbusCompany.exe')
else :
    print('错误')