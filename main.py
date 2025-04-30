import os
import time
import requests
import tkinter as tk  # 导入tkinter模块。为了方便后续讲解，命名为 tk。
from tkinter import messagebox  # 引入弹窗库，防止解释器弹出报错。
from tkinter import filedialog
import json
import hashlib
import zipfile
from shutil import move
#import sys
from shutil import  rmtree
#import subprocess
root = tk.Tk()
root.withdraw()
def choose_path():
    f_path = filedialog.askopenfilename()
    return f_path
def ask_messagebox(mess): 
    print(mess)
    input()
    ret=messagebox.askyesno(title='LCTA',message=mess)
    return ret
def display_messagebox(mess): 
	messagebox.showinfo(title='LCTA',message=mess)
def download_tran(ret,config):
    try:os.remove(os.path.expanduser("~")+'\.LCTA\download.zip')
    except:None
    try:os.remove(os.path.expanduser("~")+'\.LCTA\\'+ret[1])
    except:None
    try:
        while True:
            #print(ret[11])
            #exit()
            while True:
                try:
                    file_get=requests.get(ret[11])
                    break
                except:
                    if not ask_messagebox('下载失败，是否重新下载'):
                        os.startfile(r"true.exe")
                        os._exit(0)
            file_get=file_get.content
            #md5ing=file_get.read()
            md5=hashlib.md5(file_get).hexdigest()
            if not md5==ret[13]:
                if not ask_messagebox('下载失败，是否重新下载'):
                    os.startfile(r"true.exe")
                    os._exit(0)
            else:break
        with open(os.path.expanduser("~")+'\.LCTA\download.zip','wb') as f:
            f.write(file_get)
    except:
        try:
            if not ask_messagebox('直链方案失败，是否启用手动下载'):
                os.startfile(r"true.exe")
                os._exit(0)
            else:
                try:
                    if not config['download_path']:
                        if ask_messagebox("暂未定义下载路径,现在选择?否将使用系统默认路径"):
                            config['download_path']=choose_path()
                            download_path=config['download_path']
                        else:
                            if ret[3]:
                                download_path=os.path.join(os.path.expanduser("~"), 'Downloads',ret[3])
                            else:
                                display_messagebox('获取路径错误')
                                os.startfile(r"true.exe")
                                os._exit(0)
                    else:
                        download_path=config['download_path']
                    os.remove(download_path+'\\'+ret[1])
                except:None
                display_messagebox('请手动下载至下载文件夹')
                os.system('start '+ret[9])
                while True:
                    time.sleep(3)
                    if os.path.exists(download_path+'\\'+ret[7]):
                        os.rename(download_path+'\\'+ret[7],download_path+'\\'+'download.zip')
                        move(download_path+'\\'+'download.zip',os.path.expanduser("~")+'\.LCTA\download.zip')
                        break
        except:
            display_messagebox('未知错误，直接启动llc')
            os.startfile(r"true.exe")
            os._exit(0)
    return config
def install_tran(ret,config):
    try:retconfig=download_tran(ret,config)
    except:
        display_messagebox('未知错误，直接启动')
        os.startfile(r"true.exe")
        os._exit(0)
    try:rmtree(r'LimbusCompany_Data\\lang'+"\\"+ret[1])
    except:None
    try:
        with zipfile.ZipFile(os.path.expanduser("~")+'\.LCTA\download.zip', 'r') as zip_ref:
            zip_ref.extractall(r'LimbusCompany_Data\\lang')
    except:
        display_messagebox('解压失败，直接启动')
        os.startfile(r"true.exe")
        os._exit(0)
    try:os.remove(r'LimbusCompany_Data\\lang'+"\\"+"config.json")
    except:None
    config_lang={
        "lang": "LCTA_CN",
        "titleFont": "",
        "contextFont": ""
    }
    with open(r'LimbusCompany_Data\\lang'+"\\"+"config.json",'w') as file:
        json.dump(config_lang,file,ensure_ascii=False,indent=4)
    with open(os.path.expanduser("~")+'\.LCTA\config.json','w') as file:
        json.dump(retconfig,file,ensure_ascii=False,indent=4)
if __name__=='__main__':
    try:
        input()
        try:ret=requests.post('https://api.textdb.online/'+'保护').text
        #为保护网址不受修改隐去内容
        except:
            os.startfile(r"true.exe")
            os._exit(0)
        ret=ret.split('\n')
        if not os.path.exists(os.path.expanduser("~")+'\.LCTA'):
            os.mkdir(os.path.expanduser("~")+'\.LCTA')
        if not os.path.exists(os.path.expanduser("~")+'\.LCTA\config.json'):
            if ask_messagebox("未找到配置文件，是否要创建配置文件？"):
                rite={
                    "llc_name":ret[1],
                    "running":False,
                    "download_path":""
                }
                with open(os.path.expanduser("~")+'\.LCTA\config.json','w') as file:
                    json.dump(rite,file,ensure_ascii=False,indent=4)
            else:
                os.startfile(r"true.exe")
                os._exit(0)
    except:
        display_messagebox("启动错误，直接打开llc")
        os.startfile(r"true.exe")
        os._exit(0)
    try:
        with open(os.path.expanduser("~")+'\.LCTA\config.json','r',encoding='utf-8') as file:
            config=json.load(file)
        if not os.path.exists(r'LimbusCompany_Data\\lang\\'):
            if ask_messagebox("未找到lang目录，是否要创建目录并下载汉化包？"):
                os.mkdir(r'LimbusCompany_Data\\lang')
                install_tran(ret,config)
        elif not os.path.exists(r'LimbusCompany_Data\\lang'+"\\"+ret[1]):
            if ask_messagebox("未找到汉化包，是否要下载汉化包？"):
                install_tran(ret,config)
        elif not os.path.exists(r'LimbusCompany_Data\\lang'+"\\"+ret[1]+"\\ver.txt"):
            if ask_messagebox("汉化包已存在，但未找到ver.txt，是否要重新下载汉化包？否将写入当前版本号"):
                install_tran(ret,config)
            else:
                with open(r'LimbusCompany_Data\\lang'+"\\"+ret[1]+r"\\ver.txt",'w') as file:
                    file.write(ret[5])
        else:
            with open(r'LimbusCompany_Data\\lang'+"\\"+ret[1]+r"\\ver.txt",'r') as file:
                ver=file.readline()
                #print(ver)
                #input()
            if not ver==ret[5]:
                install_tran(ret,config)
        os.startfile(r"true.exe")
        os._exit(0)
    except:
        display_messagebox("未知错误，直接打开llc")
        os.startfile(r"true.exe")
        os._exit(0)
#if __name__=='__main__' and sys.argv[0]=="LimbusCompany_for.exe":
#    display_messagebox("程序bug")
#    os.startfile(r"true.exe")