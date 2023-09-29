string = input("Enter the string: ")
count_lower = 0
count_upper = 0
for i in string:
    if('a'<=i<='z'):
        count_lower=count_lower+1
    elif('A'<=i<='Z'):
        count_upper = count_upper+1
        
lower = count_lower
upper = count_upper

if (len(string)<5):
    print("Password not approved")
elif(lower<1):
    print("Password not approved")
elif(upper<1):
    print("Password not approved")
elif('&' not in string):
    print("Password not approved")
else:
    print("Password approved")