## Fortune

使用方式: `./Fortune.py <QQ号>`

抽取运势，每天每用户第一次调用时进行计算，并将结果存入数据库，

之后（同用户）再次调用时，不再进行计算，改为直接从数据库调取当天第一次抽取结果。

数据库为SQLite数据库，位于`./Fortune_Data/Fortune_Data.db`

初次运行时会通过爬虫获取节气信息，当到某个节气时，第一次抽取会返回节气提示.

pip列表：
`pip install requests_html`

### 更新信息:
#### Transform.py

`该脚本用于将旧版本数据库(5.0.0以前)转换为新版数据库`

使用方法:

1.将旧版数据库导出为csv格式文件(见example.csv)

2.将csv文件放置于`./Data/csv/*.csv`位置,脚本置于`./Data/`目录中

3.csv文件为数据库使用Navicat导出,其他软件尚未测试,不过只要输出的格式与`example.csv`相同即可

4.执行脚本,然后脚本会逐一读取`./Data/csv/`目录中的csv文件并写入新版数据库,缺失的数据会被`自动填充空值`

#### Version 5.0.4

`1.文本格式化修复`

#### Version 5.0.3

`1.修复main抽到1或100时,输出结果部分丢失的bug`

`2.新增若干bug`

#### Version 5.0.1 & 5.0.2

`1.修改数据库格式及数据存储`

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
