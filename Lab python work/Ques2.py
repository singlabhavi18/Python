l1 = []
n = int(input("Enter the size of list l1: "))
for i in range(n):
    x = int(input(f"Enter the element {i+1}: "))
    l1.append(x)
    

l2 = []
m = int(input("Enter the size of list l2: "))
for j in range(m):
    y = int(input(f"Enter the element {j+1}: "))
    l2.append(y)
    
    
for items in l2:
    l1.append(items)
    l1.sort()
    
print(l1)
        

