#-*- coding: utf-8 -*-

'''
Created on 2017. 8. 8.

@author: JoSoowoon
'''

from Game.Game import Game


if __name__ == '__main__':
    pass


#-------------------------------------------------------------------------------
# Main
#-------------------------------------------------------------------------------

class Main:
    '''
     주 클래스 (진입점)
    '''

    # Public Variables

    # 애플리케이션 종료 여부
    isTerminate = False


    ## Public Methods
    
    @staticmethod
    def Run():
        '''
        구동
        '''
        
        print('Main.Run() : Begin')
        
        Main.__Initialize__()
        
        # while Main.isTerminate == False:
        #     Main.__Process__()
        Main.__Process__()
        
        Main.__Release__()
        
        print('Main.Run() : End')


    ## Private Methods
        
    @staticmethod
    def __Initialize__():
        '''
        초기화
        '''        
        print('Main 초기화')

        Game.Singleton().Initialize()
    
    
    @staticmethod
    def __Process__():
        '''
        진행 
        '''
        
        print('Main 진행')
        
        Game.Singleton().Process()
    
    
    @staticmethod
    def __Release__():
        '''
        해제
        '''
        
        Game.Singleton().Release()
        
        print('Main 해제')

    
print('''
========================================
 Game Started
========================================
''')
    
Main.Run()

print('''
========================================
 Game Terminated
========================================
''')