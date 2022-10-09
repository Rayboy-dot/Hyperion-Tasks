# Declaring variables that will be used.
num = 0
count= 0
average = 0
total_sum =0

while num != - 1:               # The condition
    num= int(input("Enter a number: "))
    count += 1
    total_sum += num            # The total sum of all inputed numbers
    if num == -1:
       total_sum += 1           
       count -= 1               # To remove the number -1 from being added to average count
       break
  
  # Calculate the average 
average = total_sum/count
print(average)

#Thanks Tammy for your assistance