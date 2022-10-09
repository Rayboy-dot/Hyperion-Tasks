num1=15
num2=22
num3=35

num1<num2
print(num3)

# determine if num1 is odd or even
if (num1 % 2 )== 0:
    print("num1 is even.")
else:
    print("num1 is odd.")

# Conditional statement to sort the 3 numbers from lrgest to smallest
if num1 > num2 and num1 > num3:
    third_number = num1
elif num1 < num2 and num1 < num3:
    first_number = num1
else:
    second_number = num1

if num2 > num1 and num2 > num3:
    third_number = num2
elif num2 < num1 and num2 < num3:
    first_number = num2
else:
    second_number = num2

if num3 > num1 and num3 > num2:
    third_number = num3
elif num3 < num1 and num3 < num2:
    first_number = num3
else:
    second_number = num3
print(f"{third_number}\n{second_number}\n{first_number}") 