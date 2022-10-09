qualifing_time = int(100)

# Different time durations,cast to float
swim_time = float(input("Enter swimming time in minutes:"))
cycling_time = float(input("Enter cycling time in minutes:"))
run_time = float(input("Enter running time in minutes:"))

# Calculate total time and display
total_time = float(swim_time + cycling_time +run_time)
print(total_time)


# Giving awards based on time
if total_time <= qualifing_time:
    print("Congratulations, you won the provincial colours.")

elif total_time <= 105:
    print("Congratulations, you have won the provincial half colours.")

elif total_time <= 110:
    print("You won the provincial scroll.")

else:
    print("Sorry,You won nothing.")