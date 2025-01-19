# string 

name = input("Enter your name : \n")
age = int(input("Enter your age :\n"))

if age >= 18:
    print(f"Helow , {name} you are able to submit application for Identificatioin card .")
else:
    print(f"Sorry , {name} you are not able to submit application for Identificatioin card as you are below 18 years old.")