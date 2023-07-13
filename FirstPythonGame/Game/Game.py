#-*- coding: utf-8 -*-

'''
Created on 2017. 8. 10.

@author: JoSoowoon
'''

from Game.Scene.SceneManager import SceneManager
from Utilities.Singleton import Singleton

import win32api
import win32console
import win32con


# 정의하지 않은 모드의 콘솔(무효한 모드 값이다.)
CONSOLE_MODE_NONE = 0

# 시스템 모드 콘솔
CONSOLE_MODE_SYSTEM = 1

# 게임 모드 콘솔
CONSOLE_MODE_GAME = 2



#-------------------------------------------------------------------------------
# Game
#-------------------------------------------------------------------------------

class Game(Singleton):
    '''
    게임을 구성하는 클래스
    '''    
    
    ########################################
    ## Public Variables
    ########################################
   
    # 장면 관리자
    sceneManager = None
    
    # 캐릭터 개체 관리자
    
    # 네트워크 관리자 
   
    # 입력한 명령
    command = ''
    
    # 현재 콘솔 모드
    consoleMode = CONSOLE_MODE_NONE
    
    # 시스템 콘솔
    consoleSystem = None
    
    # 게임 콘솔
    consoleGame = None
   
   
    
    ########################################
    ## Private Variables
    ########################################
    
    # 게임 종료 여부
    __bTerminated__ = False
    
    
    
    ## Public Methods    
    
    def Initialize(self):
        '''
        초기화
        '''
        
        print('Game.Initialize()')

        self.sceneManager.Initialize()
        
        if self.consoleSystem == None:
            self.consoleSystem = win32console.GetStdHandle(win32console.STD_OUTPUT_HANDLE)
        
        if self.consoleGame == None:
            self.consoleGame = win32console.CreateConsoleScreenBuffer(DesiredAccess = win32con.GENERIC_READ | win32con.GENERIC_WRITE,
                                                                      ShareMode = 0,
                                                                      SecurityAttributes = None, 
                                                                      Flags = win32console.CONSOLE_TEXTMODE_BUFFER)
        
        self.SwitchConsoleMode(CONSOLE_MODE_GAME)
        #self.SwitchConsoleMode(CONSOLE_MODE_SYSTEM)
        
        
        # terminalSize = os.get_terminal_size()
        # terminalSize = shutil.get_terminal_size()
        # print('[TerminalSize] = [Columns] = {0}  [Lines] = {1}'.format(terminalSize.columns, terminalSize.lines))
        #
        #
        #
        # outTexts = ['Hello\n', 'My\n', 'Name\n', 'is\n', 'JoSoowoon\n']
        # for text in outTexts:
        #     sys.stdout.write(text)
        
        
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
        
        self.__ProcessInputCommand__()


    def Release(self):
        '''
        해제
        '''
        
        print('Game.Release()')
        
        # 왜 여기서는 표준 입력으로 전환하면 안되는 것일까...?
        #self.SwitchConsoleMode(CONSOLE_MODE_SYSTEM)
        
        
    def SwitchConsoleMode(self, consoleMode):
        '''
        콘솔 모드를 전환한다.
        '''
        
        if self.consoleMode == consoleMode:
            return
        
        print('Game.SwitchConsoleMode() : [TargetMode] = {0}'.format(consoleMode))
        
        self.consoleMode = consoleMode;
        
        if self.consoleMode == CONSOLE_MODE_SYSTEM:
            if(self.consoleSystem != None):
                self.consoleSystem.SetConsoleActiveScreenBuffer()
        elif self.consoleMode == CONSOLE_MODE_GAME:
            if(self.consoleGame != None):
                self.consoleGame.SetConsoleActiveScreenBuffer()
        else:
            print('Game.SwitchSonsoleMode() : Invalid console mode. Switch mode to game.')
            self.SwitchConsoleMode(CONSOLE_MODE_GAME)
            
    
    def IsTerminated(self):
        '''
        종료여부
        '''
        
        return self.__bTerminated__
    

   
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
        
        
    def __ProcessInputCommand__(self):
        '''
        입력받은 명령을 처리한다.
        '''
        
        print('Game.__ProcessInputCommand__()')
        
        #key = win32api.GetKeyState()
    
        print("명령을 입력하세요 : ")
        self.command = input()
        
        if self.command == 'quit':
            self.__bTerminated__ = True
        elif self.command == 'system':
            self.SwitchConsoleMode(CONSOLE_MODE_SYSTEM)
        elif self.command == 'game':
            self.SwitchConsoleMode(CONSOLE_MODE_GAME)
        