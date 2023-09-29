vowels =['a','e','i','o','u','A','E','I','O','U']
str = str(input("input your string: "))
h =''
for i in str:
    if i not in vowels:
     h= h+i
    else:
        continue
words = h.split()
ans = max(words,key = len)
print("longest common subsequence",ans)