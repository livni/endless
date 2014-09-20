import time
from pymodbus.client.sync import ModbusTcpClient as ModbusClient

client_ip = '192.168.1.212'

client = ModbusClient(client_ip)

onoff_coil = 1
barrel_rotation_coil = 0
speed_register = 0 # 1-10
position_register = 1 # {1,2,3}

def init():
    client.write_coil(onoff_coil, 0)
    client.write_coil(barrel_rotation_coil, 0)
    client.write_register(speed_register, 1)
    client.write_register(position_register, 2)

def set_speed(speed):
    speed = int(speed)
    if speed < 1:
        print("speed must be >= 1, adjusting to 1")
        speed = 1
    if speed > 10:
        print("speed must be <= 10, adjusting to 10")
        speed = 10
    client.write_register(speed_register, speed)

def set_position(position):
    position = int(position)
    if position not in [1, 2, 3]:
        print("position must be 1, 2 or 3. ignoring set position")
        return
    client.write_register(position_register, position)

def turn_motors_on():
    client.write_coil(onoff_coil, 1)

def turn_motors_off():
    client.write_coil(onoff_coil, 0)

def barrel_rotation_on():
    client.write_coil(barrel_rotation_coil, 1)

def barrel_rotation_off():
    client.write_coil(barrel_rotation_coil, 0)

def test():
    set_speed(3)
    set_position(1)
    turn_motors_on()
    barrel_rotation_on()
    time.sleep(1)
    barrel_rotation_off()
    set_position(3)
    time.sleep(0.1)
    turn_motors_off()

if __name__ == '__main__':
    test()
