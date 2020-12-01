#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: You might need to do some research in Google to figure out how to do this.

print("Welcome to the tip calculator!")
bill = (float (input("How much was the bill? " )))

tip = (int(input("How much tip would you like to give? 10, 12, 15 ?  ")))

people = (int(input("How many people splitting the bill ? ")))

#short form
final_amount = round(bill * (1 + tip / 100) / people, 2)

print(f"Each person should pay: ${final_amount}")