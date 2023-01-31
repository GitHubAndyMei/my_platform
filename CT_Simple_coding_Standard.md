

#                           CT_Simple_Coding_Standard

## 背景

​		python是momenta主要的脚本语言. 这个编码规范主要包含python的基本编程准则, 为保证大家代码风格的一致性, 减少代码阅读的成本, 故设立此规范. 本规范是综合PEP 8和Google Python风格指南, 结合实际的开发经验所设计, 有不足之处请多指正.

​		由于本框架自动化程度比较高, 使用了自动代码生成工具, 所以禁用使用Pylint等格式化插件, 适合自己的才是最好的.



## 1.目录名

### 格式

​	小写+下划线

### 示例

```bash
# 示例
lproj_replay
```





## 2.文件名

### 格式

​	小写+下划线

### 示例

```bash
start_ct.py
```





## 3.全局变量

不推荐使用, 但是某些场景下会用. 定义成模块内部变量, 通过公共函数访问.

### 格式

​	下划线+大写

### 示例

```python
_MOMENTA_CT = "CT"

def get_momenta_ct():
    return _MOMENTA_CT
```





## 4.局部变量

### 格式

​	小写+下划线

### 场景

​	①函数传参

​	②代码中多次使用

​	③只有一个地方使用, 但是语句比较长, 影响代码美观

### **1）Bool(布尔)**

格式: is+下划线+小写

```python
is_empty: bool = False # 是否为空
```



### **2）Numbers(数字)**

格式: 小写+下划线

```python
case_num: int = 0 # 用例数量
```



### **3）float(浮点)**

格式: 小写+下划线

```python
topic_rate: float = 0 # topic帧率
```



### **4）String(字符串)**

格式: 小写+下划线

```python
case_name: str = 0 # 用例名称
```



### **5）List(列表)**

格式: 小写+下划线+s

```python
test_cases: List[object] = [] # 用例信息列表 [TestCase]
```



### **6）Tuple(元组)**

格式: 小写+下划线+tup

```python
test_case_tup: Tuple[object] = () # 用例信息 (TestCase)
```



### **7）Dictionary(字典)**

格式: 小写+下划线+dict

```python
test_case_dict: Dict[str, object] = {}  # 用例信息 {case_name: TestCase}
```



### **8）Set(集合)**

格式: 小写+下划线+dict

```python
test_case_set: set = set()  # 用例信息 {case_name: TestCase}
```





## 5.类

如果一个类不继承自其它类, 就显式的从object继承



### 格式

​	①.类名: 大驼峰

​	②.变量名: 小写+下划线. 不对外暴露请申明为保护或私有. 类变量, 成员变量尽量事先定义好, 虽然python支持运行时定义.

​	③.成员函数: 小写+下划线. 不对外暴露请申明为保护或私有.

​	④.空行: 函数定义之间空2行, 代码块之间空1行.



### 示例

```python
# note: 类名大写
class TestCase(object):
    """
   	类注释
    """
    name: str = "test_case" # 这是一个类变量
    
    def __init__(self) -> None:
        # note: 事先定义, 声明保护!
        self._name: str = "" # 这是一个保护的成员变量.
        self._code: int = 0  # 这是一个保护的成员变量.
       
    
    def _build(self):
        """
        note: 声明保护
        """
        
        
    def _start(self):
        ...
        
        
    # note: 函数定义之间空2行
    def run(self) -> None:
        """
        这是一个公有函数
        """
        # 1.构建
        self._build()
        
        # 2.开始
        self._start()  # note: 代码块之间空1行
        
        # 3.结束
        self._done()
        
        
    def _done(self) -> None:
        ...
     
      
```



## 6.注释

### 1）模块

#### 说明

每个文件应该包含一个许可样板. 根据项目使用的许可(例如, Apache 2.0, BSD, LGPL, GPL), 选择合适的样板. 其开头应是对模块内容和用法的描述.当然

#### 示例

```python
"""

模块说明.

Typical usage example:

foo = ClassFoo()
bar = foo.FunctionBar()
"""

```



### 2）函数

#### 说明

一个函数必须要有文档字符串, 除非它满足以下条件:

1. 外部不可见
2. 非常短小
3. 简单明了



#### 格式

Args:

