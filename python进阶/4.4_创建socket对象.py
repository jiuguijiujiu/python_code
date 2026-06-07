"""
第一次用socket
"""

import socket

# 创建socket对象
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(tcp_socket)