#-*- coding: utf-8 -*-

"""
Created on 2017. 8. 10.

@author: JoSoowoon
"""

from Game.Scene.SceneManager import SceneManager
from Utilities.Singleton import Singleton

from enum import Enum, unique

from io import StringIO

import os
import sys

class eConsoleMode(Enum):
    """
    콘솔 모드 열거 클래스
    """

    # 정의하지 않은 모드의 콘솔(무효한 모드 값이다.)
    Unknown = 0

    # 시스템 모드 콘솔
    System = 1

    # 게임 모드 콘솔
    Game = 2



#-------------------------------------------------------------------------------
# Game
#-------------------------------------------------------------------------------

class Game(Singleton):
    """
    게임을 구성하는 클래스
    """

    ########################################
    ## Public Variables
    ########################################

    # 장면 관리자
    sceneManager: SceneManager

    # 캐릭터 개체 관리자

    # 네트워크 관리자

    # 입력한 명령
    command: str = ''

    # 현재 콘솔 모드
    consoleMode: eConsoleMode = eConsoleMode.Unknown

    # 시스템 출력 버퍼
    consoleOutputSystem: StringIO = StringIO()

    # 게임 출력 버퍼
    consoleOutputGame: StringIO = StringIO()



    ########################################
    ## Private Variables
    ########################################

    # 게임 종료 여부
    __bTerminated__: bool = False


    ########################################
    ## Public Methods
    ########################################

    def Initialize(self):
        """
        초기화
        """
        print(f'{Game.__name__}.{Game.Initialize.__name__}()')

        self.sceneManager.Initialize()
        self.SwitchConsoleMode(eConsoleMode.Game)

        # outTexts = ['Hello\n', 'My\n', 'Name\n', 'is\n', 'JoSoowoon\n']
        # for text in outTexts:
        #     sys.stdout.write(text)


        #=======================================================================
        # testFile = open('./Data/test.txt', 'r')
        # readData = testFile.read()
        # print(readData)
        # testFile.close()
        #=======================================================================

        #=======================================================================
        # with open('test.txt', 'r') as testFile:
        #     readData = testFile.read()
        #     print(readData)
        # testFile.close()
        #=======================================================================

        return True

    def Process(self):
        """
        실행
        """
        print(f'{Game.__name__}.{Game.Process.__name__}()')

        self.__ProcessInputCommand__()

    def Release(self):
        """
        해제
        """
        print(f'{Game.__name__}.{Game.Release.__name__}()')

        # 왜 여기서는 표준 입력으로 전환하면 안되는 것일까...?
        #self.SwitchConsoleMode(CONSOLE_MODE_SYSTEM)

    def SwitchConsoleMode(self, consoleMode: eConsoleMode):
        """
        콘솔 모드를 전환한다.
        """
        if self.consoleMode == consoleMode:
            return

        print(f'{Game.__name__}.{Game.SwitchConsoleMode.__name__}() : [TargetMode] = {consoleMode}')

        self.consoleMode = consoleMode

        currentConsole: StringIO = None
        if self.consoleMode is eConsoleMode.System:
            assert(self.consoleOutputSystem is not None)
            if(self.consoleOutputSystem is not None):
                #sys.stdout = self.consoleOutputSystem
                currentConsole = self.consoleOutputSystem
                sys.stdout.write("[Console] Console mode switch to System")
        elif self.consoleMode is eConsoleMode.Game:
            assert(self.consoleOutputGame is not None)
            if(self.consoleOutputGame is not None):
                #sys.stdout = self.consoleOutputGame
                currentConsole = self.consoleOutputSystem
                sys.stdout.write("[Console] Console mode switch to Game")
        else:
            print(f'{Game.__name__}.{Game.SwitchConsoleMode.__name__}() : Invalid console mode. Switch mode to game.')
            self.SwitchConsoleMode(eConsoleMode.Game)

        #os.system('cls')
        sys.stdout = sys.__stdout__
        sys.stdout.write(currentConsole.getvalue())

    def IsTerminated(self):
        """
        종료여부
        """

        return self.__bTerminated__


    ########################################
    ## Private Methods
    ########################################

    def __init__(self):
        """
        생성자
        """
        print(f'{Game.__name__} constructed')

        self.sceneManager = SceneManager()

    def __del__(self):
        """
        소멸자
        """
        print(f'{Game.__name__} destroyed')

    def __ProcessInputCommand__(self):
        """
        입력받은 명령을 처리한다.
        """
        print(f'{Game.__name__}.{Game.__ProcessInputCommand__.__name__}()')

        print("명령을 입력하세요 : ")
        self.command = input()

        if self.command == 'quit' or self.command == 'exit':
            self.__bTerminated__ = True
        elif self.command == 'system':
            self.SwitchConsoleMode(eConsoleMode.System)
        elif self.command == 'game':
            self.SwitchConsoleMode(eConsoleMode.Game)
