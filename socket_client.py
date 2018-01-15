# coding:utf8
"""
--------------------------------------------------------------------------
    File:   socket_client.py
    Auth:   zsdostar
    Date:   2018/1/15 12:09
    Sys:    Windows 10
--------------------------------------------------------------------------
    Desc:   
--------------------------------------------------------------------------
"""

import socket

client = socket.socket()  # 协议类型

client.connect(('localhost', 6969))

client.send(b'hello server!')

data = client.recv(1024)
print('recv data:', data)
client.close()