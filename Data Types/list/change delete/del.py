
fruits = ['apple', 'banana', 'mango', 'orange']
print(' Before delete:', fruits)

del fruits[1]
print('After delete:', fruits)

del fruits[1:3]
print('After multiple delete:', fruits)

del fruits
print("After deleting the list", fruits)