my_list = [3,3]
my_dict = {}
target = 6
for i, num in enumerate(my_list):
    comp = target - num
    if comp in my_dict:
        print(my_dict[comp], i)
        break
    my_dict[num] = i

print(my_dict)
print(my_list)