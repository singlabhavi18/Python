# Find the sum of the series 2 +22 + 222 + 2222 + .. n terms

sum = 0
n = int(input("Enter the number of terms: "))
x = 0

for i in range(n):
    x = x*10 + 2
    sum = sum + x
    
print(sum)