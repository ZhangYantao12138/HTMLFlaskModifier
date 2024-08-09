import re

# 定义一个函数，用于将匹配的src和href属性转换为Flask的url_for格式


def replace_attribute_src_href(match):
    # 获取匹配的属性名 (src 或 href)
    attribute = match.group(1)
    # 获取匹配的文件名
    filename = match.group(2)
    # 为了保留双花括号的格式，这里使用了两个转义花括号
    return f'{attribute}="{{{{ url_for(\'static\', filename=\'{filename}\') }}}}"'

# 定义一个函数，用于修改HTML文件的内容


def modify_html_file(input_file, output_file):
    # 读取输入文件的内容
    with open(input_file, 'r', encoding='utf-8') as file:
        html_content = file.read()
        # 定义匹配src和href属性的正则表达式模式
        pattern = re.compile(r'(src|href)="([^"]+?)"')
        # 使用定义的replace_attribute_src_href函数替换匹配的内容
        modified_content = pattern.sub(replace_attribute_src_href, html_content)
        # 将修改后的内容写入输出文件
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(modified_content)

# 主程序部分
if __name__ == "__main__":
    input_file = 'F:/github/2024-8-5-web/Flask/templates/__results.html'
    output_file = 'F:/github/2024-8-5-web/Flask/templates/__results.html'

    # 调用modify_html_file函数进行文件内容修改
    modify_html_file(input_file, output_file)
    print(f'HTML file has been modified and saved to {output_file}')  # 打印操作成功信息
