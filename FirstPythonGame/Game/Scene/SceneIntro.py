#-*- coding: utf-8 -*-

'''
Created on 2021. 7. 11.

@author: FlareWizard
'''


from . SceneBase import SceneBase, eSceneType



class SceneIntro(SceneBase):
    '''
    게임 장면 클래스 : 진입부
    '''


    def __init__(self, params):
        '''
        생성자
        '''
        SceneBase.__init__(self, params)
        SceneBase.sceneType = eSceneType.Intro
        print("SceneIntro created")
        