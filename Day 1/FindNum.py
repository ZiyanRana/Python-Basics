def findNum (array, num):
    for n in array:
        if (n == num):
            return True
    return False

array = [10,20,30,40,50]
num = int (input ("Enter number to find: "))
if (findNum(array, num)):
    print ("Number found.")
else:
    print ("Number not found.")