"""
Protocol of web api module.
Using self interface data language. You need to use genapi to parse
"""
import sys

sys.path.append("..")
from info import *
from service import *
from API import *
from request import *
from response import *
from param import *

'''
api(url, comment, function)
	url    : 接口地址
	comment: 接口备注
	function : 接口处理方法,为空或不传默认取url最后一个分割为api调用方法名

param(name, type, min, max, comment)
	name: 字段名称
	type: 字段类型
	min : 字段最小值(数值, 字符串类型有效)
	max : 字段最大值(数值, 字符串类型有效)
	comment: 字段备注

param参数说明:
	type:类型字段,string,int,uint32_t,int64_t,uint64_t,double,float,vector(列表),自定义类型(字典)
	min=MIN max=MAX表示不检查数据长度,当类型为string时检查字符串长度,数值类型检查数值上下限

Note:
    1.功能名不能使用insert update delete select数据库保留字符.
    2.建议使用query-查询 add-增加 alter-修改 drop-删除, 其他功能请使用自定义动词
'''


class Demo:
    service(comment="示例服务", owner="andy.mei")
    API(
        api(method="post", url="/api/v1/demo/add_demo", comment="增加demo"),
        request(
            param(name="name", type="string", min="1", max="64",  comment=u"姓名"),
            param(name="age",  type="int",    min="0", max="200", comment=u"年龄")
        ),
        response(
        )
    )
    API(
        api(method="post", url="/api/v1/demo/delete_demo", comment="删除demo"),
        request(
            param(name="name", type="string", min="1", max="32", comment=u"姓名"),
        ),
        response(
        )
    )
    API(
        api(method="post", url="/api/v1/demo/alter_demo", comment="修改demo"),
        request(
            param(name="name", type="string", min="1", max="32",  comment=u"姓名"),
            param(name="age",  type="int",    min="0", max="200", comment=u"年龄")
        ),
        response(
        )
    )
    API(
        api(method="post", url="/api/v1/demo/query_demos", comment="查询demo列表"),
        request(
        ),
        response(
            param(name="names", type="vector<string>", min="MIN", max="MAX", comment=u"姓名列表"),
        )
    )



class RoleDetail:
    info(comment="角色详情")
    param(name="role_code", type="string", min="1", max="64", comment=u"角色代码"),
    param(name="role_name", type="string", min="1", max="64", comment=u"角色名称"),

class PermissionDetail:
    info(comment="权限详情")
    param(name="permission_code", type="string", min="1", max="64", comment=u"角色代码"),
    param(name="permission_name", type="string", min="1", max="64", comment=u"角色名称"),
    param(name="url",  type="int",    min="0", max="1",  comment=u"是否是管理员 enum:0,no,不是#1,yes,是")

class RBAC:
    service(comment="权限服务", owner="施意波")
    # 角色接口
    API(
        api(method="post", url="/api/v1/RBAC/add_role",    comment="增加角色"),
        request(
            param(name="role_name", type="string", min="1", max="64", comment=u"角色名称"),
        ),
        response(
        )
    )
    API(
        api(method="post", url="/api/v1/RBAC/delete_role", comment="删除角色"),
        request(
            param(name="role_code", type="string", min="1", max="64", comment=u"角色代码")
        ),
        response(
        )
    )
    API(
        api(method="post", url="/api/v1/RBAC/alter_role",  comment="修改角色"),
        request(
            param(name="role_code", type="string", min="1", max="64", comment=u"角色代码"),
            param(name="role_name", type="string", min="1", max="64", comment=u"角色名称"),
            param(name="is_admin",  type="int",    min="0", max="1",  comment=u"是否是管理员"),
            param(name="status",    type="int",    min="0", max="2",  comment=u"角色状态 enum:0,ensure,待审核#1,normal,正常#2,stop,禁用")
        ),
        response(
        )
    )
    API(
        api(method="post", url="/api/v1/RBAC/query_roles", comment="查询角色列表"),
        request(

        ),
        response(
            param(name="roles", type="vector<RoleDetail>", min="MIN", max="MAX", comment=u"角色列表"),
        )
    )

    # 权限接口
    API(
        api(method="post", url="/api/v1/RBAC/add_permission",    comment="增加权限"),
        request(
            param(name="permission_name", type="string", min="1", max="64", comment=u"角色代码"),
            param(name="url", type="string", min="1", max="64", comment=u"角色名称")
        ),
        response(
        )
    )
    API(
        api(method="post", url="/api/v1/RBAC/delete_permission", comment="删除权限"),
        request(
            param(name="permission_code", type="string", min="1", max="64", comment=u"角色代码"),

        ),
        response(
        )
    )
    API(
        api(method="post", url="/api/v1/RBAC/query_permissions", comment="查询权限列表"),
        request(
        ),
        response(
            param(name="permissions", type="vector<PermissionDetail>", min="MIN", max="MAX", comment=u"角色列表"),

        )
    )

    # 角色权限接口
    API(
        api(method="post", url="/api/v1/RBAC/add_user_permission",    comment="增加角色权限"),
        request(
        ),
        response(
        )
    )
    API(
        api(method="post", url="/api/v1/RBAC/delete_user_permission", comment="删除角色权限"),
        request(
        ),
        response(
        )
    )
    API(
        api(method="post", url="/api/v1/RBAC/query_user_permissions", comment="查询角色权限"),
        request(
        ),
        response(
        )
    )

    # 用户角色接口
    API(
        api(method="post", url="/api/v1/RBAC/add_user_role",   comment="增加用户角色"),
        request(
            param(name="user_account", type="string", min="1", max="64", comment=u"用户账号"),
            param(name="role_code",    type="string", min="1", max="64", comment=u"角色代码")
        ),
        response(
        )
    )
    API(
        api(method="post", url="/api/v1/RBAC/delete_user_role", comment="删除用户角色"),
        request(
            param(name="user_account", type="string", min="1", max="64", comment=u"用户账号"),
            param(name="role_code",    type="string", min="1", max="64", comment=u"角色代码")
        ),
        response(
        )
    )
    API(
        api(method="post", url="/api/v1/RBAC/query_user_roles", comment="查询用户角色"),
        request(
            param(name="user_account", type="string",             min="1",   max="64", comment=u"用户账号"),
        ),
        response(
            param(name="roles",        type="vector<RoleDetail>", min="MIN", max="MAX",  comment=u"角色列表"),
        )
    )


class Auth:
    service(comment="认证服务", owner="施意波")
    API(
        api(method="post", url="/api/v1/login", comment="登录"),
        request(
            param(name="username", type="string", min="1", max="64", comment=u"用户名称"),
            param(name="password",  type="string", min="1", max="64", comment=u"密码")
        ),
        response(
            param(name="token", type="string", min="1", max="32", comment=u"token"),
        )
    )
    API(
        api(method="post", url="/api/v1/register", comment="注册"),
        request(
            param(name="username", type="string", min="1", max="64", comment=u"用户名称"),
            param(name="password",  type="string", min="1", max="64", comment=u"密码")
        ),
        response(
        )
    )
    API(
        api(method="post", url="/api/v1/get_user_info", comment="获取用户信息"),
        request(
        ),
        response(
            param(name="desc", type="string", min="1", max="32", comment=u"desc"),
            param(name="username", type="string", min="1", max="32", comment=u"desc"),
            param(name="roles", type="vector<RoleDetail>", min="MIN", max="MAX", comment=u"角色列表"),
        )
    )

