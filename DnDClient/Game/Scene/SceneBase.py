#-*- coding: utf-8 -*-

"""
Created on 2017. 8. 17.

@author: JoSoowoon
"""

from enum import Enum, unique
from Utilities.Logger import Logger


#-------------------------------------------------------------------------------
# eSceneType
#-------------------------------------------------------------------------------

@unique
class eSceneType(Enum):
    """
    장면 열거 클래스
    """

    # 무효값
    Invalid = 0

    # 진입
    Intro = 1

    # 로비
    Lobby = 2

    # 로딩
    Loading = 3

    # 게임플레이
    GamePlay = 4


    @staticmethod
    def ToName(enum):
        """
        열거형을 문자열로 반환한다.
        """
        if enum == eSceneType.Intro:
            result = 'Intro'
        elif enum == eSceneType.Lobby:
            result = 'Lobby'
        elif enum == eSceneType.Loading:
            result = 'Loading'
        elif enum == eSceneType.GamePlay:
            result = 'GamePlay'
        else:
            result = 'Invalid'
        return result



#-------------------------------------------------------------------------------
# SceneBase
#-------------------------------------------------------------------------------

class SceneBase(object):
    """
    모든 장면들이 상속받아야 하는 클래스
    """

    ########################################
    ## Public Variables
    ########################################

    # 장면 타입
    sceneType: eSceneType = eSceneType.Invalid


    ########################################
    ## Public Methods
    ########################################

    def Initialize(self):
        """
        초기화
        """
        return True

    def Process(self):
        """
        프로세스
        """
        pass

    def Release(self):
        """
        해제
        """
        pass


    ########################################
    ## Private Methods
    ########################################

    def __init__(self):
        """
        생성자
        """
        Logger.Log(f'{SceneBase.__name__} constructed')

    def __del__(self):
        """
        소멸자
        """
        Logger.Log(f'{SceneBase.__name__} destroyed')
