numbers = [1,2,3,4,5]
names = ['ali', 'king', 'john', 'jack', 'king', 'drag']

names.extend(numbers)
print(names)
print("John's index is:", names.index('john'))

names.insert(1, 'bob')
names.remove('jack')
names.pop()
print(names)

print("John's new index:", names.index('john'))
print("Appearances of king:", names.count('king'))

names.clear()
print("The array left is:", names)