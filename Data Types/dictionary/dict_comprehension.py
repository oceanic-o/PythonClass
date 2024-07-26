myDict = {x: x**2 for x in [1,2,3,4,5]}
print (myDict)


#using Zip Function to create dictionary
keys = ['a','b','c','d','e']
values = [1,2,3,4,5]  

myDict = { k:v for (k,v) in zip(keys, values)}  

print (myDict)