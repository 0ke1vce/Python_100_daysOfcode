
# Tuple are immutable list in which data cannot be modified once created
t = (3,)  # this is a tuple with  a single element
t1 = (3,4,45,32,23)
t1.count(3)   
t1.index(45)
len(t1)


# Changing indirectlt in tuples.
countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)