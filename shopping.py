product1 = input("Please enter your first product:")
product2 = input("Please enter your second product:")
product3 = input("Please enter your third product:")

price1 = float(input(f"Please enter the price of {product1}:"))
round(price1, 2)

price2 = float(input(f"please enter the price of {product2}:"))
round(price2, 2)

price3 = float(input(f"Please enter the price of {product3}:"))
round(price3, 2)

total_sum = price1 + price2 + price3
round(total_sum, 2)

average = total_sum / 3
round(average, 2)

print(f"The total of {product1}, {product2},{product3} is R{total_sum} and the average price is R{average}")

#Thank for the link to the round() function, i was clueless.
