"""
the custom_status module: Support for error code as defined by PEP8
"""

class CustomStatus:
    def __init__(self, code: int, message: str) -> None:
        self.code = code
        self.message = message

SUCCESS            = CustomStatus(200,   "success")
ERR_SYSTEM_BUSY    = CustomStatus(5000,  "the system is Busy, please try later")
ERR_PARAM          = CustomStatus(5001,  "param error")
ERR_USER_NOT_FOUND = CustomStatus(5002,  "user not found")
ERR_PASSWORD = CustomStatus(5003,  "password is error")
ERR_USER_EXISTS = CustomStatus(5004,  "user is exists")
USER_NO_LOGIN = CustomStatus(5005,  "user is not login")
TOKEN_EXPIRED = CustomStatus(5006,  "token is expired")