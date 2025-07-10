#-*- coding: utf-8 -*-

"""
Created on 2017. 8. 8.

@author: JoSoowoon
"""

from Game.Game import Game

from enum import Enum, unique
from io import StringIO
import sys

if __name__ == '__main__':
    pass


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
# Main
#-------------------------------------------------------------------------------

class Main:
    """
     주 클래스 (진입점)
    """

    ########################################
    # Public Variables
    ########################################

    # 입력한 명령
    command: str = ''

    # 현재 콘솔 모드
    consoleMode: eConsoleMode = eConsoleMode.Unknown

    # 시스템 출력 버퍼
    consoleOutputSystem: StringIO = StringIO()

    # 게임 출력 버퍼
    consoleOutputGame: StringIO = StringIO()


    ########################################
    # Private Variables
    ########################################

    # 애플리케이션 종료 여부
    __isTerminated__: bool = False


    ########################################
    ## Public Methods
    ########################################

    @staticmethod
    def Run():
        """
        구동
        """
        print(f'{Main.__name__}.{Main.Run.__name__}() : Begin')

        Main.__Initialize__()

        while True:
            Main.__CheckIsTerminated__()
            if Main.__isTerminated__ is True:
                break
            Main.__Process__()

        Main.__Release__()

        print(f'{Main.__name__}.{Main.Run.__name__}() : End')

    @staticmethod
    def SwitchConsoleMode(consoleMode: eConsoleMode):
        """
        콘솔 모드를 전환한다.
        """
        if Main.consoleMode == consoleMode:
            return

        print(f'{Main.__name__}.{Main.SwitchConsoleMode.__name__}() : [TargetMode] = {consoleMode}')

        Main.consoleMode = consoleMode

        currentConsole: StringIO = None
        if Main.consoleMode is eConsoleMode.System:
            assert(Main.consoleOutputSystem is not None)
            if(Main.consoleOutputSystem is not None):
                #sys.stdout = Main.consoleOutputSystem
                currentConsole = Main.consoleOutputSystem
                sys.stdout.write("[Console] Console mode switch to System")
        elif Main.consoleMode is eConsoleMode.Game:
            assert(Main.consoleOutputGame is not None)
            if(Main.consoleOutputGame is not None):
                #sys.stdout = Main.consoleOutputGame
                currentConsole = Main.consoleOutputSystem
                sys.stdout.write("[Console] Console mode switch to Game")
        else:
            print(f'{Main.__name__}.{Main.SwitchConsoleMode.__name__}() : Invalid console mode. Switch mode to game.')
            Main.SwitchConsoleMode(eConsoleMode.Game)

        #os.system('cls')
        sys.stdout = sys.__stdout__
        sys.stdout.write(currentConsole.getvalue())


    ## Private Methods

    @staticmethod
    def __Initialize__():
        """
        초기화
        """
        print(f'{Main.__name__}.{Main.__Initialize__.__name__}()')

        Main.SwitchConsoleMode(eConsoleMode.Game)

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

        Game.Singleton().Initialize()

    @staticmethod
    def __Process__():
        """
        진행
        """
        print(f'{Main.__name__}.{Main.__Process__.__name__}()')
        Main.__ProcessInputCommand__()
        Game.Singleton().Process()

    @staticmethod
    def __Release__():
        """
        해제
        """
        Game.Singleton().Release()
        print(f'{Main.__name__}.{Main.__Release__.__name__}()')

    @staticmethod
    def __CheckIsTerminated__():
        """
        종료 여부를 확인한다.
        """
        if Main.__isTerminated__ is True:
            return True
        isTerminated = Game.Singleton().IsTerminated()
        if isTerminated is False:
            return False
        Main.__isTerminated__ = True

    @staticmethod
    def __ProcessInputCommand__():
        """
        입력받은 명령을 처리한다.
        """
        print(f'{Main.__name__}.{Main.__ProcessInputCommand__.__name__}()')

        print("명령을 입력하세요 : ")
        Main.command = input()

        if Main.command in ('quit', 'exit'):
            Main.__isTerminated__ = True
        elif Main.command in ('system'):
            Main.SwitchConsoleMode(eConsoleMode.System)
        elif Main.command in ('game'):
            Main.SwitchConsoleMode(eConsoleMode.Game)


########################################
# 프로그램 시작
########################################

print("""
========================================
 Game Started
========================================
""")

Main.Run()

print("""
========================================
 Game Terminated
========================================
""")
