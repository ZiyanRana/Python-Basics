writeFile = open("test.txt", "w")
writeFile.write("John - Student\nHarry - Teacher\nAlan - Singer\nDarren - Cricketer")
writeFile.close()

print("First cycle: ")
readFile = open("test.txt", "r")
print(readFile.readline())
print(readFile.readlines()[1:])
readFile.close()

print("\nSecond cycle: ")
readFile2 = open("test.txt", "r")
for line in readFile2.readlines():
    print(line)
readFile2.close()

print("\nThird cycle:")
readFile3 = open("test.txt", "r")
print(f"{readFile3.read()}")
readFile3.close()