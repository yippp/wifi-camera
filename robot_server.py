
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 21:39:31 2018

@author: CUHKSZRAIL
"""

# 导入socket库:
import socket
import time 
import threading

# 创建一个基于IPv4和TCP协议的Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 监听端口:
s.bind(('127.0.0.1', 5555))

# 开始监听端口，传入的参数指定等待连接的最大数量
s.listen(5)
print('Waiting for connection...')

# 每个连接都必须创建新线程（或进程）来处理
def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        # if not data or data.decode('utf-8') == 'exit':
        #     break
        # sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)
    


# 服务器程序通过一个永久循环来接受来自客户端的连接
while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
    


