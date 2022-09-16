#Greetings
print("Hi there")

#Getting Information
Base1 = input("Enter the trapezoid first base : ")
Base1 = float(Base1)
Base2 = input("Enter the trapzoid second base : ")
Base2 = float(Base2)
Height = input("Enter the trapzoid height : ")
Height = float(Height)

#Giving Information
print("")
Area = ( ( Base1 + Base2 ) / 2 ) * Height
Area = round(Area , 3)
print("The trapezoid area is = " , Area)
print("Have a nice day ...")