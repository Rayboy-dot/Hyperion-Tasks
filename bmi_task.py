# Asking user to enter their weight and height and casting the values to float


weight = float(input("\nPlease enter your weight in kg:"))

height = float(input("Please enter your height in meter:"))

BMI = weight/(height*height)

if BMI>= 30:
    print("You are obese.")

elif BMI>=25:
    print("You are overweight")

elif BMI>=18.5:
    print("Your weight is normal.")

else:
    print("You are uderweight.")