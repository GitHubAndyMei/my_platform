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






## 2.权限服务


### 6.接口: 角色创建
**类型:  **

**url: /api/v1/auth/role_create **

**request:**
| 代码 | 数据类型 | 最小值 | 最大值 | 备注 | 默认值 |
| - | - | - | - | - | - |
| role_name|string|1|32|角色名称|""|
| password|string|1|32|密码|""|

**请求示例：**
```json
{
	"role_name":"",
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



### 7.接口: 权限列表
**类型:  **

**url: /api/v1/authority_list **

**request:**
| 代码 | 数据类型 | 最小值 | 最大值 | 备注 | 默认值 |
| - | - | - | - | - | - |
| username|string|1|32|用户名|""|
| password|string|1|32|密码|""|

**请求示例：**
```json
{
	"username":"",
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



### 8.接口: 菜单列表
**类型:  **

**url: /api/v1/menu_list **

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
| menu_list|vector<dict>|||菜单列表|[]|

**应答示例：**
```json
{
	"menu_list":[]
}
```



### 9.接口: 菜单创建
**类型:  **

**url: /api/v1/menu_create **

**request:**
| 代码 | 数据类型 | 最小值 | 最大值 | 备注 | 默认值 |
| - | - | - | - | - | - |
| menu_name|string|1|32|菜单名称|""|
| icon|string|0|32|图标|""|
| parent_code|string|0|32|图标|""|

**请求示例：**
```json
{
	"menu_name":"",
	"icon":"",
	"parent_code":""
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






## 3.认证服务


### 10.接口: 登录
**类型:  **

**url: /api/v1/login **

**request:**
| 代码 | 数据类型 | 最小值 | 最大值 | 备注 | 默认值 |
| - | - | - | - | - | - |
| username|string|1|32|用户名|""|
| password|string|1|32|密码|""|

**请求示例：**
```json
{
	"username":"",
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



### 11.接口: 注册
**类型:  **

**url: /api/v1/register **

**request:**
| 代码 | 数据类型 | 最小值 | 最大值 | 备注 | 默认值 |
| - | - | - | - | - | - |
| username|string|1|32|用户名|""|
| password|string|1|32|密码|""|

**请求示例：**
```json
{
	"username":"",
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






## 4.公共数据结构

