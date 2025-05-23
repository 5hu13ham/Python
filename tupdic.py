friends = []
for x in range(4):
    friends.append(input("Enter a friend name: "))

#functional way to convert a list into a tuple
bestfriend = tuple(friends)
print(bestfriend)

#typically a list with key-value pair
dictionary = {"Hello": "You're buffalo", "Pencil": "ha shadi cancel", "bacha": "kaccha"}

print(dictionary)
print(dictionary["bacha"])
print(dictionary[input("Enter the word you want to find in dictionary: ")])

#lists inside a tuple are mutable while tuples are immutable
a=3; b=2; c=1
exp_tup=([1,2,3],[a,b,c])

exp_tup[1][0] = 5
print(exp_tup)

#Single value tuple
single = 10,
print(len(single))
"""
############cannot be updated
single[0] = 20
print(single)
"""
#Unpacking of a tuple

list1, list2 = exp_tup
print(list1)
print(list2)

#packing of a tuple

pack_tup = 123, 234, 345
print(pack_tup)

"""
pack_tup[0] = 456
print(pack_tup[0])

########################not possible
"""
