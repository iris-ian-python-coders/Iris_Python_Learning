#Wed Jul 22, 2026


#Conditionals and defining fuctions
#Before edits:
x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
z = int(input("Enter another number: "))

if x > y:
   print(f"{x} is greater than {y}")
elif x < y:
   print(f"{x} is less than {y}")
else:
   print(f"{x} is equal to {y}")

if x > z:
   print(f"{x} is greater than {z}")
elif x < z:
   print(f"{x} is less than {z}")
else:
   print(f"{x} is equal to {z}")

if y > z:
   print(f"{y} is greater than {z}")
elif y < z:
   print(f"{y} is less than {z}")
else:
   print(f"{y} is equal to {z}")


#After edits:
def compare(a, b):
   if a > b:
       print(f"{a} is greater than {b}")
   elif a < b:
       print(f"{a} is less than {b}")
   else:
       print(f"{a} is equal to {b}")

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
z = int(input("Enter the third number: "))

compare(x, y)
compare(x, z)
compare(y, z)

