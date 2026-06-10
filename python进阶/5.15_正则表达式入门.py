"""
初学正则表达式
步骤：
1. 导包
2. 判断
3. 返回结果
"""

# 导包
import re

# 判断
result = re.match('.bc', '.bc')     # 匹配成功
result = re.match('.bc', 'abc')     # 匹配成功
result = re.match('.bc', '\nbc')    # 匹配失败

result = re.match('\.bc', '.bc')     # 匹配成功
result = re.match('\.bc', 'abc')     # 匹配失败

result = re.match('[ade]bc', 'abc')     # 匹配成功
result = re.match('[ade]bc', 'ebc')     # 匹配成功
result = re.match('[ade]bc', 'fbc')     # 匹配失败

result = re.match('[^ade]bc', 'abc')     # 匹配失败
result = re.match('[^ade]bc', 'fbc')     # 匹配成功

result = re.match('[6-9]bc', '7bc')     # 匹配成功
result = re.match('[6-9]bc', '-bc')     # 匹配失败
result = re.match('[6-9]bc', '5bc')     # 匹配失败




# 返回结果
if result:
    print(result.group())
else:
    print("匹配失败")
