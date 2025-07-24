DashCam=int(input("Enter Dashcams Needed: "))
FirstAid=int(input("Enter First Aid Kits Needed: "))
EmergKit=int(input("Enter Emergency Kits Needed: "))
AirComp=int(input("Enter Air Compressors Needed: "))
DashcamVAL= DashCam*500
FirstAidVAL= FirstAid*350
EmergKitVAL=  EmergKit*450
AirCompVAL= AirComp*280
TotalVAL= AirCompVAL+EmergKitVAL+FirstAidVAL+DashcamVAL*1.15
print("Total Dashcam Price: " + str(DashcamVAL))
print("Total First Aid Kit Price: " + str(FirstAidVAL))
print("Total Emergemcy Kit Price: " + str(EmergKitVAL))
print("Total Air Compressor Price: " + str(AirCompVAL))
print("+15% GST")
print("Total Price: " + str(TotalVAL))