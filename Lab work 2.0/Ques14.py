d1 = {'a': 100, 'b': 200, 'c': 300}
ans = False

for i in d1:
    if d1[i]==200:
        ans=True
        
        break
    else:
        continue
    
if(ans==True):
    print("200 is there")
    
else:
    print("200 is not there")