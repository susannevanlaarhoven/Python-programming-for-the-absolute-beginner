#Write a Car Salesman program where the user enters the base
#price of a car. The program should add on a bunch of extra fees
#such as tax, license, dealer prep, and destination charge. Make
#tax and license a percent of the base price. The other fees
#should be set values. Display the actual price of the car once
#all the extras are applied.

baseprice = float(input("What is the base price of the car? "))
tax = round((baseprice*0.13),2)
license = round((baseprice*0.1),2)
dealerprep = 50
destinationcharge = 125

print("\nTax is 13%. So for you car it is:",tax,".")
print("License is 10%. So for your car it is:",license,".")
print("Dealerprep will cost 50, and destination charge will be 125.")
print("\nThat makes the total price for your car:", baseprice+tax+license+dealerprep+destinationcharge, ".")
