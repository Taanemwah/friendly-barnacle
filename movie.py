People=int(input("enter how many People "))
TicketCost=int(input("enter Ticket price "))
Food=int(input("enter Food price "))
TotalTickets= People * TicketCost 
TotalFood= People * Food
TotalPrice= TotalTickets + TotalFood
print("Total Ticket price: " + str(TotalTickets))
print("Total Food price: " + str(TotalFood))
print("Total Cost: " + str(TotalPrice))
