# 					CT平台接口协议

## 1.示例服务


### 1.接口: 添加demo
**类型:  **

**url: /api/v1/demo/add_demo **

**request:**
| 代码 | 数据类型 | 最小值 | 最大值 | 备注 | 默认值 |
| - | - | - | - | - | - |
| name|string|1|32|姓名|""|
| age|int|0|200|年龄|0|

**请求示例：**
```json
{
	"name":"",
	"age":0
}
```



**response：**
| 代码 | 数据类型 | 最小值 | 最大值 | 备注 | 默认值 |
| - | - | - | - | - | - |
| name|string|1|32|姓名|""|
| age|int|0|9999|年龄|0|

**应答示例：**
```json
{
	"name":"",
	"age":0
}
```



### 2.接口: 查询demo
**类型:  **

**url: /api/v1/demo/query_demo **

**request:**
| 代码 | 数据类型 | 最小值 | 最大值 | 备注 | 默认值 |
| - | - | - | - | - | - |
| name|string|1|32|姓名|""|
| age|string|0|200|年龄|""|

**请求示例：**
```json
{
	"name":"",
	"age":""
}
```



**response：**
| 代码 | 数据类型 | 最小值 | 最大值 | 备注 | 默认值 |
| - | - | - | - | - | - |
| name|string|1|32|姓名|""|
| age|string|0|9999|年龄|""|

**应答示例：**
```json
{
	"name":"",
	"age":""
}
```



### 3.接口: 查询demo列表
**类型:  **

**url: /api/v1/demo/query_demos **

**request:**
| 代码 | 数据类型 | 最小值 | 最大值 | 备注 | 默认值 |
| - | - | - | - | - | - |
| name|string|1|32|姓名|""|
| age|int|0|200|年龄|0|

**请求示例：**
```json
{
	"name":"",
	"age":0
}
```



**response：**
| 代码 | 数据类型 | 最小值 | 最大值 | 备注 | 默认值 |
| - | - | - | - | - | - |
| name|string|1|32|姓名|""|
| age|int|0|9999|年龄|0|

**应答示例：**
```json
{
	"name":"",
	"age":0
}
```



### 4.接口: 修改demo
**类型:  **

**url: /api/v1/demo/alter_demo **

**request:**
| 代码 | 数据类型 | 最小值 | 最大值 | 备注 | 默认值 |
| - | - | - | - | - | - |
| name|string|1|32|姓名|""|
| age|int|0|200|年龄|0|

**请求示例：**
```json
{
	"name":"",
	"age":0
}
```



**response：**
| 代码 | 数据类型 | 最小值 | 最大值 | 备注 | 默认值 |
| - | - | - | - | - | - |
| name|string|1|32|姓名|""|
| age|int|0|9999|年龄|0|

**应答示例：**
```json
{
	"name":"",
	"age":0
}
```



### 5.接口: 删除demo
**类型:  **

**url: /api/v1/demo/delete_demo **

**request:**
| 代码 | 数据类型 | 最小值 | 最大值 | 备注 | 默认值 |
| - | - | - | - | - | - |
| name|string|1|32|姓名|""|
| age|int|0|200|年龄|0|

**请求示例：**
```json
{
	"name":"",
	"age":0
}
```



**response：**
| 代码 | 数据类型 | 最小值 | 最大值 | 备注 | 默认值 |
| - | - | - | - | - | - |
| name|string|1|32|姓名|""|
| age|int|0|9999|年龄|0|

**应答示例：**
```json
{
	"name":"",
	"age":0
}
```






## 2.认证服务


### 6.接口: 登录
**类型:  **

**url: /api/v1/login **

**request:**
| 代码 | 数据类型 | 最小值 | 最大值 | 备注 | 默认值 |
| - | - | - | - | - | - |
| user_name|string|1|64|用户名称|""|
| password|string|1|64|密码|""|

**请求示例：**
```json
{
	"user_name":"",
	"password":""
}
```



**response：**
| 代码 | 数据类型 | 最小值 | 最大值 | 备注 | 默认值 |
| - | - | - | - | - | - |
| jwt|string|1|32|jwt|""|

**应答示例：**
```json
{
	"jwt":""
}
```



### 7.接口: 注册
**类型:  **

**url: /api/v1/register **

**request:**
| 代码 | 数据类型 | 最小值 | 最大值 | 备注 | 默认值 |
| - | - | - | - | - | - |
| user_name|string|1|64|用户名称|""|
| password|string|1|64|密码|""|

**请求示例：**
```json
{
	"user_name":"",
	"password":""
}
```



**response：**
| 代码 | 数据类型 | 最小值 | 最大值 | 备注 | 默认值 |
| - | - | - | - | - | - |

