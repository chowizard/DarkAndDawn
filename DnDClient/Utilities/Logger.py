#-*- coding: utf-8 -*-

from typing import Callable, Optional

class Logger:
    """
    Logger Class
    """

    ########################################
    ## Private Variables
    ########################################
    
    # Log handler callback
    _logHandler: Optional[Callable[[str], None]] = None

    ########################################
    ## Public Methods
    ########################################
    
    @staticmethod
    def Initialize(logHandler: Callable[[str], None] = None):
        """
        Initialize the logger with an optional handler.
        """
        Logger._logHandler = logHandler

    @staticmethod
    def Release():
        """
        Release logger resources.
        """
        Logger._logHandler = None

    @staticmethod
    def Log(message: str):
        """
        Write a log message using the registered handler.
        """
        if Logger._logHandler:
            Logger._logHandler(message)
        else:
            # Fallback for when no handler is registered (e.g. early startup)
            print(f"[Log] {message}")

    ########################################
    ## Private Methods
    ########################################

    def __init__(self):
        """
        Constructor (Private)
        """
        pass
