TuitionFees=int(input("Enter The Tuition Fee Price: "))
SchoolUniform=int(input("Enter The School Uniform Price: "))
SportsGear=int(input("Enter The Sports Gear Price: "))
Textbooks=int(input("Enter The Textbooks Price: "))
TotalCost= Textbooks+SportsGear+SchoolUniform+TuitionFees

print("Tuition Fees Price: " + str(TuitionFees) + " School Uniform Price: " + str(SchoolUniform) + " Sports Gear Price: " + str(SportsGear) + " Textbooks Price: " + str(Textbooks))
print("Total Cost: " + str(TotalCost))