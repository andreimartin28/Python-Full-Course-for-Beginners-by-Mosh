weight = input("Weight: ")
unit = input("(L)bs or (K)g: ")

if unit.upper() == "L":
    print("You are " + str(float(weight) * 0.45) + " kg.")
else:
    print("You are " + str(float(weight) * 2.2) + " pounds.")


# Mosh's Solution
# weight = int(input('Weight: '))
# unit = input('(L)bs or (K)g: ')
# if unit.upper() == "L":
# converted = weight * 0.45 
# print(f"You are {converted} kilos.")
# else: 
#      converted = weight / 0.45 
#      print(f"You are {converted} pounds.")