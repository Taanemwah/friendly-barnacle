RunningTotal=0.0
for x in range(1,8):
    ProDesc=input("enter item desc: ")
    Proprice=float(input("enter product price: "))
    ProAMT=int(input("enter amount purchasing: "))
    TotalCost=Proprice*ProAMT
    RunningTotal += Proprice
print("total: {RunningTotal}")