# -*- coding: utf-8 -*-
"""
The file auto generated by tool genapi, Do not modify.
"""

import json
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from role_detail import *

class QueryRolesResponse:
	"""
	查询角色列表
	"""
	def __init__(self) -> None:
		self._roles = []  # 角色列表
		self._roles_u = 0  # 角色列表设置标识
		pass


	# 角色列表
	def set_roles(self, roles):
		self._roles = roles
		self._roles_u = 1


	@property
	def is_set_roles(self):
		return self._roles_u != 0


	@property
	def roles(self):
		return self._roles


	def to_dict(self) -> dict:
		"""
		Convert object to dict and return
		"""
		data_dict = {}
		data_dict["roles"] = []
		for node in self._roles:
			data_dict["roles"].append( node.to_dict() )  # 角色列表

		return data_dict


	def to_obj(self, data_dict: dict):
		"""
		Convert dict to object
		"""

		# check params

		# parse params
		for node in data_dict.get("roles"):
			obj = RoleDetail()
			obj.to_obj(node)
			self._roles.append(obj)  # 角色列表
			self._roles_u = 1


	def to_json(self):
		"""
		Convert object to object
		"""
		return json.dumps( self.to_dict() )