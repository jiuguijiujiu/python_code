"""
正则校验_提取邮箱域名
"""

# 导包
import re

# 1. 定义邮箱
email = '12346abc@163.com'

# 匹配邮箱是否合法
result = re.match(r'^[0-9a-zA-Z_]{4,20}@(163|qq|126)\.com$', email)

# 打印输出
if result:
    print(f"合法邮箱为：{result.group(0)}")       # 获取第0组的信息，效果如下，输出整个结果
    print(f"合法邮箱为：{result.group()}")
    print(f"合法邮箱为：{result.group(1)}")       # 获取第1组的信息，只输出索引为1的内容


else:
    print("邮箱不合法")