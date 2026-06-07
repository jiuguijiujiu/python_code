"""
需求：
问1，2，3，4能组合成的四位数有几种情况，按照5个一行输出．
要求：
1.要求同时包含1，2，3，4这四个数字．
    1234，1324均可
    1122，1123不行
2.要求数字1和3不能挨着．
    1324，3124不行
    1234，3412可以
3．数字4不能开头．
4．5行以内搞定(包括5行)
"""

# 思路：先转为字符串，再用字符串的功能进行判断

count = 0
for i in [str(j) for j in range(1234, 4321)]:       # 列表推导式,[表达式 for 变量 in 可迭代对象]
    if '1' in i and '2' in i and '3' in i and '4' in i and not '13' in i and not '31' in i and i[0] != '4':
        count += 1
        print(i, end='\n' if count % 5 == 0 else '\t')      #三元表达式，值1 if 条件 else 值2

# [表达式 for 变量 in 可迭代对象 if 条件]列表推导式加入判断，当条件为True时，表达式的结果会被加入新列表；当条件为False时，跳过当前元素。一行解决。
# print([int(i) for i in [str(j) for j in range(1234, 4321)] if '1' in i and '2' in i and '3' in i and '4' in i and not '13' in i and not '31' in i and i[0] != '4'])