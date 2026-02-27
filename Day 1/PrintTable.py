def printTable (number):
    for idx in range (1,11,1):
        print (number, "X", idx, "=", number*idx)

number = int ( input ("Enter the number: "))
printTable(number)