#-*- coding: utf-8 -*-

"""
Created on 2017. 8. 10.

@author: JoSoowoon
"""

from Game.Scene.SceneManager import SceneManager
from Utilities.Singleton import Singleton
from Utilities.Logger import Logger

#-------------------------------------------------------------------------------
# Game
#-------------------------------------------------------------------------------

class Game(Singleton):
    """
    Class responsible for core game logic
    """

    ########################################
    ## Public Variables
    ########################################

    # Scene Manager
    sceneManager: SceneManager = None

    ########################################
    ## Private Variables
    ########################################

    # Game termination flag
    _isTerminated: bool = False

    ########################################
    ## Public Methods
    ########################################

    def Initialize(self):
        """
        Initialize Game
        """
        Logger.Log(f'{Game.__name__}.{Game.Initialize.__name__}()')

        self.sceneManager.Initialize()
        return True

    def Release(self):
        """
        Release Game Resources
        """
        Logger.Log(f'{Game.__name__}.{Game.Release.__name__}()')

    def IsTerminated(self):
        """
        Check if game is terminated
        """
        return self._isTerminated

    ########################################
    ## Private Methods
    ########################################

    def __init__(self):
        """
        Constructor (Private)
        """
        Logger.Log(f'{Game.__name__} constructed')
        self.sceneManager = SceneManager()
        super().__init__()

    def __del__(self):
        """
        Destructor
        """
        self.sceneManager = None
        Logger.Log(f'{Game.__name__} destroyed')
