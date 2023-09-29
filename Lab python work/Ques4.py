lst = []
while True:
    x = input("Enter the element for the list: ")
    lst.append(x)
    z = input("Do you want to continue? [Y/N]: ")
    if z.upper() == "N":
        break
    elif z.upper() == "Y":
        pass
    else:
        print("Invalid response.")
while True:
    print("1) Insert\n2) Delete")
    x = int(input("Enter your choice: "))
    if x == 1:
        pos = int(input("Enter the position: "))
        if pos >= len(lst):
            print("Invalid index.")
        else:
            ele = input("Enter the element: ")
            lst.insert(pos, ele)
    elif x == 2:
        print("1) Deletion by position\n 2) Deletion by value\n3) Deletion by slicing")
        y = int(input("Enter your choice: "))
        if y == 1:
            index = int(input("Enter the position: "))
            if index >= len(lst):
                print("Invalid index.")
            else:
                lst.pop(index)
        elif y == 2:
            val = input("Enter the value: ")
            if val not in lst:
                print("Invalid value.")
            else:
                lst.remove(val)
        elif y == 3:
            pos1 = int(input("Enter the first position: "))
            pos2 = int(input("Enter the second position: "))
            if pos2 < pos1:
                print("Invalid operation.")
            elif pos1 >= len(lst) and pos2 >= len(lst):
                print("Invalid positions. ")
            else:
                lst = lst[:pos1] + lst[pos2 + 1:]
        z = input("Do you want to perform anymore operations? [Y/N]: ")
        if z.upper() == "N":
            break
print(lst)