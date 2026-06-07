"""
案例：文件上传案例，客户端代码

回顾：网络客户端实现流程
    1. 创建客户端socket对象
    2.  连接服务器端ip与端口号
    3. 读取文件数据，发送数据给服务器
    4. 释放资源
"""
# 导包
import socket

# 1. 创建客户端socket对象
clint_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. 连接服务器端ip与端口号
clint_socket.connect(('127.0.0.1', 6666))

# 3. 读取文件数据，发送数据给服务器
with open('1.txt', 'rb') as f:
    while True:
        data = f.read(8192)
        clint_socket.send(data)
        if len(data) == 0:
            break

# 4. 释放资源
clint_socket.close()