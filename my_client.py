import socket
import struct
import cv2

client_socket = socket.socket()
client_socket.connect(('127.0.0.1', 8002))

connection = client_socket.makefile('wb')
try:
    #打开摄像头
    cap = cv2.VideoCapture(0)
    while (1):
        #读取图片
        ret, frame = cap.read()
        # cv2.imshow("capture", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        #转换为jpg格式
        img_str = cv2.imencode('.jpg', frame)[1].tostring()
        #获得图片长度
        s = struct.pack('<L', len(img_str))
        # print(s)
        #将图片长度传输到服务端
        connection.write(s)
        connection.flush()
        # 传输图片流
        connection.write(img_str)
        connection.flush()

except Exception as e:
    print(e)
finally:
    connection.close()
    client_socket.close()