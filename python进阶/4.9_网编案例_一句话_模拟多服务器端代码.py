"""
流程：
1.创建套接字服务器对象
2.绑定端口号
3.设置监听
4.等待客户端连接请求
5.发送数据
6.接收数据
7.关闭套接字

细节：
客户端与服务端通过字节流（bytes）形式通信
"""
# 导包
import socket

# 1.创建套接字服务器对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2.绑定端口号
server_socket.bind(('127.0.0.1', 10086))    # 元组的形式传

# 3.设置监听
server_socket.listen(5)

while True:
    try:
        # 4.等待客户端连接请求
        accept_socket, clint_info = server_socket.accept()  # 接收的是元组

        # 5.发送数据
        accept_socket.send(b'hello!')   # 字符串转为二进制

        # 6.接受数据
        data = accept_socket.recv(1024).decode('utf-8')    # 收到的是字节流，需要进行编码
        print(f"服务器收到来自{clint_info}的信息：{data}")

        # 7.关闭套接字
        accept_socket.close()
        # server_socket.close() # 服务器端一般不关闭
    except:
        pass

# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)