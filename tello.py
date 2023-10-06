from djitellopy import Tello
import time

tello = Tello()
tello.connect()
tello.takeoff()
# tello.turn_motor_on()
# x = 50
# tello.move_up(x)
# time.sleep(10)
height = tello.get_height()
print("Height: ", height)
x, y, z = 50, 50, 50
speed = 15
tello.go_xyz_speed(x, y, z, speed)
x, y, z = -50, -50, -50
speed = 15
tello.go_xyz_speed(x, y, z, speed)
# time.sleep(10)
tello.land()
flight_time = tello.get_flight_time()
power = tello.get_battery()
print("Power= ", power)
print("Flight Time: ", flight_time)
