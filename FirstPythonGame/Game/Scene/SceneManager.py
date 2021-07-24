#-*- coding: utf-8 -*-

'''
Created on 2017. 8. 17.

@author: JoSoowoon
'''

from Game.Scene.SceneBase import eSceneType
from Game.Scene.SceneIntro import SceneIntro
from Game.Scene.SceneLobby import SceneLobby
from Game.Scene.SceneLoading import SceneLoading
from Game.Scene.SceneGamePlay import SceneGamePlay


#-------------------------------------------------------------------------------
# SceneManager
#-------------------------------------------------------------------------------

class SceneManager:
    '''
    장면 관리자
    '''
    
    # Public Variables
    
    # 장면 목록
    scenes = { }
    
    

    ## Public Methods
        
    def Initialize(self):
        '''
        초기화
        '''
        
        self.__InitializeScenes__()
        return True
    
    
    ## Private Methods
    
    def __init__(self):
        '''
        생성자
        '''
        
        print('SceneManager contructed')
        
        
    def __del(self):
        '''
        소멸자
        '''
        
        for scene in self.scenes:
            del scene
        self.scenes.clear()
        
        print('SceneManager destroyed')

        
    def __InitializeScenes__(self):
        '''
        장면 객체들을 초기화한다.
        '''
        
        self.scenes.setdefault(eSceneType.Intro, SceneIntro())
        self.scenes.setdefault(eSceneType.Lobby, SceneLobby())
        self.scenes.setdefault(eSceneType.Loading, SceneLoading())
        self.scenes.setdefault(eSceneType.GamePlay, SceneGamePlay())
