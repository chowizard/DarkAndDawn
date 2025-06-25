#-*- coding: utf-8 -*-

"""
Created on 2021. 7. 18.

@author: FlareWizard
"""

class Singleton(object):
    """
    싱글톤 클래스
    : 싱글톤을 구현하기 위한 클래스들은 이 클래스를 상속하여야 한다. 
    """
    
    ########################################
    ## Public Variables
    ########################################
    
    # 싱글톤 인스턴스
    __singleton = None


    ########################################
    ## Public Methods
    ########################################
        
    @classmethod
    def Singleton(targetClass):
        """
        싱글톤 인스턴스 획득
        """
        targetClass.__singleton = targetClass()
        targetClass.Singleton = targetClass.__Singleton
        return targetClass.__singleton
    
    @classmethod
    def __Singleton(targetClass):
        """
        싱글톤 인스턴스 획득
        """
        return targetClass.__singleton
    
    
    ########################################
    ## Private Methods
    ########################################
    
    def __init__(self):
        """
        생성자
        """
        #super().__init__()
        