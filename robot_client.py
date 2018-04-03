# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 21:49:58 2018

@author: CUHKSZRAIL
"""

# 导入socket库:
import socket
import cv2
import numpy

# open cam
cap = cv2.VideoCapture(0)

# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接:
s.connect(('127.0.0.1', 5555))
    
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))
    
# for data in [b'Michael']:
#     # 发送数据:
#     s.send(data)
#     print(s.recv(1024).decode('utf-8'))

# Take each frame
ret, img = cap.read()

while ret:
    # show the image
    # cv2.imshow('image', img)
    result, imgencode = cv2.imencode('.jpg', img)
    data = numpy.array(imgencode)
    stringData = data.tobytes()

    # s.send(bytes(len(stringData)).ljust(16))
    s.send(stringData)

    # if (cv2.waitKey(30) & 0xFF) == 'q' or 'Q' or 'Esc':
    #     exit()

# close the socket
s.send(b'exit')
s.close()
# close the camera and destroy the window
cap.release()
cv2.destroyAllWindows()