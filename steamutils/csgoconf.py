#!/usr/bin/env python
#! -*- coding: utf-8 -*-

"""

    @author: Radic4l
"""

import time
import os

__author__ = 'Radic4l'
__version__ = '0.0.1'
__all__ = ['getConf']


def getConf(self):
    path = self+'/730/local/cfg/config.cfg'
    path = path.replace('/','\\'+'\\')
    finalDic = {}
    if os.path.isfile(path):
        # Get file's Last modification timestamp only in terms of seconds since epoch
        modTimesinceEpoc = os.path.getmtime(path)
        # Convert seconds since epoch to readable timestamp
        modificationTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(modTimesinceEpoc))
        openConfigFile = open(path, 'r',encoding='utf8')
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
                    'pathConfig': path,
                    'pathFolder': self + '/730',
                    'update': modificationTime
                }
                finalDic[self.split('/')[-1]] = dic

        openConfigFile.close()
        return finalDic
        # return path
    else:
        return f'Error path : {path}'
