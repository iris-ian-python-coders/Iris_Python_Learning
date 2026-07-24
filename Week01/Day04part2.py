#Thu Jul 23, 2026

#Drone Waypoint function
#Before:
from easytello import tello

drone = tello.Tello()

def fly_to_waypoint(waypoint):
   if waypoint == "A":
       drone.takeoff()
       drone.ccw(45)
       drone.forward(50)
       drone.back(50)
       drone.cw(45)
       drone.land()

   elif waypoint == "B":
       drone.takeoff()
       drone.ccw(45)
       drone.forward(50)
       drone.back(50)
       drone.cw(45)
       drone.forward(50)
       drone.back(50)
       drone.land()

   elif waypoint == "C":
       drone.takeoff()
       drone.ccw(45)
       drone.forward(50)
       drone.back(50)
       drone.cw(45)
       drone.forward(50)
       drone.back(50)
       drone.cw(45)
       drone.forward(50)
       drone.back(50)
       drone.ccw(45)
       drone.land()
   return

waypoint = input("Which waypoint would you like to go? ")
fly_to_waypoint()

#After:
drone = tello.Tello()
drone.set_speed(30)
drone.wait(1)

def waypoint_a():
   drone.ccw(45)
   drone.forward(50)
   drone.back(50)
   drone.cw(45)

def waypoint_b():
   drone.forward(50)
   drone.back(50)

def waypoint_c():
   drone.cw(45)
   drone.forward(50)
   drone.back(50)
   drone.ccw(45)

def fly_to_waypoint(waypoint):
   drone.takeoff()

   if waypoint == "A":
       waypoint_a()

   elif waypoint == "B":
       waypoint_a()
       waypoint_b()

   elif waypoint == "C":
       waypoint_a()
       waypoint_b()
       waypoint_c()

   else:
       print("Invalid waypoint")
       drone.land()
       return

   drone.land()

waypoint = input("Which waypoint would you like to go? ").upper()
fly_to_waypoint(waypoint)

#Drone curves
from easytello import Tello, tello

drone = tello.Tello()

def dronefunction():
   print(drone.get_battery())
   drone.takeoff()
   drone.curve(50, 50, 0, 100, 0, 5, 30)
