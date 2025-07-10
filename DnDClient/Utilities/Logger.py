#-*- coding: utf-8 -*-

from io import StringIO

class Logger:
    """
    로그 클래스
    """

    # 로그 버퍼
    buffer: StringIO

    @staticmethod
    def Log(message: str):
        """
        로그를 버퍼에 쓴다.
        """
        if Logger.buffer is not None:
            Logger.buffer.write(message)
