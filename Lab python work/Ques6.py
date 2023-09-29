n = int(input("Enter the number of students: "))
list1 = []
for i in range(n):
    Email = input(f"Enter the Email {i+1}: ")
    list1.append(Email)

tuple1 = tuple(list1)

names = []
domains = []

for items in tuple1:
    name,domain = items.split("@")
    names.append(name)
    domains.append(domain)
    
names = tuple(names)
domains = tuple(domains)

print("Names = ", names)
print("Domains = ", domains)
print("Tuple = ", tuple1)