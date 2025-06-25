#-*- coding: utf-8 -*-

'''
Created on 2024. 1. 10.

@author: chowizard
'''

from win32 import win32api
from win32 import win32console
from win32.lib import win32con

import time
import sys

print('----------------------------------------\n' +
      '[ Started ]\n' + 
      '----------------------------------------\n\n')

systemConsole = win32console.GetStdHandle(win32console.STD_OUTPUT_HANDLE)
print('[SystemConsole] = {Handle}'.format(Handle = systemConsole))

eventConsole = win32console.CreateConsoleScreenBuffer(DesiredAccess = win32con.GENERIC_READ | win32con.GENERIC_WRITE, 
                                                      ShareMode = 0,
                                                      SecurityAttributes = None,
                                                      Flags = win32console.CONSOLE_TEXTMODE_BUFFER)
print('[EventConsole] = {Handle}'.format(Handle = eventConsole))

sys.stdin.read(1)
eventConsole.SetStdHandle(win32console.STD_OUTPUT_HANDLE)
eventConsole.SetConsoleActiveScreenBuffer()
print('eventConsole activated.')
#consoleMode = win32console.GetConsoleDisplayMode()
#print('[ConsoleMode] = {Mode}'.format(Mode = consoleMode))

time.sleep(3)

sys.stdin.read(1)
systemConsole.SetStdHandle(win32console.STD_OUTPUT_HANDLE)
systemConsole.SetConsoleActiveScreenBuffer()
print('systemConsole activated.')
#consoleMode = win32console.GetConsoleMode()
#print('[ConsoleMode] = {Mode}'.format(Mode = consoleMode))

sys.stdin.read(1)
eventConsole.SetStdHandle(win32console.STD_OUTPUT_HANDLE)
eventConsole.SetConsoleActiveScreenBuffer()
print('eventConsole activated.')

sys.stdin.read(1)
systemConsole.SetStdHandle(win32console.STD_OUTPUT_HANDLE)
systemConsole.SetConsoleActiveScreenBuffer()
print('systemConsole activated.')

print('\n\n----------------------------------------\n' +
      '[ Finished ]\n' + 
      '----------------------------------------\n\n')
