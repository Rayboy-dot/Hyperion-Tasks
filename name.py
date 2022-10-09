# Declaring variables
name = 0
count = 0

while name != "Stop":                   # The condition
    name = input("Enter the name of the pupil in class,type 'Stop' to indicate all names have been entered: ")
    count += 1                          # Increment by 1 every a name is inputed and counting
    if  name == "Stop":
        count -= 1                      # Removing the word stop from printing on the list
        print(count)
        
        

        
