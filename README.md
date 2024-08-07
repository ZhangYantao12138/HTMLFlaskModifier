# 格式转换器（HTMl to Flask Template）

---

## 简介
在使用 Flask 框架开发 Web 应用时，一般会用到 render_template() 方法渲染 HTML 文件。该方法要求 HTML 中使用到的静态文件储存在 statics 文件夹中，并使用 url_for() 方法指定路径。而在一般的静态页面中，路径是使用相对路径在 href、src 等属性中标记出的，但这种方法不被 render_template() 兼容。    
这个项目正是着眼于上述问题，致力于使静态页面的 HTML 文件可以便捷地转化为适用于 Flask 开发的格式。

---

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
3. 运行test.py文件
运行后，根据图形界面指示操作即可。

---

## 改进方向
如果你想贡献这个开源项目，让它变得更好，不妨从以下方向入手：
1. 美化 tkinter 的图形界面。
2. 尝试兼容整个静态网站代码文件夹的修改，把它直接输出成可用的 Statics 文件夹和 Templates 文件夹。（甚至输出一个简单的app.py文件）
3. 把项目打包成可执行文件，让没有 python 环境的用户也可以直接使用图形界面。

---
# English ver.
# Format Converter (HTML to Flask Template)

---

## Introduction
When developing web applications using the Flask framework, the `render_template()` method is typically used to render HTML files. This method requires that the static files referenced in the HTML be stored in the `statics` folder and that the paths be specified using the `url_for()` method. However, in standard static pages, paths are often marked in the `href` and `src` attributes using relative paths, which are not compatible with `render_template()`. This project aims to address this issue by enabling the easy conversion of static HTML pages to a format suitable for Flask development.

---

## Usage Instructions
To use this project for format conversion, please follow these steps:

1. **Download the Project**  
   First, download the project to your local machine via the download zip or clone method.

2. **Install Dependencies**  
   This project uses the following third-party library: `tkinter`.  
   You can configure it in your terminal using the following command:
    ```shell
    pip install tkinter
    ```

3. **Run `test.py` File**  
   After running the file, follow the instructions provided in the graphical interface.

---

## Areas for Improvement
If you want to contribute to this open-source project and make it better, consider the following directions:

1. Improve the graphical interface of `tkinter`.
2. Attempt to modify the entire static website code folder and directly output it as a usable `statics` folder and `templates` folder (even output a simple `app.py` file).
3. Package the project into an executable file so that users without a Python environment can also use the graphical interface directly.