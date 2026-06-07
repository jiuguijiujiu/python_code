"""
流程：
1.创建套接字客户端对象
2.连接服务器端，指定服务器端ip与端口号
3.接收服务器数据
4.发送数据
5.关闭套接字

细节：
客户端与服务端通过字节流（bytes）形式通信
"""
# 导包
import socket

# 1.创建套接字客户端对象
clint_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2.连接服务器端，指定服务器端ip与端口号
clint_socket.connect(('127.0.0.1', 10086))  # 元组的形式传

# 3.接收服务器数据
data = clint_socket.recv(1024).decode('utf-8')
print(f"来自服务器信息：{data}")

# 4.发送数据
clint_socket.send("你好".encode('utf-8'))

# 5.关闭套接字
clint_socket.close()

