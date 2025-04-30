import os
import shutil
def dell(file_name):
    try:
        os.remove(file_name)
    except:
        pass
def fixs():
    dell('LimbusCompany.exe')
    dell('LimbusCompany_for.exe')
    dell('LimbusCompany_true.exe')
    dell(os.path.expanduser("~")+'\.LCTA\\running_true')
    shutil.copyfile('LimbusCompany_backup.exe','LimbusCompany_true.exe')
    shutil.copyfile('LimbusCompany_LCTA.exe','LimbusCompany.exe')
if __name__ == '__main__':
    fixs()