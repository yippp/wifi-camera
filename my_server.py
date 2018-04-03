import socket
import struct
from PIL import Image
import numpy
import io

server_socket = socket.socket()
# 绑定socket通信端口
server_socket.bind(('0.0.0.0', 8002))
server_socket.listen(0)

connection = server_socket.accept()[0].makefile('rb')



while True:
    #获得图片长度
    image_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]
    # print(image_len)
    if not image_len:
        break

    image_stream = io.BytesIO()
    #读取图片
    image_stream.write(connection.read(image_len))

    image_stream.seek(0)
    image = Image.open(image_stream)
    cv2img = numpy.array(image, dtype=numpy.uint8)
    # print(cv2img[0][0])
