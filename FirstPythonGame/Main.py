'''
Created on 2017. 8. 8.

@author: JoSoowoon
'''

from Game import Game

if __name__ == '__main__':
    pass

class Main:
    ''' 주 클래스 '''

    isTerminate = False
    game = Game.Game() 
    
    #-------------------------------------------------------------------------------
    def __init__(self):
        '''
        생성자
        '''
        
        print('Main 생성자')


    #-------------------------------------------------------------------------------
    def Initialize(self):
        '''
        초기화 
        '''
        
        print('Main 초기화')
        
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
        
        self.game.Initialize()
    
    #-------------------------------------------------------------------------------
    def Process(self):
        '''
        진행 
        '''
        
        print('Main 진행')
        
        self.game.Process()
    
    
    #-------------------------------------------------------------------------------
    def Release(self):
        '''
        해제
        '''
        
        print('Main 해제')
    
    
main = Main()
main.Initialize()
