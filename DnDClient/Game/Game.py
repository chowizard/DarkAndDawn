#-*- coding: utf-8 -*-

"""
Created on 2017. 8. 10.

@author: JoSoowoon
"""

from Game.Scene.SceneManager import SceneManager
from Utilities.Singleton import Singleton
from Utilities.Logger import Logger

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
    sceneManager: SceneManager = None

    # 캐릭터 개체 관리자

    # 네트워크 관리자


    ########################################
    ## Private Variables
    ########################################

    # 게임 종료 여부
    __isTerminated__: bool = False


    ########################################
    ## Public Methods
    ########################################

    def Initialize(self):
        """
        초기화
        """
        Logger.Log(f'{Game.__name__}.{Game.Initialize.__name__}()')

        self.sceneManager.Initialize()

        return True

    def Process(self):
        """
        실행
        """
        Logger.Log(f'{Game.__name__}.{Game.Process.__name__}()')

    def Release(self):
        """
        해제
        """
        Logger.Log(f'{Game.__name__}.{Game.Release.__name__}()')

        # 왜 여기서는 표준 입력으로 전환하면 안되는 것일까...?
        #self.SwitchConsoleMode(CONSOLE_MODE_SYSTEM)

    def IsTerminated(self):
        """
        종료여부
        """
        return self.__isTerminated__


    ########################################
    ## Private Methods
    ########################################

    def __init__(self):
        """
        생성자
        """
        Logger.Log(f'{Game.__name__} constructed')
        self.sceneManager = SceneManager()
        super().__init__()

    def __del__(self):
        """
        소멸자
        """
        self.sceneManager = None
        Logger.Log(f'{Game.__name__} destroyed')
