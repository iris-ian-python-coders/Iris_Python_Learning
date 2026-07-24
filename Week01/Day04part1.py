#Thu Jul 23, 2026

#Drone Conversions
#Before
def meters_to_cm(meters):
   cm = meters * 100
   return cm

def feet_to_cm(feet):
   cm_12 =  feet * 30.48
   return cm_12

def mph_to_cms(mph):
   cms = mph * 44.704
   return cms

meters = float(input("How many meters did you go? "))
feet = float(input("How many feet did you go? "))
mph = float(input("How fast (mph) did you go? "))

print(f"You went {meters_to_cm(meters)} centimeters.")
print(f"You went {feet_to_cm(feet)} centimeters.")

#After
def meters_to_cm(meters):
   return meters * 100

def feet_to_cm(feet):
   return feet * 30.48

def mph_to_cms(mph):
   return mph * 44.704

meters = input("How many meters did you go? ")
if meters != "":
   print(f"You went {meters_to_cm(float(meters))} centimeters.")

feet = input("How many feet did you go? ")
if feet != "":
   print(f"You went {feet_to_cm(float(feet))} centimeters.")

mph = input("How fast (mph) did you go? ")
if mph != "":
   print(f"You went {mph_to_cms(float(mph))} centimeters per second.")
