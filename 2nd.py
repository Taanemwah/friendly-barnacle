ProductName= input("enter product name")
UnitPrice=float(input("enter unit price"))
AmountSold=int(input("enter amount sold"))
TotalSale=UnitPrice*AmountSold
if TotalSale>100:
    discount=TotalSale*0.1
CostToCustomer=TotalSale-discount
print("Product:"+ProductName)
print("UnitPrice"+str(UnitPrice))
print("TotalSales"+str(TotalSale))
print("Customer price"+str(CostToCustomer))                          