numbers = [1,1,1,1,1,1,5,10,11,12,4,2,3,6,1,7,8]
print(numbers.count(1))
numbers.sort()
print(numbers)

"""
Write an application that (attempts to) encrypt your grocery list using a very simple version of Pig Latin. Using a loop, change the value for every grocery item using the following rule:

Append "-ay" to the end of the word
Using our original grocery list as an example, your output should read:

["milkay", "eggsay", "breaday", "butteray", "baconay"]

"""

breakfast_items = ["milk", "egg", "bread", "butter", "bacon"]
for i in range(0, len(breakfast_items)):
        breakfast_items[i] = breakfast_items[i]+"ay"

print(breakfast_items)