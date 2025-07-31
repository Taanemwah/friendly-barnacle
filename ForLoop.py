for loopcounter in range(1,7):
    ItemUnitPrice = int(input("Enter unit price "))
    AmountPurchased = int(input("Enter amount purchased "))
    BeMult = int(input("enter Number to be multiplied"))
    ItemSubtotal = ItemUnitPrice * AmountPurchased
    result = BeMult*loopcounter
    print("Subtotal is " + str(ItemSubtotal))
    