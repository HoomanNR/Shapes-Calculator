#Greetings
print("Hi there")

#Getting Information
BigDiameter = input("Enter the big diameter of diamond : ")
BigDiameter = float(BigDiameter)
SmallDiameter = input("Enter the small diameter of dimaond : ")
SmallDiameter = float(SmallDiameter)

#Giving Information
print("")
Area = ( BigDiameter * SmallDiameter ) / 2
Area = round(Area , 3)
print("The diamond area is = " , Area )
print("Have a nice day ...")