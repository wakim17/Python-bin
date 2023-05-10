

pas = int(input("Enter the number of passengers in your taxi: "))
if pas == 1:
    strtprice = 2.50
    print("The starting price is £" + format(strtprice, ",.2f"))
elif pas == 2:
    strtprice = 3.00
    print("The starting price is £" + format(strtprice, ",.2f"))
elif pas == 3:
    strtprice = 3.50
    print("The starting price is £" + format(strtprice, ",.2f"))
elif pas == 4:
    strtprice = 4.00
    print("The starting price is £" + format(strtprice, ",.2f"))
elif pas >= 5:
    strtprice = 5.00
    print("The starting price is £" + format(strtprice, ",.2f"))
else:
    print("Run the program again")
