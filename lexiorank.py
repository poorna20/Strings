def fact(n):
    f=1
    while n>=1:
        f=f*n
        n=n-1
    return f

def countsmaller(s,l,h):
    i=l+1
    count=0
    while i<=h:
        if s[i]<s[l]:
            count+=1
        i+=1
    return count

def rank(s):
    rank=1
    n=len(s)
    left=fact(n)
    i=0
    while i<n:
        left=left/(n-i)
        small=countsmaller(s,0,n-1)
        rank+=left*small
        i+=1
    print (int(rank))
s=input()
rank(s)
