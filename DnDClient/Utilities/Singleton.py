#-*- coding: utf-8 -*-

"""
Created on 2021. 7. 18.

@author: FlareWizard
"""

class Singleton(object):
    """
    Singleton Class
    """

    ########################################
    ## Public Variables
    ########################################

    # Singleton Instance
    __singleton: object = None

    ########################################
    ## Public Methods
    ########################################

    @classmethod
    def Singleton(targetClass):
        """
        Get Singleton Instance
        """
        if targetClass.__singleton is None:
            targetClass.__singleton = targetClass()
        return targetClass.__singleton

    ########################################
    ## Private Methods
    ########################################

    def __init__(self):
        """
        Constructor
        """
        super().__init__()
