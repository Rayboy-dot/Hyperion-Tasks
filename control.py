# Write a code to request user to enter their age. determine using if-elif-else  statement to allow or not a user access to a party with age limit 18

 
age = int(input("Please enter your age:"))

if age >= 18:
    print("You are old enough.")

elif age==17:
    print("Almost there")

else:
    print("You are just too young.")