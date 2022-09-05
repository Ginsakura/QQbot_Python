# QQ_bot_功能模块

通用模块,只要能调用/加载外部文件/脚本/应用程序的bot插件均可调用本系列脚本

`以类重写的版本是为了适配基于Go-CQHttp开发的Python框架`

C++重构版:[QQbot_CPP](https://github.com/Ginsakura/QQbot_cpp)

## [AzurLane Script](https://github.com/Ginsakura/QQbot_Python/tree/main/AzurLane)
### Version 0.0.1

使用方式：`./AzurLane.py <command> [argument]`

框架搭建中······

## [Cloud music](https://github.com/Ginsakura/QQbot_Python/tree/main/Cloud_Music)
### Version 2.0.1

使用方式：`./Cloudmusic.py <QQ号> <传入文本>`

接收文本，若有“ID”部分，后续取数字作为网易云歌曲ID进行返回。

处理后，存储操作数据至`./Cloudmusic_Data/Cloudmusic_Data.db`中。

## [Costom Welcome](https://github.com/Ginsakura/QQbot_Python/tree/main/Costom_Welcome)
### Version 0.0.1

使用方式：未定义

仅群聊权限者有权操作。

指定bot在有人入群时的自定义欢迎词。

处理后，存储操作数据至`./Costom_Welcome_Data/Costom_Welcome_Data.db`中。

## [Dice](https://github.com/Ginsakura/QQbot_Python/tree/main/Dice)
### Version 0.1.0

骰娘，并没有写完

## [Everyday60s](https://github.com/Ginsakura/QQbot_Python/tree/main/Everyday60s)
### Version 1.3.1

使用方式：`./Everyday60s.py`

通过爬虫获取知乎专栏[每天60秒读懂世界](https://www.zhihu.com/people/mt36501/posts)的数据，并通过Pillow库进行制图

图片存储于`./Img/`文件夹内

pip列表：

    `pip install requests_html`

    `pip install pillow`

## [Favorability](https://github.com/Ginsakura/QQbot_Python/tree/main/Favorability)
### Version 1.0.3

使用方式：`./Favorability.py <操作> <QQ号>`

不成熟的好感度插件。

数据存储方式为SQLite数据库，位于`./Favorability_Data/Favorability_Database.db`

## [Fortune](https://github.com/Ginsakura/QQbot_Python/tree/main/Fortune)
### Version 5.0.0

使用方式：`./Fortune.py <QQ号>`

抽取运势，每天每用户第一次调用时进行计算，并将结果存入数据库，

之后（同用户）再次调用时，不再进行计算，改为直接从数据库调取当天第一次抽取结果。

数据库为SQLite数据库，位于`./Fortune_Data/Fortune_Data.db`

初次运行时会通过爬虫获取节气信息，当到某个节气时，第一次抽取会返回节气提示.

pip列表：
`pip install requests_html`

## [System Status](https://github.com/Ginsakura/QQbot_Python/tree/main/System_Status)
### Version 1.0.0

使用方式：`./System_Status.py <QQ号>`

传入操作人，并且对比是否为允许操作用户，

若是，则返回当前系统的部分参数。

pip列表：
`pip install psutil`

## [Tarot](https://github.com/Ginsakura/QQbot_Python/tree/main/Tarot)
### Version 1.0.2

使用方式：`./Tarot.py <QQ号>`

传入操作人，自动计算抽取塔罗牌，每次抽取三张。

数据存储至SQLite数据库：`./Tarot_Data/Tarot_Data.db`

下次更新修改数据存储格式。
