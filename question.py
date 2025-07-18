"""
count the number of pair whose absolute difference is equal to k in a given array

"""

k = int(input("Enter a number"))
array = list(map(int, input("Enter the list with a space").split()))
count = 0
array_set = set(array)

for i in array_set:
    if i + k in array_set:
        count += 1

print(count)

"""
find odd even without conditions or loop
"""

k = int(input())
array = ["Even", "Odd"]
print(array[k%2])