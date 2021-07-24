#-*- coding: utf-8 -*-

'''
Created on 2017. 8. 10.

@author: JoSoowoon
'''

from Game.Scene.SceneManager import SceneManager
from Utilities.Singleton import Singleton
 

#-------------------------------------------------------------------------------
# Game
#-------------------------------------------------------------------------------

class Game(Singleton):
    '''
    게임을 구성하는 클래스
    '''
   
    ## Public Variables
   
    # 장면 관리자
    sceneManager = None
    
    # 캐릭터 개체 관리자
    
    # 네트워크 관리자 
   
    command = ''
    
    
    ## Public Methods    
    
    def Initialize(self):
        '''
        초기화
        '''
        
        print('Game.Initialize()')
        
        self.sceneManager.Initialize()
        
        #=======================================================================
        # testFile = open('./Data/test.txt', 'r')
        # readData = testFile.read()
        # print(readData)
        # testFile.close()
        #=======================================================================

        #=======================================================================
        # with open('test.txt', 'r') as testFile:
        #     readData = testFile.read()
        #     print(readData)
        # testFile.close()
        #=======================================================================
        
        return True

   
    def Process(self):
        '''
        실행
        '''
        
        print('Game.Process()')
    
        print("명령을 입력하세요 : ")
        self.command = input()


    def Release(self):
        '''
        해제
        '''
        
        print('Game.Release()')
   
   
    ## Private Methods
   
    def __init__(self):
        '''
        생성자
        '''
        
        print('Game 생성')
        
        self.sceneManager = SceneManager()
        
        
    def __del__(self):
        '''
        소멸자
        '''
        
        print('Game 소멸')
   
