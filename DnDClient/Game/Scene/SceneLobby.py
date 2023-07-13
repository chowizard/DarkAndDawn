#-*- coding: utf-8 -*-

'''
Created on 2021. 7. 11.

@author: FlareWizard
'''

from Game.Scene.SceneBase import SceneBase, eSceneType


#-------------------------------------------------------------------------------
# SceneLobby
#-------------------------------------------------------------------------------

class SceneLobby(SceneBase):
    '''
    게임 장면 클래스 : 로비
    '''
    
    
    ## Public Methods
    
    def Initialize(self):
        '''
        초기화
        ''' 
        
        return True
    
    
    def Process(self):
        '''
        프로세스
        '''
        
        pass
    
        
    def Release(self):
        '''
        해제
        '''
        
        pass
    
    

    ## Private Methods

    def __init__(self):
        '''
        생성자
        '''
        
        print("SceneLobby constructed")
        
        super().__init__()
        SceneBase.sceneType = eSceneType.Lobby
        
        
    def __del__(self):
        '''
        소멸자
        '''
        
        print('SceneLobby destroyed')
        
        super().__del__()
        