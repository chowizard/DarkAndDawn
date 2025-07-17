#-*- coding: utf-8 -*-

from enum import Enum
from io import StringIO
import os
import sys

from Utilities.Logger import Logger
from Game.Game import Game

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

class Console:
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
        Logger.Log(f'{Console.__name__}.{Console.Run.__name__}() : Begin')

        Console.__Initialize__()

        while True:
            Console.__CheckIsTerminated__()
            if Console.__isTerminated__ is True:
                break
            Console.__Process__()

        Console.__Release__()

        Logger.Log(f'{Console.__name__}.{Console.Run.__name__}() : End')

    @staticmethod
    def SwitchConsoleMode(consoleMode: eConsoleMode):
        """
        콘솔 모드를 전환한다.
        """
        if Console.consoleMode == consoleMode:
            return

        Logger.Log(f'{Console.__name__}.{Console.SwitchConsoleMode.__name__}() : [TargetMode] = {consoleMode}')

        Console.consoleMode = consoleMode
        consoleBuffer = Console.GetConsoleBuffer()
        if consoleBuffer is not None:
            Logger.LogToBuffer(consoleBuffer, f'[Console] Console mode switch to {Console.consoleMode}')

    @staticmethod
    def GetConsoleBuffer() -> StringIO:
        """
        현재 콘솔 버퍼를 가져온다.
        """
        consoleBuffer: StringIO
        if (Console.consoleMode is eConsoleMode.System):
            consoleBuffer = Console.consoleOutputSystem
        elif (Console.consoleMode is eConsoleMode.Game):
            consoleBuffer = Console.consoleOutputGame
        else:
            consoleBuffer = None

        return consoleBuffer

    ## Private Methods

    @staticmethod
    def __Initialize__():
        """
        초기화
        """
        Logger.Log(f'{Console.__name__}.{Console.__Initialize__.__name__}()')

        Console.SwitchConsoleMode(eConsoleMode.Game)

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
        Logger.Log(f'{Console.__name__}.{Console.__Process__.__name__}()')
        Console.__ProcessInputCommand__()
        Game.Singleton().Process()

    @staticmethod
    def __Release__():
        """
        해제
        """
        Game.Singleton().Release()
        Logger.Log(f'{Console.__name__}.{Console.__Release__.__name__}()')

    @staticmethod
    def __CheckIsTerminated__():
        """
        종료 여부를 확인한다.
        """
        if Console.__isTerminated__ is True:
            return True
        isTerminated = Game.Singleton().IsTerminated()
        if isTerminated is False:
            return False
        Console.__isTerminated__ = True

    @staticmethod
    def __ProcessInputCommand__():
        """
        입력받은 명령을 처리한다.
        """
        Logger.Log(f'{Console.__name__}.{Console.__ProcessInputCommand__.__name__}()')

        try:
            print("명령을 입력하세요 : ")
            Console.command = input()

            if Console.command in ('quit', 'exit'):
                Console.__isTerminated__ = True
            elif Console.command in 'system':
                Console.SwitchConsoleMode(eConsoleMode.System)
            elif Console.command in 'game':
                Console.SwitchConsoleMode(eConsoleMode.Game)
                Console.consoleOutputGame.truncate(0)
                Console.consoleOutputGame.seek(os.SEEK_SET)

            os.system('cls')
            sys.stdout = sys.__stdout__
            consoleBuffer = Console.GetConsoleBuffer()
            if consoleBuffer is not None:
                sys.stdout.write(consoleBuffer.getvalue())

        except KeyboardInterrupt:
            Logger.Log('[Program] Program terminated by user!')
            Console.__isTerminated__ = True

        except Exception as exception:
            Logger.Log(f'[Exception] Exception occurred! <Content> = {str(exception)}')
            Console.__isTerminated__ = True
