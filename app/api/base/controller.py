import traceback
from typing import Dict
from flask.views import MethodView
from flask import request, jsonify

from common.exception import MyException
from common.result_code import ERR_SYSTEM_BUSY, SUCCESS, CustomStatus
from common.logger import logger
from config import ENV


def response(status: CustomStatus, data=None):
    result = {
        "code": status.code,
        "message": status.message,
        "data": data
    }
    return result


class BaseView(MethodView):
    request_protocol = None  # 请求协议类
    response_protocol = None  # 应答协议类
    view_func = {
        "get": None,  # List all users or Show a single auth
        "post": None,  # Create a new auth
        "put": None,  # 如果该更新对应的URI多次调用的结果一致，则PUT。如果每次提交相同的内容，最终结果不一致的时候，用POST
        "delete": None,  # Delete a auth
        "path": None  # Update a auth
    }

    def call_view_func(self, request_dict: Dict, handler):
        request_obj = self.request_protocol()
        response_obj = self.response_protocol()
        if callable(handler):
            try:
                request_obj.to_obj(request_dict)
                handler(request_obj, response_obj)
                return jsonify(response(SUCCESS, response_obj.to_dict()))
            except MyException as e:
                logger.error(e)
                return jsonify(response(CustomStatus(e.code, e.message)))
            except Exception as e:
                print(ENV)
                if not ENV or ENV == 'dev':
                    raise e
                logger.error(traceback.format_exc())
                logger.error(f"系统异常:{e}")
                print(e)
                return jsonify(response(ERR_SYSTEM_BUSY))
        else:
            return jsonify(response(ERR_SYSTEM_BUSY))

    def get(self):
        print(request.args.to_dict())
        request_dict = request.args.to_dict()
        return self.call_view_func(request_dict, self.view_func.get("get"))

    def post(self):
        request_dict = request.get_json()
        return self.call_view_func(request_dict, self.view_func.get("post"))

    def put(self):
        pass

    def delete(self):
        pass
