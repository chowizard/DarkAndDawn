#-*- coding: utf-8 -*-

'''
Created on 2017. 8. 17.

@author: JoSoowoon
'''


from enum import Enum, unique


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


class SceneBase(object):
    '''
    모든 장면들이 상속받아야 하는 클래스
    '''
    
    # 장면 타입
    sceneType = eSceneType.Invalid
    

    def __init__(self, params):
        '''
        생성자
        '''
        
    @staticmethod
    def StaticMethod():
        pass
    
    @classmethod
    def ClassMethod(self):
        pass
    
    