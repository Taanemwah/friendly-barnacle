RunningTotal = 0.0
for x in range(4):
    ProductDesc = float(input("Enter Amount sold: "))
    ProductPrice = float(input("Enter product price: "))
    RunningTotal += ProductPrice
print("Total: ", RunningTotal)