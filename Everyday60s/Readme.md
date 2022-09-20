## Everyday60s
使用方式：`./Everyday60s.py`

通过爬虫获取知乎专栏[每天60秒读懂世界](https://www.zhihu.com/people/mt36501/posts)的数据，并通过Pillow库进行制图

图片存储于`./Img/`文件夹内

pip列表：
`pip install requests_html`
`pip install pillow`

### 更新信息：

#### Version 1.4.1

`->1.修复缩进问题`

#### Version 1.4.0

`->1.修复专栏因不过审而发图片导致的程序崩溃`

#### Version 1.3.1

`->1.修复没有微语导致的程序崩溃`

#### Version 1.3.0

`->1.新增数据库存储专栏地址等数据的框架`

#### Version 1.2.6
`->1.优化排版`

`--->1.1.换行由固定24字符换行修改为触底换行(string_lenth=[24,48])`

`->2.预留内存对象接口`
