# -*- coding: utf-8 -*-
"""
The file auto generated by tool genapi, Do not modify.
"""

from app.api.base.controller import BaseView
from app.api.demo.service import DemoService
from middleware.decorator import *

from external.protocol.python.add_demo_request import AddDemoRequest
from external.protocol.python.add_demo_response import AddDemoResponse
from external.protocol.python.alter_demo_request import AlterDemoRequest
from external.protocol.python.alter_demo_response import AlterDemoResponse
from external.protocol.python.delete_demo_request import DeleteDemoRequest
from external.protocol.python.delete_demo_response import DeleteDemoResponse
from external.protocol.python.query_demo_request import QueryDemoRequest
from external.protocol.python.query_demo_response import QueryDemoResponse
from external.protocol.python.query_demos_request import QueryDemosRequest
from external.protocol.python.query_demos_response import QueryDemosResponse


class AddDemoView(BaseView):

    methods = ["POST"]  # 允许的请求方式
    request_protocol  = AddDemoRequest
    response_protocol = AddDemoResponse
    view_func = {
		"post": DemoService.add_demo
	}


class QueryDemoView(BaseView):

    methods = ["GET"]  # 允许的请求方式
    request_protocol  = QueryDemoRequest
    response_protocol = QueryDemoResponse
    view_func = {
		"get": DemoService.query_demo
	}


class QueryDemosView(BaseView):

    methods = ["POST"]  # 允许的请求方式
    request_protocol  = QueryDemosRequest
    response_protocol = QueryDemosResponse
    view_func = {
		"post": DemoService.query_demos
	}


class AlterDemoView(BaseView):

    methods = ["POST"]  # 允许的请求方式
    request_protocol  = AlterDemoRequest
    response_protocol = AlterDemoResponse
    view_func = {
		"post": DemoService.alter_demo
	}


class DeleteDemoView(BaseView):

    methods = ["POST"]  # 允许的请求方式
    request_protocol  = DeleteDemoRequest
    response_protocol = DeleteDemoResponse
    view_func = {
		"post": DemoService.delete_demo
	}

