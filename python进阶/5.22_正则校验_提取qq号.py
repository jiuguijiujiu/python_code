"""
正则校验_提取qq号
"""

# 导包
import re

# 需求：数据格式为qq:数字，从文本种提取qq文本与qq号
# qq数据
s = 'qq:123456'

# 正则校验
result = re.match(r'^(qq):(\d{6,11})$', s)

# 打印结果
if result:
    print(result.group())
    print(result.group(0))

    # 只要qq两字
    print(result.group(1))
    # 只要qq号码
    print(result.group(2))
else:
    print("未匹配")