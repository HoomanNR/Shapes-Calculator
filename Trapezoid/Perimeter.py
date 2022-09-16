#Greetings
print("Hi there")

#Getting Information
Base1 = input("Enter the trapezoid first base : ")
Base1 = float(Base1)
Base2 = input("Enter the trapzoid second base : ")
Base2 = float(Base2)
Side1 = input("Enter the trapezoid first side : ")
Side1 = float(Side1)
Side2 = input("Enter the trapezoid second side : ")
Side2 = float(Side2)

#Giving Information
print("")
Perimeter = Base1 + Base2 + Side1 + Side2
Perimeter = round(Perimeter , 3)
print("The trapezoid perimeter is = " , Perimeter)
print("Have a nice day ...")