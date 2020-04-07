def tostring(a):
    return ''.join(a)

def permu(a,l,r):
    if (l==r):
        print (tostring(a))
    else:
        for i in range(l,1+r):
            a[l],a[i]=a[i],a[l]
            permu(a,l+1,r)
            a[l],a[i]=a[i],a[l]
           

s=input()
a=list(s)
n=len(a)
permu(a,0,n-1)
