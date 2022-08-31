## Everyday60s
使用方式：`./Everyday60s.py`

通过爬虫获取知乎专栏[每天60秒读懂世界](https://www.zhihu.com/people/mt36501/posts)的数据，并通过Pillow库进行制图

图片存储于`./Img/`文件夹内

pip列表：
`pip install requests_html`
`pip install pillow`

### 更新信息：
#### Version 1.2.6
`->1.优化排版`

`--->1.1.换行由固定24字符换行修改为触底换行(string_lenth=[24,48])`

`->2.预留内存对象接口`
