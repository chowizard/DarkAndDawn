#-*- coding: utf-8 -*-

from io import StringIO
from typing import Optional

class Logger:
    """
    로그 클래스
    """

    ########################################
    ## Public Variables
    ########################################
    # 로그 버퍼
    buffer: StringIO


    ########################################
    ## Public Methods
    ########################################
    @staticmethod
    def Initialize(buffer: StringIO):
        """
        로거 초기화
        """
        Logger.buffer = buffer

    @staticmethod
    def Release():
        """
        로거 자원 해제
        """
        if Logger.buffer is not None and not Logger.buffer.closed:
            Logger.buffer.close()
            Logger.buffer = None

    @staticmethod
    def Log(message: str):
        """
        로그를 버퍼에 쓴다.
        """
        if Logger.buffer is not None:
            Logger.LogToBuffer(Logger.buffer, message)

    @staticmethod
    def LogToBuffer(buffer: StringIO, message: str):
        """
        로그를 특정 버퍼에 쓴다.
        """
        try:
            if buffer is not None and not buffer.closed:
                buffer.write(f"{message}\n")
        except:
            # 로그 쓰기 실패 시 무시
            pass


    ########################################
    ## Private Methods
    ########################################

    def __init__(self):
        """
        생성자
        """
        super().__init__()
