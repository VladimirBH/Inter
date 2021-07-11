import asyncio
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

pointsrez = "sdg"

async def handle_tcp_echo(reader, writer):  
    global i
    print('Connection from {}'.format(
        writer.get_extra_info('peername')
    ))
    while True:
        data = await reader.read(100)
        if data:
            message = data.decode()
            print("Echoing back: {!r}".format(message))
            writer.write(str(pointsrez).encode())
            
        else:
            print("Terminating connection")
            writer.close()
            break
async def rez():
    global pointsrez
    while True:
        await asyncio.sleep(1)
        while True:
            points = ""
            try:
                for i,scan in enumerate(lidar.iter_scans(min_len=150)):
                    for inf in scan:
                        angel_lidar = int(inf[1])
                        if( angel_lidar > 0 and angel_lidar < 90 or angel_lidar > 270  ):
                            points += str(inf[1]) + ";" +str(inf[2]) + ","
                    break
            except:
                lidar.clear_input()
            if ( points != ""):
                pointsrez = points
                break
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        asyncio.ensure_future(
            asyncio.start_server(handle_tcp_echo, '127.0.0.1', 10000),
            loop=loop
        )
    )
    asyncio.ensure_future(rez())
    print("sdg")
    loop.run_forever()