​	列出每个参数的名字, 并在名字后使用一个冒号和一个空格, 分隔对该参数的描述.如果描述太长超过了单行80字符,使用2或者4个空格的	悬挂缩进(与文件其他部分保持一致). 描述应该包括所需的类型和含义. 如果一个函数接受*foo(可变长度参数列表)或者**bar (任意关键	字参数), 应该详细列出*foo和**bar.

Returns: (或者 Yields: 用于生成器)

​	描述返回值的类型和语义. 如果函数返回None, 这一部分可以省略.

Raises:

​	列出与接口有关的所有异常



#### 示例

```python
def fetch_smalltable_rows(table_handle: smalltable.Table,
                        keys: Sequence[Union[bytes, str]],
                        require_all_keys: bool = False,
) -> Mapping[bytes, Tuple[str]]:
    """Fetches rows from a Smalltable.

    Retrieves rows pertaining to the given keys from the Table instance
    represented by table_handle.  String keys will be UTF-8 encoded.

    @param table_handle: An open smalltable.Table instance.
    @type  table_handle:
    
    @return: generator of BagMessage(topic, message, timestamp) namedtuples for each message in the bag file
    @rtype:  generator of tuples of (str, U{genpy.Message}, U{genpy.Time}) [not raw] or (str, (str, str, str, tuple, class), U{genpy.Time}) [raw] 

    Raises:
        IOError: An error occurred accessing the smalltable.
    """
```



### 3）类

#### 说明

类应该在其定义下有一个用于描述该类的文档字符串. 如果你的类有公共属性(Attributes), 那么文档中应该有一个属性(Attributes)段. 并且应该遵守和函数参数相同的格式.

#### 示例

```python
class SampleClass(object):
    """Summary of class here.

    Longer class information....
    Longer class information....

    Attributes:
        likes_spam: A boolean indicating if we like SPAM or not.
        eggs: An integer count of the eggs we have laid.
    """

    def __init__(self, likes_spam=False):
        """Inits SampleClass with blah."""
        self.likes_spam = likes_spam
        self.eggs = 0

    def public_method(self):
        """Performs operation blah."""
```



### 4）块注释和行注释

#### 说明

最需要写注释的是代码中那些技巧性的部分. 如果需要解释的代码, 那么你应该现在就给它写注释.

1.对于复杂的操作, 应该在其操作开始前写上若干行注释. 

2.对于不是一目了然的代码, 应在其行尾添加注释.

3.为了提高可读性, 注释应该至少离开代码2个空格

#### 示例

```python
# 块注释

if i & (i-1) == 0:        # 行注释
```



### 5）类型注释

#### 说明

​	1.若对类型没有任何显示，请使用 `Any`

​	2.无需注释模块中的所有函数:

​		①.公共的API需要注释

​		②.难以理解的代码请进行注释

​		③.无法通过变量名知道数据类型的请进行注释

#### 示例

```python
# 无法通过变量名知道数据类型的请进行注释
timestamp_str: str = "0"

# 无法通过变量名知道数据类型的请进行注释
topic_rate: float = 0.0

# 难以理解的代码请进行注释
rate_static_dict: Dict[str, List[float, float, float]] = {} # 表格形式的topic帧率信息字典 {topic_name:[max, min, round]}

# 公共的API需要注释
def get_rate_static_dict() -> Dict[str, List[float, float, float]]:
    return rate_static_dict
```



### 6）TODO注释

#### 说明

为临时代码使用TODO注释, 它是一种短期解决方案. 不算完美, 但够好了.

#### 示例

```python
# @TODO: 这里是个临时方案, 未来需要优化.
```



## 7.枚举类

类型, 状态等有限的常量集合, 请使用枚举, 枚举值使用整数.

### 格式

​	ENUM+下划线+大写

### 示例

```python
class ENUM_BAG_TYPE(Enum):
    ROSBAG_VIDEO = 1
    ROSBAG_RAW = 2
    ROSBAG = 3 
    MFBAG = 4
    WSBAG = 5
```



## 8.其他可读性建议

1）代码注释请用中文, 大部分人英文不太好.

2）单个函数代码行数不超过30行.

3）函数形参不超过5个, 返回值不要超过3个.

4）if, for, while, with, try代码块之后通常会空1行.

5）函数底部的return通常另起1行.

6）即用即拿, 就近原则.

7）变量命名尽量能够准确描述变量的含义, 做到见文知意.

8）非通用类代码, 少用data, status, result, key, value等之类的名词.