country_capitals = {
  "Nepal": "Kathmandu", 
  "India":"New Delhi",
  "USA": "Washington, D.C."
}

for country in country_capitals:
    print(country)

# what will this print?


for country in country_capitals:
    capital = country_capitals[country]
    print(capital)

# what will this print?

keys = country_capitals.keys()
values = country_capitals.values()

#list comprehension of above 
keys = [key for key in country_capitals]
values = [country_capitals[key] for key in country_capitals]


#simplest way to loop and get key value
for key, value in country_capitals.items():
    print(f"key:{key}, value:{value}")