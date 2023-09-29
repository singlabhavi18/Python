s = input("Enter the String: ")
lower = 0
upper = 0
symbol = 0
digits = 0

for i in s:
    if('a'<=i<='z'):
        lower = lower+1
    elif('A'<=i<='Z'):
        upper = upper+1
    elif("0"<=i<="9"):
        digits = digits+1
    else:
        symbol = symbol+1

alphabets = lower + upper

print("lower", lower)
print("digits: ", digits)
print("upper: ", upper)
print("symbols: ", symbol)
print("alphabets: ", alphabets)

