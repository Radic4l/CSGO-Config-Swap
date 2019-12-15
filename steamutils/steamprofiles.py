#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = 'Radic4l'
__version__ = '0.0.1'
__all__ = ['getProfilesPath']

import os

def getProfilesPath(path):
    """
        Fonction servant à retrouver tous les profile
        steam présent sur la sessionde l'utilisateur courant

        :return: Liste des paths

        Usage:

        >>> import steamutils
        >>> steamutils.getProfilesPath(arg=path)
    """

    foldersPath = path+'/userdata/'
    usersFolders = [foldersPath+i for i in os.listdir(foldersPath)]

    for i in usersFolders:
        if not os.path.isdir(i):
            usersFolders.remove(i)

    return usersFolders