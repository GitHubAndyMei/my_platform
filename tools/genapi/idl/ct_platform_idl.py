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
    service(comment="示例服务", owner="andy.mei@momenta.ai")
    API(
        api(method="post", url="/api/v1/demo/add_demo", comment="添加demo"),
        request(
            param(name="name", type="string", min="1", max="32",   comment=u"姓名"),
            param(name="age",  type="int",    min="0", max="200",  comment=u"年龄")
        ),
        response(
            param(name="name", type="string", min="1", max="32",   comment=u"姓名"),
            param(name="age",  type="int",    min="0", max="9999", comment=u"年龄")
        )
    )
    API(
        api(method="get", url="/api/v1/demo/query_demo", comment="查询demo"),
        request(
            param(name="name", type="string", min="1", max="32",   comment=u"姓名"),
            param(name="age",  type="string", min="0", max="200",  comment=u"年龄")
        ),
        response(
            param(name="name", type="string", min="1", max="32",   comment=u"姓名"),
            param(name="age",  type="string", min="0", max="9999", comment=u"年龄")
        )
    )
    API(
        api(method="post", url="/api/v1/demo/query_demos", comment="查询demo列表"),
        request(
            param(name="name", type="string", min="1", max="32",   comment=u"姓名"),
            param(name="age",  type="int",    min="0", max="200",  comment=u"年龄")
        ),
        response(
            param(name="name", type="string", min="1", max="32",   comment=u"姓名"),
            param(name="age",  type="int",    min="0", max="9999", comment=u"年龄")
        )
    )
    API(
        api(method="post", url="/api/v1/demo/alter_demo", comment="修改demo"),
        request(
            param(name="name", type="string", min="1", max="32",   comment=u"姓名"),
            param(name="age",  type="int",    min="0", max="200",  comment=u"年龄")
        ),
        response(
            param(name="name", type="string", min="1", max="32",   comment=u"姓名"),
            param(name="age",  type="int",    min="0", max="9999", comment=u"年龄")
        )
    )
    API(
        api(method="post", url="/api/v1/demo/delete_demo", comment="删除demo"),
        request(
            param(name="name", type="string", min="1", max="32",   comment=u"姓名"),
            param(name="age",  type="int",    min="0", max="200",  comment=u"年龄")
        ),
        response(
            param(name="name", type="string", min="1", max="32",   comment=u"姓名"),
            param(name="age",  type="int",    min="0", max="9999", comment=u"年龄")
        )
    )
    API(
        api(method="post", url="/api/v1/login", comment="登录"),
        request(
            param(name="username", type="string", min="1", max="32", comment=u"用户名"),
            param(name="password", type="string", min="1", max="32", comment=u"密码")
        ),
        response(
            param(name="jwt", type="string", min="1", max="32", comment=u"jwt"),
        )
    )