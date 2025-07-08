#-*- coding: utf-8 -*-

from io import StringIO

class Logger:
    """
    로그 클래스
    """

    # 로그 버퍼
    buffer: StringIO = None

    @staticmethod
    def Log(message: str):
        """
        로그를 버퍼에 쓴다.
        """
        Logger.buffer.write(message)
