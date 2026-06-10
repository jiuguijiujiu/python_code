"""
正则校验_校验html标签

参考html代码：
    <html>              # 开始：开放标签  # 结束：闭合标签
      <head></head>
      <body></body>
      <br />            # 自闭合标签
    </html>
"""

import re
# 需求1：校验html一级标签
# 1. 自定义html一级标签
# html_s = "<html>abc123</html>"

# 2. 正则匹配校验
# 方法1
# result = re.match(r'<[a-zA-Z]{1,4}>.*</[a-zA-Z]{1,4}>', html_s)       # 字母数1~4

# # 方法2:引入分组概念
# result = re.match(r'<([a-zA-Z]{1,4})>.*</\1>', html_s)       # 字母数1~4
#
#
# # 3.1 打印输出
# if result:
#     print(result.group())
# else:
#     print("匹配失败")


# 需求2：校验html一级标签
# 1. 自定义html一级标签
html_s = "<html><h1>abc123</h1></html>"

# 2. 正则匹配校验
# 方法1
# result = re.match(r'<[a-zA-Z]{1,4}><h[1-6]>.*</h[1-6]></[a-zA-Z]{1,4}>', html_s)       # 字母数1~4  标题标签1~6

# 方法2:引入分组概念
# result = re.match(r'<([a-zA-Z]{1,4})><(h[1-6])>.*</\2></\1>', html_s)       # 字母数1~4  标题标签1~6

# 方法3:给分组起名
result = re.match(r'<(?P<A>[a-zA-Z]{1,4})><(?P<B>h[1-6])>.*</(?P=B)></(?P=A)>', html_s)       # 字母数1~4  标题标签1~6

# 3.1 打印输出
if result:
    print(result.group())
else:
    print("匹配失败")