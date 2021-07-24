#-*- coding: utf-8 -*-

'''
Created on 2017. 8. 17.

@author: JoSoowoon
'''


from . SceneBase import eSceneType
from . SceneIntro import SceneIntro
from . SceneLobby import SceneLobby
from . SceneLoading import SceneLoading
from . SceneGamePlay import SceneGamePlay

from Utilities.Singleton import Singleton


class SceneManager(Singleton):
    '''
    장면 관리자
    '''
    
    #-------------------------------------------------------------------------------
    # Public Variables
    #-------------------------------------------------------------------------------
    
    # 장면 목록
    scenes = { }
    
    
    #-------------------------------------------------------------------------------
    # Public Methods
    #-------------------------------------------------------------------------------
        
    def Initialize(self):
        '''
        초기화
        '''
        self.__InitializeScenes__()
        return True
    
    
    #-------------------------------------------------------------------------------
    # Private Methods
    #-------------------------------------------------------------------------------
    
    def __init__(self):
        '''
        생성자
        '''
        #super.__init__()
        
    def __InitializeScenes__(self):
        '''
        장면 객체들을 초기화한다.
        '''
        self.scenes.setdefault(eSceneType.Intro, SceneIntro())
        self.scenes.setdefault(eSceneType.Lobby, SceneLobby())
        self.scenes.setdefault(eSceneType.Loading, SceneLoading())
        self.scenes.setdefault(eSceneType.GamePlay, SceneGamePlay())


#-------------------------------------------------------------------------------
# Test Codes
#-------------------------------------------------------------------------------

if(__name__ == '__main__') :
    '''
    SceneManager 테스트 코드
    '''
    
    def TestSingleton():
        '''
        싱글톤 작동 여부 테스트
        '''
        sceneManager = SceneManager.Singleton()
        print(sceneManager)
        sceneManager2 = SceneManager.Singleton()
        print(sceneManager2)
        
        print(sceneManager == sceneManager2)
        
        sceneManager.number = 1
        sceneManager2.number = 2
        print('First = {0},  Second = {1}'.format(sceneManager.number, sceneManager2.number))    
    
    TestSingleton()
    
