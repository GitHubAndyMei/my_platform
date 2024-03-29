# -*- coding: utf-8 -*-
"""
The file auto generated by tool genapi, Do not modify.
"""

import json
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

class AuthorityListRequest:
	"""
	权限列表
	"""
	def __init__(self) -> None:
		self._user_name = ""  # 用户名
		self._user_name_u = 0  # 用户名设置标识
		self._password = ""  # 密码
		self._password_u = 0  # 密码设置标识
		pass


	# 用户名
	def set_user_name(self, user_name):
		self._user_name = user_name
		self._user_name_u = 1


	@property
	def is_set_user_name(self):
		return self._user_name_u != 0


	@property
	def user_name(self):
		return self._user_name


	# 密码
	def set_password(self, password):
		self._password = password
		self._password_u = 1


	@property
	def is_set_password(self):
		return self._password_u != 0


	@property
	def password(self):
		return self._password


	def to_dict(self) -> dict:
		"""
		Convert object to dict and return
		"""
		data_dict = {}
		data_dict["user_name"] = self._user_name  # 用户名
		data_dict["password"] = self._password  # 密码

		return data_dict


	def to_obj(self, data_dict: dict):
		"""
		Convert dict to object
		"""

		# check params
		if len( data_dict.get("user_name") ) < 1:
			raise Exception("param:user_name error, out of range min:1!")
		if len( data_dict.get("user_name") ) > 32:
			raise Exception("param:user_name error, out of range max:32!")
		if len( data_dict.get("password") ) < 1:
			raise Exception("param:password error, out of range min:1!")
		if len( data_dict.get("password") ) > 32:
			raise Exception("param:password error, out of range max:32!")

		# parse params
		self.set_user_name( data_dict.get("user_name") )  # 用户名
		self.set_password( data_dict.get("password") )  # 密码


	def to_json(self):
		"""
		Convert object to object
		"""
		return json.dumps( self.to_dict() )