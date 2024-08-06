# HTML格式转换器（HTMl to Flask Template）

## 简介
在使用Flask框架开发应用时，会用到render_template()方法渲染html文件。该方法要求html中使用到的静态文件储存在statics文件夹中，并使用url_for方法指定路径。而在一般的静态页面中，路径是使用相对路径在href、src等属性中标记出的，但这种方法不被render兼容。    
为了解决以上问题，使静态页面的html文件可以便捷地用于Flask开发，我们编写了这个格式转换程序。

## 使用说明
为了使用该项目进行格式转化，请遵循以下步骤。
1. 本地化
首先，将该项目通过download zip或clone方法下载到本地。
2. 确认依赖库安装
本项目使用到的第三方库包括：
tkinter
可以使用以下指令在终端中配置：
```shell
pip install tkinter
```
3. 运行test.py
运行后，根据图形界面指示操作即可。

