# -*- coding: utf-8 -*-
"""
The file auto generated by tool genapi, Do not modify.
"""

import json
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

class MenuCreateRequest:
	"""
	菜单创建
	"""
	def __init__(self) -> None:
		self._menu_name = ""  # 菜单名称
		self._menu_name_u = 0  # 菜单名称设置标识
		self._icon = ""  # 图标
		self._icon_u = 0  # 图标设置标识
		self._parent_code = ""  # 图标
		self._parent_code_u = 0  # 图标设置标识
		pass


	# 菜单名称
	def set_menu_name(self, menu_name):
		self._menu_name = menu_name
		self._menu_name_u = 1


	@property
	def is_set_menu_name(self):
		return self._menu_name_u != 0


	@property
	def menu_name(self):
		return self._menu_name


	# 图标
	def set_icon(self, icon):
		self._icon = icon
		self._icon_u = 1


	@property
	def is_set_icon(self):
		return self._icon_u != 0


	@property
	def icon(self):
		return self._icon


	# 图标
	def set_parent_code(self, parent_code):
		self._parent_code = parent_code
		self._parent_code_u = 1


	@property
	def is_set_parent_code(self):
		return self._parent_code_u != 0


	@property
	def parent_code(self):
		return self._parent_code


	def to_dict(self) -> dict:
		"""
		Convert object to dict and return
		"""
		data_dict = {}
		data_dict["menu_name"] = self._menu_name  # 菜单名称
		data_dict["icon"] = self._icon  # 图标
		data_dict["parent_code"] = self._parent_code  # 图标

		return data_dict


	def to_obj(self, data_dict: dict):
		"""
		Convert dict to object
		"""

		# check params
		if len( data_dict.get("menu_name") ) < 1:
			raise Exception("param:menu_name error, out of range min:1!")
		if len( data_dict.get("menu_name") ) > 32:
			raise Exception("param:menu_name error, out of range max:32!")
		if len( data_dict.get("icon") ) < 0:
			raise Exception("param:icon error, out of range min:0!")
		if len( data_dict.get("icon") ) > 32:
			raise Exception("param:icon error, out of range max:32!")
		if len( data_dict.get("parent_code") ) < 0:
			raise Exception("param:parent_code error, out of range min:0!")
		if len( data_dict.get("parent_code") ) > 32:
			raise Exception("param:parent_code error, out of range max:32!")

		# parse params
		self.set_menu_name( data_dict.get("menu_name") )  # 菜单名称
		self.set_icon( data_dict.get("icon") )  # 图标
		self.set_parent_code( data_dict.get("parent_code") )  # 图标


	def to_json(self):
		"""
		Convert object to object
		"""
		return json.dumps( self.to_dict() )