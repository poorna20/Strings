s=input()
a=list(s)
odd=[]
eve=[]
for i in range(1,len(a),2):
    eve.append(a[i])
    odd.append(a[i-1])
for i in odd:
    print (i,end='')
for i in eve:
    print (i,end='')
