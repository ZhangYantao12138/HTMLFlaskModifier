import re
import os

# 定义一个函数，用于将匹配的src和href属性转换为Flask的url_for格式


def replace_attribute_src_href(match):
    # 获取匹配的属性名 (src 或 href)
    attribute = match.group(1)
    # 获取匹配的文件名
    filename = match.group(2)
    # 为了保留双花括号的格式，这里使用了两个转义花括号
    return f'{attribute}="{{{{ url_for(\'static\', filename=\'{filename}\') }}}}"'

# 定义一个函数，用于修改HTML文件的内容


def modify_html_file(file_path):
    # 读取输入文件的内容
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
        # 定义匹配src和href属性的正则表达式模式
        pattern = re.compile(r'(src|href)="([^"]+?)"')
        # 使用定义的replace_attribute_src_href函数替换匹配的内容
        modified_content = pattern.sub(replace_attribute_src_href, html_content)
        # 将修改后的内容写入输出文件
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(modified_content)


def replace_html_content(file_path):
    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()


# 替换特定的<script>标签内容
    style_pattern = r'<style type="text/css">[\s\S]*?<script src'
    new_script = """  
    <script>  
        document.oncontextmenu = function (event) {  
            event = event || window.event;  
            var targetElement = event.target || event.srcElement;  
            if (!targetElement) return true;  

            if (targetElement.tagName) {  
                if (targetElement.tagName.toLowerCase() === "input" && targetElement.type.toLowerCase() === "text" ||  
                    targetElement.tagName.toLowerCase() === "textarea") {  
                    return true;  
                }  
            }  
            return false;  
        }  
    </script>
    <script src  
    """
    content = re.sub(style_pattern, new_script, content, flags=re.IGNORECASE | re.DOTALL)

    # 写入修改后的内容回文件
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


def fix_iframe(file_path):
    pattern_id = r'iframe id="([^"]+)"'
    pattern_iframe_attrs = r'scrolling="auto" frameborder="0" webkitallowfullscreen mozallowfullscreen'

    # 读取整个文件内容
    with open(file_path, 'r', encoding='utf-8') as f_input:
        content = f_input.read()

    # 使用正则表达式查找所有iframe标签
    iframes = re.finditer(pattern_id, content)

    # 创建一个新的字符串来保存修改后的内容
    new_content = content

    # 遍历所有找到的iframe标签
    for match in iframes:
        # 提取iframe的id
        iframe_id = match.group(1)

        # 查找当前iframe标签的起始和结束位置
        start = match.start()
        end = content.find('>', start) + 0  # '>'是标签的结束

        # 提取整个iframe标签
        iframe_tag = content[start:end]

        # 检查这个iframe标签是否包含我们想要修改的属性
        if re.search(pattern_iframe_attrs, iframe_tag):
            # 构建新的src属性
            new_src = f'iframe id="{iframe_id}" data-label="内部框架" src="http://127.0.0.1:5000/{iframe_id}"'

            iframe_tag_replaced = re.sub(iframe_tag, new_src, iframe_tag, count=1)

            # 将修改后的iframe标签放回原位置
            new_content = new_content[:start] + iframe_tag_replaced + new_content[end:]

            # 写入修改后的内容到文件
    with open(file_path, 'w', encoding='utf-8') as f_output:
        f_output.write(new_content)

# 主程序部分
folder_path = "F:/python/auto/templates"
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        modify_html_file(file_path)
        fix_iframe(file_path)
        replace_html_content(file_path)
        print(file_path, "done")

