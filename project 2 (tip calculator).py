#print("welcome to the tip calculator !")
bill=float(input("what was the total bill ?=₹"))
tip=float(input("how much tip do you like to give ?=in%"))
no_of_people=int(input("how many people to split the bill?="))
#calculation of bill
total_tip=(tip/100)*bill
total_bill= bill +total_tip
total_amount_per_person=round(total_bill/no_of_people,2)
#total money
print(f"each person should pay:₹{total_amount_per_person}")