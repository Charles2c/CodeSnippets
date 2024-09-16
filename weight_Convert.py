weight = float(input("Weight: "))
conversion = input("(K)g or (L)bs: ")

if conversion.upper() == "K":
    weightl = weight * 2.2
    print("Weight in Lbs: " + str(weightl))
elif conversion.upper() == "L":
    weightk = weight / 2.2
    print("Weight in Kgs: " + str(weightk))
else:
    print("You did not enter 'K' or 'L'.")