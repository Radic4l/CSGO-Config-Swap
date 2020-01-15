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
import json

if __name__ == '__main__':
    profilesListe = steamutils.getProfilesPath(steamutils.steamPath())
    # print(profilesListe)
    # print(f"One Profile : {steamutils.getConf.profile(profilesListe[6])}")
    # t = steamutils.getConf.profile(profilesListe)

    # print(type(profilesListe))
    # for p in profilesListe:
    #     print(p)
    #     print(type(p))
    profilesDict = steamutils.getConf.profiles(profilesListe)
    print(f"All Profiles : {steamutils.getConf.profiles(profilesListe)}")
    json_conf = json.dumps(profilesDict, sort_keys=True, indent=4)
    print(json_conf)
    print(type(json_conf))
