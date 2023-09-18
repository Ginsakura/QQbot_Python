## Everyday60s
使用方式：`./Everyday60s.py`

通过爬虫获取知乎专栏[每天60秒读懂世界](https://www.zhihu.com/people/mt36501/posts)的数据，并通过Pillow库进行制图

图片存储于`./Img/`文件夹内

### 字体来源: [霞鹜文楷](https://github.com/lxgw/LxgwWenKai)

pip列表：
`pip install requests_html`
`pip install pillow`

### 更新信息：
#### Version 2.0.2
1. 修复文本日期没有渲染的bug

#### Version 2.0.2
1. 修复格式问题导致第一条新闻缺失的bug

#### Version 2.0.1
1. 修复因没有头图而导致的报错的bug
2. 重写readme.md
3. 添加没有头图时的小图片

#### Version 2.0.0
1. 以类方式重写

#### Version 1.4.3
1. Fix Bug:每天每次都会从网络获取数据，改为每天仅第一次从网络获取数据
2. Add Some Bug

#### Version 1.4.2
1. Fix Bug
2. Add Some Bug

#### Version 1.4.1
1. 修复缩进问题

#### Version 1.4.0
1. 修复专栏因不过审而发图片导致的程序崩溃

#### Version 1.3.1
1. 修复没有微语导致的程序崩溃

#### Version 1.3.0
1. 新增数据库存储专栏地址等数据的框架

#### Version 1.2.6
1. 优化排版
    1. 换行由固定24字符换行修改为触底换行(string_lenth=[24,48])
2. 预留内存对象接口