**应答示例：**
```json
{
}
```






## 3.权限服务


### 8.接口: 添加角色
**类型:  **

**url: /api/v1/RBAC/add_role **

**request:**
| 代码 | 数据类型 | 最小值 | 最大值 | 备注 | 默认值 |
| - | - | - | - | - | - |
| role_code|string|1|64|角色代码|""|
| role_name|string|1|64|角色名称|""|
| is_admin|int|0|1|是否是管理员|0|
| status|int|0|2|角色状态 enum:0,ensure,待审核#1,normal,正常#2,stop,禁用|0|

**请求示例：**
```json
{
	"role_code":"",
	"role_name":"",
	"is_admin":0,
	"status":0
}
```



**response：**
| 代码 | 数据类型 | 最小值 | 最大值 | 备注 | 默认值 |
| - | - | - | - | - | - |

**应答示例：**
```json
{
}
```



### 9.接口: 删除角色
**类型:  **

**url: /api/v1/RBAC/delete_role **

**request:**
| 代码 | 数据类型 | 最小值 | 最大值 | 备注 | 默认值 |
| - | - | - | - | - | - |
| role_code|string|1|64|角色代码|""|

**请求示例：**
```json
{
	"role_code":""
}
```



**response：**
| 代码 | 数据类型 | 最小值 | 最大值 | 备注 | 默认值 |
| - | - | - | - | - | - |

**应答示例：**
```json
{
}
```



### 10.接口: 修改角色
**类型:  **

**url: /api/v1/RBAC/alter_role **

**request:**
| 代码 | 数据类型 | 最小值 | 最大值 | 备注 | 默认值 |
| - | - | - | - | - | - |
| role_code|string|1|64|角色代码|""|
| role_name|string|1|64|角色名称|""|
| is_admin|int|0|1|是否是管理员|0|
| status|int|0|2|角色状态 enum:0,ensure,待审核#1,normal,正常#2,stop,禁用|0|

**请求示例：**
```json
{
	"role_code":"",
	"role_name":"",
	"is_admin":0,
	"status":0
}
```



**response：**
| 代码 | 数据类型 | 最小值 | 最大值 | 备注 | 默认值 |
| - | - | - | - | - | - |

**应答示例：**
```json
{
}
```



### 11.接口: 查询角色列表
**类型:  **

**url: /api/v1/RBAC/query_roles **

**request:**
| 代码 | 数据类型 | 最小值 | 最大值 | 备注 | 默认值 |
| - | - | - | - | - | - |
| role_name|string|1|64|角色名称|""|
| status|int|0|2|角色状态 enum:0,ensure,待审核#1,normal,正常#2,stop,禁用|0|

**请求示例：**
```json
{
	"role_name":"",
	"status":0
}
```



**response：**
| 代码 | 数据类型 | 最小值 | 最大值 | 备注 | 默认值 |
| - | - | - | - | - | - |
| roles|vector<RoleDetail>|||角色列表|[]|

**应答示例：**
```json
{
	"roles":[]
}
```



### 12.接口: 增加权限
**类型:  **

**url: /api/v1/RBAC/add_permission **

**request:**
| 代码 | 数据类型 | 最小值 | 最大值 | 备注 | 默认值 |
| - | - | - | - | - | - |

**请求示例：**
```json
{
}
```



**response：**
| 代码 | 数据类型 | 最小值 | 最大值 | 备注 | 默认值 |
| - | - | - | - | - | - |

**应答示例：**
```json
{
}
```



### 13.接口: 删除权限
**类型:  **

**url: /api/v1/RBAC/delete_permission **

**request:**
| 代码 | 数据类型 | 最小值 | 最大值 | 备注 | 默认值 |
| - | - | - | - | - | - |

**请求示例：**
```json
{
}
```



**response：**
| 代码 | 数据类型 | 最小值 | 最大值 | 备注 | 默认值 |
| - | - | - | - | - | - |

**应答示例：**
```json
{
}
```



### 14.接口: 修改权限
**类型:  **

**url: /api/v1/RBAC/alter_permission **

**request:**
| 代码 | 数据类型 | 最小值 | 最大值 | 备注 | 默认值 |
| - | - | - | - | - | - |

**请求示例：**
```json
{
}
```



**response：**
| 代码 | 数据类型 | 最小值 | 最大值 | 备注 | 默认值 |
| - | - | - | - | - | - |

**应答示例：**
```json
{
}
```



### 15.接口: 查询权限列表
**类型:  **

**url: /api/v1/RBAC/query_permissions **

**request:**
| 代码 | 数据类型 | 最小值 | 最大值 | 备注 | 默认值 |
| - | - | - | - | - | - |

**请求示例：**
```json
{
}
```



