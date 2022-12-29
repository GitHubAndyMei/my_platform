"""
the custom_status module: Support for error code as defined by PEP8
"""

class CustomStatus:
    def __init__(self, code: int, message: str) -> None:
        self.code = code
        self.message = message

SUCCESS            = CustomStatus(200,   "success")
ERR_SYSTEM_BUSY    = CustomStatus(5000,  "The system is Busy, please try later")
ERR_PARAM          = CustomStatus(5001,  "Param error")
ERR_USER_NOT_FOUND = CustomStatus(5002,  "User not found")
ERR_PASSWORD       = CustomStatus(5003,  "Password is error")
ERR_USER_EXISTS    = CustomStatus(5002,  "User already exists")
