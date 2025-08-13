

FlourAMT=int(input("enter how many KGs of flour needed: "))
BeansAMT=int(input("enter how many Cans of beans needed: "))
UpNGoAMT=int(input("enter how many bottles of Up and Go needed: "))
BreadAMT=int(input("enter how many loafs of Bread needed: "))
FlourPrice=4.5*FlourAMT
BeansPrice=2.5*BeansAMT
UpnGoPrice=4.8*UpNGoAMT
BreadPrice=4.6*BreadAMT
TotalPrice=FlourPrice+BeansPrice+UpnGoPrice+BreadPrice
print("total Flour amount: " + str(FlourPrice))
print("total Beans amount: " + str(BeansPrice))
print("total Up and Go amount: " + str(UpnGoPrice))

