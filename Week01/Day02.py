#Tue Jul 21, 2026

#get the name of the camp
CampName = input("What is the name of your camp? ")

#Get the number of days
NumDays = int(input("How many days is {}? ".format(CampName)))

#Find out what day of the camp it is
CurrentDay = int(input("What is the current day of the camp: "))

#Find out how many days left in camp
DaysLeft = NumDays - CurrentDay

#Output the number of days left in camp
print("There are {} days left in {}".format(DaysLeft, CampName))



#Converting miles per hour to meters per second
def convert(mph:float):
   meters_per_sec = float(mph * 0.44704)
   return meters_per_sec

miles = float(input("How many miles per hour are you going: "))

print(f"You are going ",convert(miles), "meters per second.")


#Age until: calculator

name = input("Enter your name: ")
age = int(input("Enter your age: "))
until = int(input("Enter the age you want to calculate to (how many years you have until x, enter x):"))

AgeUntil = until - age
if age < until:
   print("You have {} years left until you are {}.".format(AgeUntil, until))
else:
   print("You are very old, {}".format(name))

