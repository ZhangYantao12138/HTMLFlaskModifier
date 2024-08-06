import re
import os
import tkinter as tk
from tkinter import filedialog, messagebox

# 定义一个函数，用于将匹配的src和href属性转换为Flask的url_for格式
def replace_attribute_src_href(match):
    # 获取匹配的属性名 (src 或 href)
    attribute = match.group(1)
    # 获取匹配的文件名
    filename = match.group(2)
    # 为了保留双花括号的格式，这里使用了两个转义花括号
    return f'{attribute}="{{{{ url_for(\'static\', filename=\'{filename}\') }}}}"'

# 定义一个函数，用于修改HTML文件的内容
def modify_html_file(input_file, output_folder):
    try:
        # 读取输入文件的内容
        with open(input_file, 'r', encoding='utf-8') as file:
            html_content = file.read()
            # 定义匹配src和href属性的正则表达式模式
            pattern = re.compile(r'(src|href)="([^"]+?)"')
            # 使用定义的replace_attribute_src_href函数替换匹配的内容
            modified_content = pattern.sub(replace_attribute_src_href, html_content)
        
        # 获取输入文件名并创建输出文件路径
        base_filename = os.path.basename(input_file)
        output_file = os.path.join(output_folder, f'modified_{base_filename}')
        
        # 将修改后的内容写入输出文件
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(modified_content)
        
        return output_file
    except FileNotFoundError:
        print(f'The file {input_file} was not found.')
        return None
    except IOError as e:
        print(f'An IOError occurred: {e}')
        return None

# 定义一个函数来处理文件选择和转换
def process_files():
    files = filedialog.askopenfilenames(title="Select HTML files", filetypes=[("HTML files", "*.html")])
    if not files:
        return
    
    # 获取文件所在目录并创建输出文件夹
    input_dir = os.path.dirname(files[0])
    output_folder = os.path.join(input_dir, 'modified_files')
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    modified_files = []
    for file in files:
        modified_file = modify_html_file(file, output_folder)
        if modified_file:
            modified_files.append(modified_file)
    
    if modified_files:
        messagebox.showinfo("运行成功", f"文件格式已更改，保存至{output_folder}")
    else:
        messagebox.showwarning("错误", "未成功修改，请检查原文件")

# 创建主窗口
root = tk.Tk()
root.title("HTML Modifier")
root.geometry("300x150")

# 创建按钮
btn_select_files = tk.Button(root, text="Select HTML Files", command=process_files)
btn_select_files.pack(pady=20)

# 运行主循环
root.mainloop()
