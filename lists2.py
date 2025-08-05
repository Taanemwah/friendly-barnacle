MyfirstList=["tom","sarah","Dick","mary","harry"]
print(MyfirstList)
for item in MyfirstList:
    print(item)

MySecondList = []
for counter in range(9):
 NewName = input("enter a name ")
MySecondList.append(NewName)
print("the number of the names in the list is" + str(len(MySecondList)))
print("the first element in the list is" + MySecondList[0])
for item in MySecondList:
    print(item)