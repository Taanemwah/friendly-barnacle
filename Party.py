SnackAMT=int(input("Enter Amount Of Snacks needed: "))
SnackVAL=SnackAMT*25
DrinksAMT=int(input("Enter Amount Of Drinks needed: "))
DrinksVAL=DrinksAMT*40
DecoAMT=int(input("Enter Amount Of Decorations needed: "))
DecoVAL=DecoAMT*15
TotalVAL=DecoVAL+DrinksVAL+SnackVAL
ServFee=TotalVAL*1.10
print("Total Snacks Price: " + str(SnackVAL))
print("Total Drinks Price: " + str(DrinksVAL))
print("Total Deco Price: " + str(DecoVAL))
print("+10% service fee")
print("Total Price: " + str(ServFee))