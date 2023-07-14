import socket
from PIL import Image
import io

# адркс хоста будет разным в зависимости от настроек в сети
HOST = '192.168.1.100'
PORT = 9000

#Создание сокета и присвоение ему определенных адреса и порта
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen() # ожидание соединения
    print(f"Server listening on {HOST}:{PORT}")
    while True:
        conn, addr = s.accept()
        print('Connected by', addr)
        
        #Читаем длину сообщения
        data = conn.recv(16).strip().decode()
        size = int(data)
        print(f"Image size: {size} bytes")
        
        #Читаем байты сообщения
        data = conn.recv(size)
        #Преобразуем байты обратно в изображение
        img = Image.open(io.BytesIO(data))
        img.show()