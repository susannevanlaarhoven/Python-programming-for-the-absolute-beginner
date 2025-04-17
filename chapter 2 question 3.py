# Write a Tipper program where the user enters a restaurant bill total. The program should then display two amounts:
#a 15 percent tip and a 20 percent tip.
bill = float(input("Please enter the bill total: "))
print("Your bill total including a 15% tip is: ", round((bill*1.15),2))
print("Your bill total including a 20% tip is: ", round((bill*1.2),2))
