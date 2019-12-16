#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Application pour echanger les differentes configurations
    de Counter Strike : Global Offensive entre
    les différents profiles utilisateurs steam

    @Author : Radic4l
"""

__author__ = 'Radic4l'
__version__ = '0.0.1'


import steamutils

if __name__ == '__main__':
    profilesListe = steamutils.getProfilesPath(steamutils.steamPath())
    print(profilesListe)
    print(steamutils.getConf(profilesListe[6]))