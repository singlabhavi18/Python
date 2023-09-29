list1 = [5, 20, 15, 20, 25, 50, 20]
# remove_ele = 20

# list1 = list(filter(lambda x: x!=remove_ele, list1))

# print(list1)

for i in list1:
    if(i==20):
        list1.remove(i)
        
print(list1)