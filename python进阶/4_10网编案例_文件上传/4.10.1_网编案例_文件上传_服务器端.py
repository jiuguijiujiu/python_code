"""
案例：文件上传案例，服务器端代码

回顾：网络服务器端实现流程
    1. 创建服务器端socket对象
    2. 对象绑定 ip 与 端口号
    3. 设置最大监听数
    4. 等待客户端申请建立连接
    5. 接收读取客户端上传的文件数据,把读取到的数据写到本地文件中
    6. 释放资源
"""

# 导包
import socket

# 1.创建服务器端socket对象
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 2.对象绑定ip与端口号
server_socket.bind(('127.0.0.1',6666))

# 3.设置最大监听数
server_socket.listen(5)

# 4.等待客户端申请建立连接
accept_socket, clint_info = server_socket.accept()

# 5.接收读取客户端上传的文件数据(循环读取8192),把读取到的数据写到本地文件中
with open('my_data.txt', 'wb') as dest_f:
    while True:
        bys = accept_socket.recv(8192)  # 8192字节 = 8kb

        # 判断是否还有数据，无数据结束
        if len(bys) == 0:
            break

        # 写入数据
        dest_f.write(bys)

# 6.释放资源
accept_socket.close()