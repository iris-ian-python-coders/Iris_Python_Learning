#Wed Jul 22, 2026


#For loops
x = 0
for i in range(10):
   x += 1
   print(f"i = {i}")

#While loops
x = 0
while x < 10:
   x += 1
   print(x)

#More Complicated while loop
def exit():
   ex = 2
   while ex != 0 and ex != 1:
       ex = int(input("Enter 0 to leave and 1 to stay: "))
   return ex
counter = 0

stay = True

while stay:
   print(counter)
   counter += 1
   stay = exit()

print("You have exited the loop")



#Drone commands:

from easytello import tello

my_drone = tello.Tello()

#cw = clockwise, ccw = counterclockwise
my_drone.takeoff()
mydrone.forward(5)
mydrone.backward(5)
mydrone.up(5)
mydrone.down(5)
mydrone.left(2)
mydrone.right(2)
mydrone.cw(90)
mydrone.ccw(180)
mydrone.land()
