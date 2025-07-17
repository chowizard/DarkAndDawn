#-*- coding: utf-8 -*-

"""
Created on 2017. 8. 8.

@author: JoSoowoon
"""

if __name__ == '__main__':
    # 내용 없음
    pass


from Utilities.Logger import Logger
from Console import Console


########################################
# 프로그램 시작
########################################

print("""
========================================
 Game Started
========================================
""")

Logger.Initialize(Console.consoleOutputSystem)
Console.Run()
Logger.Release()

print("""
========================================
 Game Terminated
========================================
""")
