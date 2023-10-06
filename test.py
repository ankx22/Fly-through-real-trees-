from djitellopy import Tello
import time
import csv

# Filepath to your CSV
csv_filepath = 'trajnew.csv'

# Lists to hold the coordinates
x_coords = []
y_coords = []
z_coords = []

# Open and read the CSV
with open(csv_filepath, mode='r', newline='') as file:
    reader = csv.reader(file)
    
    # Read x coordinates
    x_coords = [float(i) for i in next(reader)]
    
    # Read y coordinates
    y_coords = [float(i) for i in next(reader)]
    
    # Read z coordinates
    z_coords = [float(i) for i in next(reader)]

    # Skip the next six rows which you don't want
    for _ in range(6):
        next(reader)

# Print out the lists (for testing)

x_coords = [int(x) for x in x_coords]
y_coords = [int(y) for y in y_coords]
z_coords = [int(z) for z in z_coords]

# print("X Coordinates:", x_coords)
# print("Y Coordinates:", y_coords)
# print("Z Coordinates:", z_coords)

tello = Tello()
tello.connect()
tello.takeoff()
speeds = 10
for i in range(len(x_coords)):
    tello.go_xyz_speed(x_coords[i],y_coords[i],z_coords[i],speeds)
tello.land()
flight_time = tello.get_flight_time()
power = tello.get_battery()
print("Power= ", power)
print("Flight Time: ", flight_time)
