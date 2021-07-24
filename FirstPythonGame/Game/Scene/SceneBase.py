#-*- coding: utf-8 -*-

'''
Created on 2017. 8. 17.

@author: JoSoowoon
'''

from enum import Enum, unique


#-------------------------------------------------------------------------------
# eSceneType
#-------------------------------------------------------------------------------

@unique
class eSceneType(Enum):
    '''
    장면 관련 열거 클래스
    '''

    Invalid = 0
    Intro = 1
    Lobby = 2
    Loading = 3
    GamePlay = 4


    @staticmethod
    def ToName(enum):
        result = 'Invalid'

        if enum == eSceneType.Intro:
            result = 'Intro'
        elif enum == eSceneType.Lobby:
            result = 'Lobby'
        elif enum == eSceneType.Loading:
            result = 'Loading'
        elif enum == eSceneType.GamePlay:
            result = 'GamePlay'

        return result



#-------------------------------------------------------------------------------
# SceneBase
#-------------------------------------------------------------------------------

class SceneBase(object):
    '''
    모든 장면들이 상속받아야 하는 클래스
    '''
    
    
    ## Public Variables
    
    # 장면 타입
    sceneType = eSceneType.Invalid
    

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
    
        print('SceneBase constructed')
        
    
    def __del__(self):
        '''
        소멸자
        '''
        
        print('SceneBase destroyed')