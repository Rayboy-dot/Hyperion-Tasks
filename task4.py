# Declare variable
num = int(input("please enter a whole number:"))

# Determine if num is divisible

if (num % 2 == 0) and (num % 5 == 0):
    print("num is divisible by 2 and by 5")

elif (num % 2 == 0) or (num % 5 == 0):
    print("num is divisible by 2 or by 5.")

else:
    print("Not divisible by 2 or 5.")

    