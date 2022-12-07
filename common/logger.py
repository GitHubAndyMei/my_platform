# -*- coding: utf-8 -*-
import logging

logger = logging.getLogger("logger")
logger.setLevel(logging.INFO)

handler = logging.FileHandler("log/ct_platform.log")
handler.setFormatter(logging.Formatter("%(asctime)s|%(levelname)s|%(filename)s %(funcName)s %(lineno)s|%(message)s"))

logger.addHandler(handler)