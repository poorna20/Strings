s=input()
i=0
sign=1
res=0
if (s[0]=='-'):
    sign=-1
    i+=1
while i<len(s):
    res=res*10+(ord(s[i])-ord('0'))
    i+=1
print (res*sign)
