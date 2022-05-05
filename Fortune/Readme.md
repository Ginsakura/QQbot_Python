## Fortune

使用方式：`./Fortune.py [QQ号]`

抽取运势，每天每用户第一次调用时进行计算，并将结果存入数据库，

之后（同用户）再次调用时，不再进行计算，改为直接从数据库调取当天第一次抽取结果。

数据库为SQLite数据库，位于`./Fortune_Data/Fortune_Data.db`

初次运行时会通过爬虫获取节气信息，当到某个节气时，第一次抽取会返回节气提示.

pip列表：
`pip install requests_html`

### 更新信息:
#### Version 5.0.0

`->1.将函数修改为类方式实现`

#### Version 4.0.2

`->1.轻度修改部分运势评价词`

#### Version 4.0.1

`->1.新增节气提示词`

`->2.通过requests_html库进行爬取节气数据,并存入数据库`

#### Version 4.0.0

`->1.提前写入节气提示词部分代码`

#### Version 3.0.3

`->1.Fix(Add) bugs`

#### Version 3.0.2

`->1.Fix(Add) bugs`

#### Version 3.0.1

`->1.Fix(Add) bugs`

#### Version 3.0.0

`->1.重写`

`->2.数据存储由ini配置文件改为SQLite数据库`

#### Version 2.2.0

`->1.更换数据存储方式``失败`
