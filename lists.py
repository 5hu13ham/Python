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
lunch_items = ("roti", "naam", "garlic bread", "butter", "shahi chicken")
for i in range(0, len(breakfast_items)):
        breakfast_items[i] = breakfast_items[i]+"ay"

breakfast_items.append("jamay")
breakfast_items.extend(lunch_items)
breakfast_items.sort()
breakfast_items.insert(3,"what's for dessert")
breakfast_items.remove("what's for dessert")
item = breakfast_items.pop()
breakfast_items.reverse()
print(breakfast_items.copy())
print(breakfast_items)
print(item)

from collections import deque
queue = deque(breakfast_items)
print(queue.popleft())
print(queue.pop())
print(queue)

print(list(map(lambda x : x**2,range(10))))

square = [x**2 for x in range(10)]
print(square)

matrix = [(x,y) for x in range(1,4) for y in range(1,4) if x!=y]
print (matrix)