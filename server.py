# test-server.py
import socket
import sys
from rplidar import RPLidar
import time
import math

lidar = RPLidar('/dev/ttyUSB0')

lidar.clear_input()
try:
    info = lidar.get_info()
except:
    lidar.clear_input()
    time.sleep(0.1)
    info = lidar.get_info()

print(info)

health = lidar.get_health()
print(health)
lidar.set_pwm(1000)
j = 1
px = 300
py = 300


# создаемTCP/IP сокет
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Привязываем сокет к порту
server_address = ('localhost', 10000)
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
                    for i,scan in enumerate(lidar.iter_scans(min_len=150)):
                        for inf in scan:
                            
                          
                            #print(inf)
                            #print('\n')
                            angel_lidar = int(inf[1])
                            if( angel_lidar > 0 and angel_lidar < 90 or angel_lidar > 270  ):
                                points += str(inf[1]) + ";" +str(inf[2]) + ","
                        break
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