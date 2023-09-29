def dog_str(string):
    s = string.lower().split()
    
    for i in s:
        if(i == "dog"):
            return True
            break
string = input("Enter the string: ")

print(dog_str(string))