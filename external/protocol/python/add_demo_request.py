# -*- coding: utf-8 -*-
"""
The file auto generated by tool genapi, Do not modify.
"""

import json
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

class AddDemoRequest:
	"""
	添加demo
	"""
	def __init__(self) -> None:
		self._name = ""  # 姓名
		self._name_u = 0  # 姓名设置标识
		self._age = 0  # 年龄
		self._age_u = 0  # 年龄设置标识
		pass


	# 姓名
	def set_name(self, name):
		self._name = name
		self._name_u = 1


	@property
	def is_set_name(self):
		return self._name_u != 0


	@property
	def name(self):
		return self._name


	# 年龄
	def set_age(self, age):
		self._age = age
		self._age_u = 1


	@property
	def is_set_age(self):
		return self._age_u != 0


	@property
	def age(self):
		return self._age


	def to_dict(self) -> dict:
		"""
		Convert object to dict and return
		"""
		data_dict = {}
		data_dict["name"] = self._name  # 姓名
		data_dict["age"] = self._age  # 年龄

		return data_dict


	def to_obj(self, data_dict: dict):
		"""
		Convert dict to object
		"""

		# check params
		if len( data_dict.get("name") ) < 1:
			raise Exception("param:name error, out of range min:1!")
		if len( data_dict.get("name") ) > 32:
			raise Exception("param:name error, out of range max:32!")
		if data_dict.get("age") < 0:
			raise Exception("param:age error, out of range min:0!")
		if data_dict.get("age") > 200:
			raise Exception("param:age error, out of range max:200!")

		# parse params
		self.set_name( data_dict.get("name") )  # 姓名
		self.set_age( data_dict.get("age") )  # 年龄


	def to_json(self):
		"""
		Convert object to object
		"""
		return json.dumps( self.to_dict() )