#-*- coding: utf-8 -*-

'''
Created on 2021. 7. 11.

@author: FlareWizard
'''

from Game.Scene.SceneBase import SceneBase, eSceneType


#-------------------------------------------------------------------------------
# SceneGamePlay
#-------------------------------------------------------------------------------

class SceneGamePlay(SceneBase):
    '''
    게임 장면 클래스 : 게임 플레이
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
        
        print("SceneGamePlay constructed")
        
        super().__init__()
        SceneBase.sceneType = eSceneType.GamePlay
        
        
    def __del__(self):
        '''
        소멸자
        '''
        
        print('SceneGamePlay destroyed')
        
        super().__del__()