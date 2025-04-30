import os
from win32gui import ShowWindow,FindWindow,IsWindow,SendMessage
import win32con
from win32process import GetWindowThreadProcessId
from psutil import Process
from time import sleep
from fix import *
#from tkinter.messagebox import askyesno
#def ask_messagebox(mess): 
#    ret=askyesno(title='LCTA',message=mess)
#    return ret
if not os.path.exists(os.path.expanduser("~")+'\.LCTA\\running_true'):
    open(os.path.expanduser("~")+'\.LCTA\\running_true','x') 	# 创建空文件
else:
    a= FindWindow(None, "LimbusCompany")
    if a:
        os._exit(0)
    else:
        fixs()
        os._exit(0)
def rename_back():
    if os.path.exists("LimbusCompany_for.exe"):
        os.rename("LimbusCompany.exe", "LimbusCompany_true.exe")
        os.rename("LimbusCompany_for.exe", "LimbusCompany.exe")
if (not os.path.exists("LimbusCompany_for.exe")) and (os.path.exists("LimbusCompany_true.exe")):
    os.rename("LimbusCompany.exe", "LimbusCompany_for.exe")
    os.rename("LimbusCompany_true.exe", "LimbusCompany.exe")
    #os.startfile("LimbusCompany.exe")
    #os.system('start \"'+os.getcwd()+'\\LimbusCompany.exe\"')
    os.system('start LimbusCompany.exe')
elif os.path.exists("LimbusCompany_backup.exe") and os.path.exists("LimbusCompany_LCTA.exe"):
    fixs()

while True:
    sleep(5)
    handle = FindWindow(None, "LimbusCompany")
    if not handle:
        rename_back()
        os._exit(0)
    hread_id, process_id = GetWindowThreadProcessId(handle)   
    p_bin = Process(process_id).exe()   
    di=(os.path.dirname(p_bin))
    if di==os.getcwd():
        break
    else:
    #ShowWindow(handle, win32con.SW_MAXIMIZE)
        SendMessage(handle,win32con.WM_CLOSE)
while True:
    sleep(20)
    V = IsWindow(handle)
    if not V:
        rename_back()
        if os.path.exists(os.path.expanduser("~")+'\.LCTA\\running_true'):
            dell(os.path.expanduser("~")+'\.LCTA\\running_true')
        os._exit(0)
#计算机\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Steam App 1973530



#os.rename("LimbusCompany.exe", "LimbusCompany_true.exe")
#os.rename("LimbusCompany_for.exe", "LimbusCompany.exe")