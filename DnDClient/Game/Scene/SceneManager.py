#-*- coding: utf-8 -*-

"""
Created on 2017. 8. 17.

@author: JoSoowoon
"""

from Game.Scene.SceneBase import eSceneType, SceneBase
from Game.Scene.SceneIntro import SceneIntro
from Game.Scene.SceneLobby import SceneLobby
from Game.Scene.SceneLoading import SceneLoading
from Game.Scene.SceneGamePlay import SceneGamePlay
from Utilities.Logger import Logger


#-------------------------------------------------------------------------------
# SceneManager
#-------------------------------------------------------------------------------

class SceneManager:
    """
    장면 관리자
    """

    ########################################
    # Public Variables
    ########################################

    # 장면 목록
    scenes: dict[eSceneType, SceneBase] = \
    {
        eSceneType.Intro: SceneIntro(),
        eSceneType.Lobby: SceneLobby(),
        eSceneType.Loading: SceneLoading(),
        eSceneType.GamePlay: SceneGamePlay()
    }

    # 현재 장면
    currentScene: SceneBase = None


    ########################################
    ## Public Methods
    ########################################

    def Initialize(self) -> bool:
        """
        초기화
        """
        self.__InitializeScenes__()
        return True

    def ChangeScene(self, sceneType: eSceneType):
        """
        장면 교체
        """
        if sceneType in self.scenes:
            self.currentScene = self.scenes[sceneType]
            self.currentScene.Initialize()
            return True
        else:
            return False


    ########################################
    ## Private Methods
    ########################################

    def __init__(self):
        """
        생성자
        """
        Logger.Log(f'{SceneManager.__name__} constructed')

    def __del__(self):
        """
        소멸자
        """
        #for scene in self.scenes:
        #    del scene
        self.scenes.clear()
        Logger.Log(f'{SceneManager.__name__} destroyed')


    def __InitializeScenes__(self):
        """
        장면 객체들을 초기화한다.
        """
        self.scenes.setdefault(eSceneType.Intro, SceneIntro())
        self.scenes.setdefault(eSceneType.Lobby, SceneLobby())
        self.scenes.setdefault(eSceneType.Loading, SceneLoading())
        self.scenes.setdefault(eSceneType.GamePlay, SceneGamePlay())
