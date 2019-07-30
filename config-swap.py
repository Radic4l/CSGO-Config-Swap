#!/usr/bin/env python 
#-*- coding: utf-8 -*-
import os
import pathlib
import shutil
import easygui
import json
import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'


def findDrive():
    '''
    -> Vérification des disques existants
        => Retourne un tableau contenant les disques existant
    '''
    driveLetterList = ['A:','D:','C:','E:','B:','F:','G:','H:','I:','J:','K:','L:','M:','N:','O:','P:','Q:','R:','S:','T:','U:','V:','W:','X:','Y:','Z:']
    existingDrives = []
    nbDrives = 0
    for letter in driveLetterList:
        try:
            disk = pathlib.Path(letter)
            print("Checking existing drive ... "+bcolors.HEADER+"{0}".format(letter)+bcolors.ENDC+" -> ", end="", flush=True)
            time.sleep(0.05)
            if disk.exists() == True:
                print(bcolors.OKGREEN+"{0}".format(disk.exists())+bcolors.ENDC)
                existingDrives.append(letter)
                nbDrives = nbDrives + 1
            else:
                print(bcolors.FAIL+"{0}".format(disk.exists())+bcolors.ENDC)
        except WindowsError:
            print(bcolors.FAIL+'Permission Denied'+bcolors.ENDC)
            continue
    print(bcolors.OKBLUE+'{0} drive(s) up {1}'.format(nbDrives, existingDrives)+bcolors.ENDC)
    time.sleep(0.5)
    return existingDrives

def locateSteamFolder(self):
    '''
    -> Localise l'emplacement de steam sur les disques existants
        => Retourne l'emplacement (path) de steam
     
     NB: Ajouter dans un tableau la valeur de existingPath
     a chaque boucle si a la fin le table ne contient que false
     alors demander à l'utilisateur de rentrer le path en input
    '''
    existingTabs = {}
    for letter in self:
        path = letter + '\\Program Files (x86)\\Steam\\userdata'
        existingPath = pathlib.Path(path).exists()
        if existingPath == True:
            existingTabs[existingPath] = path
        elif existingPath == False:
            existingTabs[existingPath] = path
            #exist = pathlib.Path(path).exists()
    # print(bcolors.BOLD+"Dictionnaire des path sur disque : {}".format(existingTabs)+bcolors.ENDC)
    if True in existingTabs:
        return existingTabs[True]
    else:
        path = easygui.diropenbox() + '\\userdata'
        return path

def findUserFolder ():
    '''
    -> vérifie l'éxistance du dossier CSGO 
        -> # L'id du dossier csgo et le 730
    -> créer un json des profile avec différentes cles
        => Numéros de dossier utilisateur : name, pathConfig, pathFolder, update
        => retourne le dictionnaire # json_loaded
    '''
    finalDic = {}
    for x in os.listdir(steamUserdataPath):
        exists = os.path.isfile(steamUserdataPath + '\\' + x + '\\730\\local\\cfg\\config.cfg')
        if exists:
            configFilePath = steamUserdataPath + '\\' + x + '\\730\\local\\cfg\\config.cfg'

            # Get file's Last modification time stamp only in terms of seconds since epoch
            modTimesinceEpoc = os.path.getmtime(configFilePath)
            # Convert seconds since epoch to readable timestamp
            modificationTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(modTimesinceEpoc))
            # print('config file found on profile folder ' + x)
            openConfigFile = open(configFilePath,'r',
                                    encoding='utf8')
            readConfigFile = openConfigFile.read()
            splited_config = readConfigFile.split("\n")
            time.sleep(0.5)
            for lines in splited_config:
                values = lines.split(' ')
                # print(values)
                if 'name' in values:
                    values.remove('name')
                    cleanValues = " ".join(values)
                    dic = {
                        'name':cleanValues.replace('"',''),
                        'pathConfig':configFilePath,
                        'pathFolder': steamUserdataPath + '\\' + x + '\\730',
                        'update':modificationTime
                    }
                    finalDic[x] = dic
                    print(bcolors.OKGREEN+'We found settings of ' + cleanValues + ' account from ' + x + ' Last modified at : ' + modificationTime+bcolors.ENDC)
                    time.sleep(0.5)
                    openConfigFile.close()
                else:
                    continue
        else:
            print(bcolors.FAIL+'No config file on '+x+bcolors.ENDC)
            time.sleep(0.5)
            continue
    json_conf = json.dumps(finalDic, sort_keys=True, indent=4) # convertie le dictionnaire en string
    #print(bcolors.OKBLUE+'The Final Dict is : {}'.format(finalDic)+bcolors.ENDC)
    #print(type(finalDic))
    #print(bcolors.HEADER+'JSON FILE :'+bcolors.ENDC)    
    #time.sleep(1)
    #print(json_conf)
    #print(type(json_conf))
    json_loaded = json.loads(json_conf) # retransforme le type(str) en dictionnaire
    #print(json_loaded['72453270']['name'])
    #print(type(json_loaded))
    return json_loaded
    
def backupConfigFile ():
    '''
    -> Retire le dossier de configuration csgo du profile cible
    -> Créer un backup du dossier de configuration
    '''
    timeTest = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime())
    print(timeTest)
    #if os.path.isdir() == False:
     #   pass
        # os.mkdir("E:\\Program Files (x86)\\Steam\\userdata\\29832948\\730\\local\\cfg-Backup")
        # os.rename("E:\\Program Files (x86)\\Steam\\userdata\\29832948\\730\\local\\cfg\\config.cfg", "E:\\Program Files (x86)\\Steam\\userdata\\29832948\\730\\local\\cfg-Backup\\config-{0}.cfg".format(timeTest))
        # pass


if __name__ == '__main__':

    drives = findDrive() # tableau des disques existants
    steamUserdataPath = locateSteamFolder(drives)
    print('Print de steamUserdataPath : '+steamUserdataPath+' = {0}'.format(type(steamUserdataPath)))
    test = findUserFolder()
    print(test)
    len(test)
    for key,value in test.items():
        print('=' * len(str(value)))
        print(key)
        print(str(value))
        time.sleep(0.5)
    backupConfigFile()