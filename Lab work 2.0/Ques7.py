def dog_str(string):
    s = string.lower().split()
    
    count = 0
    
    for i in s:
        if(i == "dog"):
            count += 1
    
    return count

string = input("Enter the string: ")

print(dog_str(string))