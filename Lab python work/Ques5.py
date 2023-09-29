strg = " "
x = int(input("Enter the size of string: "))
for i in range(x):
    l = str(input(f"Enter the element {i+1} of str: "))
    strg = strg + " " + l
    
z = strg.split()


List = []

for items in z:
    y = int(items)
    List.append(y)    
    
def selection_sort(array, size):
    for index in range(size):
        min_index = index
        
        for j in range(index+1, size):
            if(array[j]<array[min_index]):
                min_index= j
        
        (array[index], array[min_index]) = (array[min_index], array[index])


selection_sort(List, x)
print(List)