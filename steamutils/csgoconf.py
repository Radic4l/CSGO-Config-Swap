#!/usr/bin/env python
#! -*- coding: utf-8 -*-

"""
    Implémentation du module de manipulation
    des fichiers de configurations des profils
    steam existant.

    @author: Radic4l
"""

import time
import os

__author__ = 'Radic4l'
__version__ = '0.0.1'
__all__ = ['getConf']

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'

class getConf:

    def profile(self):
        """
            Implémentation servant à retourner
            certaines information concernant
            le profile csgo concernant les configurations

        :param self: Url d'un dossier de profile steam
        :return: Dictionnaire d'informations sur le profile cible

        Usage:

            >>> import steamutils
            >>> steamutils.getConf('e:/program files (x86)/steam/userdata/95148732')
        """

        path = self + '/730/local/cfg/config.cfg'
        path = path.replace('/', '\\' + '\\')
        final_dict = {}
        if os.path.isfile(path):
            # Get file's Last modification timestamp only in terms of seconds since epoch
            modTimesinceEpoc = os.path.getmtime(path)
            # Convert seconds since epoch to readable timestamp
            modificationTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(modTimesinceEpoc))
            openConfigFile = open(path, 'r', encoding='utf8')
            readConfigFile = openConfigFile.read()
            splited_config = readConfigFile.split("\n")

            for lines in splited_config:
                values = lines.split(' ')
                # print(values)
                if 'name' in values:
                    values.remove('name')
                    cleanValues = " ".join(values)
                    dic = {
                        'name': cleanValues.replace('"', ''),
                        'pathConfig': path.replace('\\\\', '\\'),
                        'pathFolder': self + '/730',
                        'update': modificationTime
                    }
                    final_dict[self.split('/')[-1]] = dic

            openConfigFile.close()
            return final_dict
            # return path
        else:
            return f'Error path : {path}'


    def profiles (self):
        final_dict = {}
        # print(f"{bcolors.WARNING}[i] SELF VARIABLE : {profiles}{bcolors.ENDC}")
        for p in self:
            print(f"{bcolors.WARNING}[i] VALUE FROM for p : {p}{bcolors.ENDC}")
            path = p + '/730/local/cfg/config.cfg'
            path = path.replace('/', '\\' + '\\')
            print(f"{bcolors.OKBLUE}[.] Analizing path : {path} ...{bcolors.ENDC}")
            if os.path.isfile(path):
                print(f"{bcolors.OKGREEN}[+] Path is OK adding profile informations ...{bcolors.ENDC}")
                # Get file's Last modification timestamp only in terms of seconds since epoch
                modTimesinceEpoc = os.path.getmtime(path)
                # Convert seconds since epoch to readable timestamp
                modificationTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(modTimesinceEpoc))
                openConfigFile = open(path, 'r', encoding='utf8')
                readConfigFile = openConfigFile.read()
                splited_config = readConfigFile.split("\n")

                for lines in splited_config:
                    values = lines.split(' ')
                    # print(values)
                    if 'name' in values:
                        values.remove('name')
                        cleanValues = " ".join(values)
                        dic = {
                            'name': cleanValues.replace('"', ''),
                            'pathConfig': path.replace('\\\\', '\\'),
                            'pathFolder': p + '/730',
                            'update': modificationTime
                        }
                        final_dict[p.split('/')[-1]] = dic
                openConfigFile.close()
            else :
                print(f"{bcolors.FAIL}[!] No Config file found for : {p}{bcolors.ENDC}")
            print("\n")
        return final_dict
            # else:
            #     return f'Error path : {path}'