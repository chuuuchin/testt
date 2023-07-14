import cv2
import numpy as np
import socket

# путь камеры может различаться, в зависимости от устройства, "с камеры" это неоднозначно, т.к. на одном устройстве может быь несколько камер.
cap = cv2.VideoCapture(0)

# задаем соединение TCP/IP и адрес хоста и порта получателя
HOST = '192.168.1.24' # адрес хоста получателя
PORT = 9000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while(True):
    # Захватываем кадр за кадром
    ret, frame = cap.read()

    #Конвертируем изображение в строку байтов
    imgString = cv2.imencode('.jpg', frame)[1].tostring()

    #Отправляем изображение на другой компьютер
    s.sendall((str(len(imgString)).ljust(16)).encode('utf-8'))
    s.sendall(imgString)

# Закрываем все окна и удаляем конончательно соединение
cap.release()
cv2.destroyAllWindows()
s.close()