#!/usr/bin/env python
# -*- coding: utf-8 -*-

import winreg

__author__ = 'Radic4l'
__version__ = '0.0.1'
__all__ = ['steamPath','gamesId']


def steamPath():

    """
        Implémentation utilisé pour trouver
        le chemin d'installation de steam

        :return: une string du path steam

        Usage:

        >>> import steamutils
        >>> steamutils.steamPath()

    """

    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Valve\\Steam', 0, winreg.KEY_READ)
    (valeur, typevaleur) = winreg.QueryValueEx(key, 'SteamPath')
    winreg.CloseKey(key)
    return valeur

def gamesId():

    """
        Retourne tout les jeux steam achetés
        de tous les utilisateurs steam présents

        :return: Liste d'ID des jeux steam existant sur le compte

        Usage:

        >>> import steamutils
        >>> steamutils.gamesId()
    """
    
    parentKey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Valve\\Steam\\Apps')
    i = 0
    ids = []
    while True:
        try:
            key = winreg.EnumKey(parentKey, i)
            ids.append(key)
            i += 1
        except WindowsError:
            break
    winreg.CloseKey(parentKey)
    ids.remove('0')
    return ids

if __name__ == '__main__':
    print(steamPath())
    print(gamesId())

