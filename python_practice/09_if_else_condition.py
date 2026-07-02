# if statement ka matlab hota hai han yan na, if else statments tab use hoti hain jab hamain code main koi condition ue karni hai tab hum if elif else conditions use kar ke is problem ko solve karte hain



#  1 
age = int (input("Enter your age:"))

if age >= 100:
    print("you are too old to signed up!")
elif age >= 18:
    print("you are now signed up!")
elif age < 0:
    print("you haven't been born not yet!")
else:
    print("you must be 18+ to signed up!")
    
    
    
#  2
response = input ("Would you like food? (Y/N)")

if response == "Y":
    print("Have some food!")
else:
    print("No food for you!")
    
    
    
#  3
name = input ("Enter your name!")

if name == "":
    print("you did not a type in your name.")
else:
    print(f"Hello, {name}")
    
    
    
#  4
for_sale = True

if for_sale:
    print("This item is for sale!")
elif for_sale == False:
    print("This item is not for sale currently!")
    
    