**response：**
| 代码 | 数据类型 | 最小值 | 最大值 | 备注 | 默认值 |
| - | - | - | - | - | - |

**应答示例：**
```json
{
}
```



### 16.接口: 添加角色权限
**类型:  **

**url: /api/v1/RBAC/add_user_permission **

**request:**
| 代码 | 数据类型 | 最小值 | 最大值 | 备注 | 默认值 |
| - | - | - | - | - | - |

**请求示例：**
```json
{
}
```



**response：**
| 代码 | 数据类型 | 最小值 | 最大值 | 备注 | 默认值 |
| - | - | - | - | - | - |

**应答示例：**
```json
{
}
```



### 17.接口: 删除角色权限
**类型:  **

**url: /api/v1/RBAC/delete_user_permission **

**request:**
| 代码 | 数据类型 | 最小值 | 最大值 | 备注 | 默认值 |
| - | - | - | - | - | - |

**请求示例：**
```json
{
}
```



**response：**
| 代码 | 数据类型 | 最小值 | 最大值 | 备注 | 默认值 |
| - | - | - | - | - | - |

**应答示例：**
```json
{
}
```



### 18.接口: 查询角色权限
**类型:  **

**url: /api/v1/RBAC/query_user_permissions **

**request:**
| 代码 | 数据类型 | 最小值 | 最大值 | 备注 | 默认值 |
| - | - | - | - | - | - |

**请求示例：**
```json
{
}
```



**response：**
| 代码 | 数据类型 | 最小值 | 最大值 | 备注 | 默认值 |
| - | - | - | - | - | - |

**应答示例：**
```json
{
}
```



### 19.接口: 添加用户角色
**类型:  **

**url: /api/v1/RBAC/add_user_role **

**request:**
| 代码 | 数据类型 | 最小值 | 最大值 | 备注 | 默认值 |
| - | - | - | - | - | - |
| user_account|string|1|64|用户账号|""|
| role_code|string|1|64|角色代码|""|

**请求示例：**
```json
{
	"user_account":"",
	"role_code":""
}
```



**response：**
| 代码 | 数据类型 | 最小值 | 最大值 | 备注 | 默认值 |
| - | - | - | - | - | - |

**应答示例：**
```json
{
}
```



### 20.接口: 删除用户角色
**类型:  **

**url: /api/v1/RBAC/delete_user_role **

**request:**
| 代码 | 数据类型 | 最小值 | 最大值 | 备注 | 默认值 |
| - | - | - | - | - | - |
| user_account|string|1|64|用户账号|""|
| role_code|string|1|64|角色代码|""|

**请求示例：**
```json
{
	"user_account":"",
	"role_code":""
}
```



**response：**
| 代码 | 数据类型 | 最小值 | 最大值 | 备注 | 默认值 |
| - | - | - | - | - | - |

**应答示例：**
```json
{
}
```



### 21.接口: 查询用户角色
**类型:  **

**url: /api/v1/RBAC/query_user_roles **

**request:**
| 代码 | 数据类型 | 最小值 | 最大值 | 备注 | 默认值 |
| - | - | - | - | - | - |
| user_account|string|1|64|用户账号|""|

**请求示例：**
```json
{
	"user_account":""
}
```



**response：**
| 代码 | 数据类型 | 最小值 | 最大值 | 备注 | 默认值 |
| - | - | - | - | - | - |
| roles|vector<RoleDetail>|||角色列表|[]|

**应答示例：**
```json
{
	"roles":[]
}
```






## 4.公共数据结构

### 1.RoleDetail: 角色详情

| 代码 | 数据类型 | 最小值 | 最大值 | 备注 | 默认值 |
| - | - | - | - | - | - |
| role_code|string|1|64|角色代码|""|
| role_name|string|1|64|角色名称|""|
| is_admin|int|0|1|是否是管理员 enum:0,no,不是#1,yes,是|0|
| status|int|0|2|角色状态 enum:0,ensure,待审核#1,normal,正常#2,stop,禁用|0|

**示例：**
```json
{
	"role_code":"",
	"role_name":"",
	"is_admin":0,
	"status":0
}
```



### 2.PermissionDetail: 权限详情

| 代码 | 数据类型 | 最小值 | 最大值 | 备注 | 默认值 |
| - | - | - | - | - | - |
| role_code|string|1|64|角色代码|""|
| role_name|string|1|64|角色名称|""|
| is_admin|int|0|1|是否是管理员 enum:0,no,不是#1,yes,是|0|
| status|int|0|2|角色状态 enum:0,ensure,待审核#1,normal,正常#2,stop,禁用|0|

**示例：**
```json
{
	"role_code":"",
	"role_name":"",
	"is_admin":0,
	"status":0
}
```



