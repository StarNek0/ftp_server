# coding:utf8
"""
--------------------------------------------------------------------------
    File:   socket_server.py
    Auth:   zsdostar
    Date:   2018/1/15 12:18
    Sys:    Windows 10
--------------------------------------------------------------------------
    Desc:   
--------------------------------------------------------------------------
"""

import socket

server = socket.socket()

server.bind(('localhost', 6969))  # 绑定监听端口

server.listen()  # 监听

conn,addr = server.accept()  # 等client连进来, conn就是连进来的这个server的实例

data = conn.recv(1024)  # 一定是conn.而不是server.
print('recv data:', data)
conn.send(data.upper())

import time
time.sleep(300)
server.close()