# -*- coding: utf-8 -*-
"""
The file auto generated by tool genapi, Do not modify.
"""

import json
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

class LoginResponse:
	"""
	登录
	"""
	def __init__(self) -> None:
		self._token = ""  # token
		self._token_u = 0  # token设置标识
		pass


	# token
	def set_token(self, token):
		self._token = token
		self._token_u = 1


	@property
	def is_set_token(self):
		return self._token_u != 0


	@property
	def token(self):
		return self._token


	def to_dict(self) -> dict:
		"""
		Convert object to dict and return
		"""
		data_dict = {}
		data_dict["token"] = self._token  # token

		return data_dict


	def to_obj(self, data_dict: dict):
		"""
		Convert dict to object
		"""

		# check params
		if len( data_dict.get("token") ) < 1:
			raise Exception("param:token error, out of range min:1!")
		if len( data_dict.get("token") ) > 32:
			raise Exception("param:token error, out of range max:32!")

		# parse params
		self.set_token( data_dict.get("token") )  # token


	def to_json(self):
		"""
		Convert object to object
		"""
		return json.dumps( self.to_dict() )