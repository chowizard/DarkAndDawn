#-*- coding: utf-8 -*-

"""
Created on 2017. 8. 8.

@author: JoSoowoon
"""

from Game.Game import Game


if __name__ == '__main__':
    pass


#-------------------------------------------------------------------------------
# Main
#-------------------------------------------------------------------------------

class Main:
    """
     주 클래스 (진입점)
    """

    ########################################
    # Public Variables
    ########################################



    ########################################
    # Private Variables
    ########################################

    # 애플리케이션 종료 여부
    __isTerminate__ = False


    ########################################
    ## Public Methods
    ########################################

    @staticmethod
    def Run():
        """
        구동
        """
        print(f'{Main.__name__}.{Main.Run.__name__}() : Begin')

        Main.__Initialize__()

        while True:
            Main.__CheckIsTerminated__()
            if Main.__isTerminate__ == True:
                break

            Main.__Process__()
        #Main.__Process__()

        Main.__Release__()

        print(f'{Main.__name__}.{Main.Run.__name__}() : End')


    ## Private Methods

    @staticmethod
    def __Initialize__():
        """
        초기화
        """
        print(f'{Main.__name__}.{Main.__Initialize__.__name__}()')
        Game.Singleton().Initialize()

    @staticmethod
    def __Process__():
        """
        진행
        """
        print(f'{Main.__name__}.{Main.__Process__.__name__}()')
        Game.Singleton().Process()


    @staticmethod
    def __Release__():
        """
        해제
        """
        Game.Singleton().Release()
        print(f'{Main.__name__}.{Main.__Release__.__name__}()')

    @staticmethod
    def __CheckIsTerminated__():
        """
        종료 여부를 확인한다.
        """
        if Main.__isTerminate__ == True:
            return True
        else:
            isTerminated = Game.Singleton().IsTerminated()
            if isTerminated == False:
                return False

            Main.__isTerminate__ = True


########################################
# 프로그램 시작
########################################

print("""
========================================
 Game Started
========================================
""")

Main.Run()

print("""
========================================
 Game Terminated
========================================
""")
