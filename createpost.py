import sys
import os
import datetime

# 确保用户提供了一个命令行参数作为标题
if len(sys.argv) < 2:
    print("错误: 请提供一个标题。")
    print("用法: python createpost.py 我是标题")
    sys.exit(1)

# 从命令行参数获取标题
title = sys.argv[1]

# 定义_posts文件夹的路径
posts_folder = "./_posts"

# 如果_posts文件夹不存在，则创建它
if not os.path.exists(posts_folder):
    os.makedirs(posts_folder)

# 获取当前日期和时间
current_date = datetime.datetime.now()

# 创建文件名格式为 yyyy-mm-dd-title.markdown
filename = f"{current_date.strftime('%Y-%m-%d')}-{title}.markdown"

# 定义完整的文件路径
full_path = os.path.join(posts_folder, filename)

# 定义要写入文件的内容
content = f"""---
layout: post
title:  "{title}"
date:  {current_date.strftime('%Y-%m-%d %H:%M:%S')} -0500
categories: jekyll update
---
"""

# 写入内容到Markdown文件
with open(full_path, "w", encoding="utf-8") as file:
    file.write(content)

print(f"文件已成功创建于: {full_path}")
