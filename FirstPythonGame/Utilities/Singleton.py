#-*- coding: utf-8 -*-

'''
Created on 2021. 7. 18.

@author: FlareWizard
'''

class Singleton(object):
    '''
    싱글톤 클래스
    : 싱글톤을 구현하기 위한 클래스들은 이 클래스를 상속하여야 한다. 
    '''
    
    
    # 싱글톤 인스턴스
    __singleton = None

        
    def __init__(self):
        '''
        생성자
        '''
        #super().__init__()
        
    @classmethod
    def Singleton(cls):
        '''
        싱글톤 인스턴스 획득
        '''
        cls.__singleton = cls()
        cls.Singleton = cls.__Singleton
        return cls.__singleton
    
    @classmethod
    def __Singleton(cls):
        '''
        싱글톤 인스턴스 획득
        '''
        return cls.__singleton
        