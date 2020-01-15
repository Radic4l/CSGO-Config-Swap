#!/usr/bin/env python
# -*- coding: utf-8 -*-
import winreg

__author__ = 'Radic4l'
__version__ = '0.0.1'
__all__ = ['games']

def games():
    # i = 0
    # key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,'Software\\Valve\\Steam', 0, winreg.)
    parentKey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Valve\\Steam\\Apps')
    i = 0
    while True:
        try:
            key = winreg.EnumKey(parentKey, i)
            print(key)
            i += 1
        except WindowsError:
            break

if __name__ == '__main__':
    print(games())