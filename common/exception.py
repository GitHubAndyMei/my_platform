"""
exception modul
"""

from common.result_code import CustomStatus


class CtException(Exception):
    '''
    @brief ct异常类,所有异常类需要继承此类
    '''

    def __init__(self, status: CustomStatus, message=""):
        super().__init__()
        self.code = status.code
        if message:
            self.message = message
        else:
            self.message = status.message

    def __str__(self):
        return f"code: {self.code}, message: {self.message}"