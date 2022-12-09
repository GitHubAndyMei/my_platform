# -*- coding: utf-8 -*-
import logging
from config import LOG_PATH

logger = logging.getLogger("logger")
logger.setLevel(logging.INFO)

handler = logging.FileHandler(f"{LOG_PATH}/ct_platform.log")
handler.setFormatter(logging.Formatter("%(asctime)s|%(levelname)s|%(filename)s %(funcName)s %(lineno)s|%(message)s"))

logger.addHandler(handler)