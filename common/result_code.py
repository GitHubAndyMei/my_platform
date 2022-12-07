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