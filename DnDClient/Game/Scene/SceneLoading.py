#-*- coding: utf-8 -*-

"""
Created on 2021. 7. 11.

@author: FlareWizard
"""

from Game.Scene.SceneBase import SceneBase, eSceneType
from Utilities.Logger import Logger

#-------------------------------------------------------------------------------
# SceneLoading
#-------------------------------------------------------------------------------

class SceneLoading(SceneBase):
    """
    게임 장면 클래스 : 로딩
    """

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

    def Enter(self):
        """
        장면 진입
        """
        Logger.Log(f'Enter {SceneLoading.__name__}')

    def Exit(self):
        """
        장면 퇴장
        """
        pass
        Logger.Log(f'Exit {SceneLoading.__name__}')


    ########################################
    ## Private Methods
    ########################################

    def __init__(self):
        """
        생성자
        """
        Logger.Log(f'{SceneLoading.__name__} constructed')

        super().__init__()
        SceneBase.sceneType = eSceneType.Loading

    def __del__(self):
        """
        소멸자
        """
        Logger.Log(f'{SceneLoading.__name__} destroyed')

        super().__del__()
