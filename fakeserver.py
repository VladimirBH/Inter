# test-server.py
import socket
import sys
import time
import math
import random

j = 1
px = 300
py = 300


# создаемTCP/IP сокет
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Привязываем сокет к порту
server_address = ('localhost', 10002)
print('Старт сервера на {} порт {}'.format(*server_address))
sock.bind(server_address)

# Слушаем входящие подключения
sock.listen(1)
points = ""
while True:
    print('Ожидание соединения...')
    connection, client_address = sock.accept()
    try:
        print('Подключено к:', client_address)
        while True:
            while True: 
                try:
                    #print(1)
                    points = ""
                    #print(4)
                    for i in range(0,360):
                        if ( (i > 0 and i < 50) or (i>310 and i < 360)):
                            points += str(i) + ";" +str(i*2+1000+random.randint(100,1000)) + ","

                    #print(3)
                except:
                    #vprint(2)
                    lidar.clear_input()
                #print(6)
                if ( points != ""):
                    break
            data = connection.recv(8192)
            #print(f'Получено: {data.decode()}')
            if data:
                #print('Обработка данных...')
                #data = data.upper()
            #print(points,1)
                connection.sendall(points.encode())
            else:
                print('Нет данных от:', client_address)
                break

    finally:
        # Очищаем соединение
        connection.close()