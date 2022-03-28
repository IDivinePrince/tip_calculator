#Infinite's tip calculator intro
print("Greetings, Welcome to Infinite's Tip Calculator, I will assist you in calculating your bill")
#Concepts and code logic Resources referenced using https://www.youtube.com/watch?v=cBDka0lKImI


# 1. Ask the bill amount.
food_cost = float(input("How much is the total bill?:\n"))
#float function allows for the bill amount given to have decimals.
#Float class is necessary since the bill amount entered (input) may contain a decimal.
# \n allows user's answer to print on a seperate line.

#2. Ask the user for the percentage of the tip they're willing to provide.
tip = int(input('What is the tip percentage?:\n'))

#3. As instructed, Include a 10 percent sales tax to the your meal non arbitrarily.
sales_tax = .10


#4. Ask how many people are splitting the bill.
people = int(input("How many people are splitting the bill:\n?"))

#5. Calculate the bill.
food_with_tip = (food_cost * tip/100) 
food_with_sales_tax = food_cost * sales_tax
food_with_both_taxes = food_cost + food_with_tip + food_with_sales_tax
final_avg = (food_cost + food_with_sales_tax + food_with_tip)/people


#6. Ensure that the final amount displayed is rounded 2 decimal digits.
#Adding a colon,dot, "2f" formats integers and floats referencing https://www.youtube.com/watch?v=cBDka0lKImI

#7. Show the bill on screen using f-string.
print(f'Your 10% sales tax total is ${food_with_sales_tax:.2f} and your food total with tax and tip included is ${food_with_both_taxes:.2f} ')
print(f'The total amount each person should pay is ${final_avg:.2f}')