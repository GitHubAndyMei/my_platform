# -*- coding: utf-8 -*-
"""
The file auto generated by tool genapi, Do not modify.
"""

from app.api.base.controller import BaseView
from app.api.rbac.service import RBACService
from middleware.decorator import *

from external.protocol.python.add_permission_request import AddPermissionRequest
from external.protocol.python.add_permission_response import AddPermissionResponse
from external.protocol.python.add_role_request import AddRoleRequest
from external.protocol.python.add_role_response import AddRoleResponse
from external.protocol.python.add_user_permission_request import AddUserPermissionRequest
from external.protocol.python.add_user_permission_response import AddUserPermissionResponse
from external.protocol.python.add_user_role_request import AddUserRoleRequest
from external.protocol.python.add_user_role_response import AddUserRoleResponse
from external.protocol.python.alter_permission_request import AlterPermissionRequest
from external.protocol.python.alter_permission_response import AlterPermissionResponse
from external.protocol.python.alter_role_request import AlterRoleRequest
from external.protocol.python.alter_role_response import AlterRoleResponse
from external.protocol.python.delete_permission_request import DeletePermissionRequest
from external.protocol.python.delete_permission_response import DeletePermissionResponse
from external.protocol.python.delete_role_request import DeleteRoleRequest
from external.protocol.python.delete_role_response import DeleteRoleResponse
from external.protocol.python.delete_user_permission_request import DeleteUserPermissionRequest
from external.protocol.python.delete_user_permission_response import DeleteUserPermissionResponse
from external.protocol.python.delete_user_role_request import DeleteUserRoleRequest
from external.protocol.python.delete_user_role_response import DeleteUserRoleResponse
from external.protocol.python.query_permissions_request import QueryPermissionsRequest
from external.protocol.python.query_permissions_response import QueryPermissionsResponse
from external.protocol.python.query_roles_request import QueryRolesRequest
from external.protocol.python.query_roles_response import QueryRolesResponse
from external.protocol.python.query_user_permissions_request import QueryUserPermissionsRequest
from external.protocol.python.query_user_permissions_response import QueryUserPermissionsResponse
from external.protocol.python.query_user_roles_request import QueryUserRolesRequest
from external.protocol.python.query_user_roles_response import QueryUserRolesResponse
from external.protocol.python.role_detail import *

class AddRoleView(BaseView):
    """
    增加角色
    """
    methods = ["POST"]  # 允许的请求方式
    request_protocol  = AddRoleRequest
    response_protocol = AddRoleResponse
    view_func = {
        "post": RBACService.add_role
    }

class DeleteRoleView(BaseView):
    """
    删除角色
    """
    methods = ["POST"]  # 允许的请求方式
    request_protocol  = DeleteRoleRequest
    response_protocol = DeleteRoleResponse
    view_func = {
        "post": RBACService.delete_role
    }

class AlterRoleView(BaseView):
    """
    修改角色
    """
    methods = ["POST"]  # 允许的请求方式
    request_protocol  = AlterRoleRequest
    response_protocol = AlterRoleResponse
    view_func = {
        "post": RBACService.alter_role
    }

class QueryRolesView(BaseView):
    """
    查询角色列表
    """
    methods = ["POST"]  # 允许的请求方式
    request_protocol  = QueryRolesRequest
    response_protocol = QueryRolesResponse
    view_func = {
        "post": RBACService.query_roles
    }

class AddPermissionView(BaseView):
    """
    增加权限
    """
    methods = ["POST"]  # 允许的请求方式
    request_protocol  = AddPermissionRequest
    response_protocol = AddPermissionResponse
    view_func = {
        "post": RBACService.add_permission
    }

class DeletePermissionView(BaseView):
    """
    删除权限
    """
    methods = ["POST"]  # 允许的请求方式
    request_protocol  = DeletePermissionRequest
    response_protocol = DeletePermissionResponse
    view_func = {
        "post": RBACService.delete_permission
    }

class AlterPermissionView(BaseView):
    """
    修改权限
    """
    methods = ["POST"]  # 允许的请求方式
    request_protocol  = AlterPermissionRequest
    response_protocol = AlterPermissionResponse
    view_func = {
        "post": RBACService.alter_permission
    }

class QueryPermissionsView(BaseView):
    """
    查询权限列表
    """
    methods = ["POST"]  # 允许的请求方式
    request_protocol  = QueryPermissionsRequest
    response_protocol = QueryPermissionsResponse
    view_func = {
        "post": RBACService.query_permissions
    }

class AddUserPermissionView(BaseView):
    """
    增加角色权限
    """
    methods = ["POST"]  # 允许的请求方式
    request_protocol  = AddUserPermissionRequest
    response_protocol = AddUserPermissionResponse
    view_func = {
        "post": RBACService.add_user_permission
    }

class DeleteUserPermissionView(BaseView):
    """
    删除角色权限
    """
    methods = ["POST"]  # 允许的请求方式
    request_protocol  = DeleteUserPermissionRequest
    response_protocol = DeleteUserPermissionResponse
    view_func = {
        "post": RBACService.delete_user_permission
    }

class QueryUserPermissionsView(BaseView):
    """
    查询角色权限
    """
    methods = ["POST"]  # 允许的请求方式
    request_protocol  = QueryUserPermissionsRequest
    response_protocol = QueryUserPermissionsResponse
    view_func = {
        "post": RBACService.query_user_permissions
    }

class AddUserRoleView(BaseView):
    """
    增加用户角色
    """
    methods = ["POST"]  # 允许的请求方式
    request_protocol  = AddUserRoleRequest
    response_protocol = AddUserRoleResponse
    view_func = {
        "post": RBACService.add_user_role
    }

class DeleteUserRoleView(BaseView):
    """
    删除用户角色
    """
    methods = ["POST"]  # 允许的请求方式
    request_protocol  = DeleteUserRoleRequest
    response_protocol = DeleteUserRoleResponse
    view_func = {
        "post": RBACService.delete_user_role
    }

class QueryUserRolesView(BaseView):
    """
    查询用户角色
    """
    methods = ["POST"]  # 允许的请求方式
    request_protocol  = QueryUserRolesRequest
    response_protocol = QueryUserRolesResponse
    view_func = {
        "post": RBACService.query_user_roles
    }

