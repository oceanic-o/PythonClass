fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

fruits_list = [x if x != "banana" else "orange" for x in fruits]

print(fruits_list)
