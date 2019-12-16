#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Implémentation des fonctions utiles
    à la gestions des profiles steam.

    @author: Radic4l

"""

__author__ = 'Radic4l'
__version__ = '0.0.1'
__all__ = ['getProfilesPath']

import os

def getProfilesPath(path):

    """
        Fonction servant à retrouver tous les profile
        steam présent sur la sessionde l'utilisateur courant

        :return: Liste de paths des profiles steam trouver dans le dossier userdata/

        Usage:

        >>> import steamutils
        >>> steamutils.getProfilesPath(arg=path) # utiliser le path retourné par la méthode steamutils.steamPath()
    """

    foldersPath = path+'/userdata/'
    usersFolders = [foldersPath+i for i in os.listdir(foldersPath)]

    for i in usersFolders:
        if not os.path.isdir(i):
            usersFolders.remove(i)

    return usersFolders

