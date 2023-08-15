# SvnTraverse

## 说明
这是一个SVN在线的目录遍历工具，可以将SVN的目录给遍历出来，结果会保存为一个“SVN目录+日期.xls”的文件。

## 事前准备
首先需要按照相应的python模块，所需要的模块在requirements.txt这个文件里面

pip3 install -r requirements.txt

需要安装Edge浏览器

本脚本使用的是Edge浏览器，请自行下载对应的webdrive版本：

参考链接：https://blog.csdn.net/tk1023/article/details/109078613

https://developer.microsoft.com/zh-cn/microsoft-edge/tools/webdriver/

https://msedgewebdriverstorage.z22.web.core.windows.net/

下载之后需将"msedgedriver.exe"修改为"MicrosoftWebDriver.exe"，并将该文件放入python3的安装文件夹目录下

## 运行脚本
python3 SvnTraverse.py

即可完成目录文件的生成
