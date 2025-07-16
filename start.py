GST_RATE = 0.15
productName = input("Enter product name ")
productPrice = input("Enter unit price of product ")
amountPurchased = int(input("Enter amount purchased "))
saleTotal = int(productPrice) * int(amountPurchased)
print("product name:" + productName)
print("price: " + str(productPrice) )
print("amount purchased: " + str(amountPurchased))
print("Total sales: " + str(saleTotal))
