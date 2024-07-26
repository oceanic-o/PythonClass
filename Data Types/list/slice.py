#accessing list element with slicing index

lan = ['python', 'java', 'javascript', 'c', 'cpp', 'kotlin', 'swift']

# items beginning to end
print(lan[:])

# items from index o to index 4
print(lan[0:5])

# items from index 6 to end
print(lan[6:])


'''Note: 
    there will be IndexError if the index exceed or not valid
'''