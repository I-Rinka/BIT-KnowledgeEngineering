d={}
for i in range(10):
    if not 'a' in d:
        d['a']=1
    else:
        d['a']=d['a']+i
print(d)