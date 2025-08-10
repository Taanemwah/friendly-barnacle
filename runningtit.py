RunningTotal = 0.0
for x in range(4):
    ProductDesc = input("Enter product description: ")
    ProductPrice = float(input("Enter product price: "))
    RunningTotal += ProductPrice
    print("Total: ", RunningTotal)