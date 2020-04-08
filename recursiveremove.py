def remove(s,lastremoved):
    if len(s)==0 or len(s)==1:
        return s
    if s[1]==s[0]:
        lastremoved=ord(s[0])
        while len(s)>0 and s[0]==s[1]:
            s=s[1:]
        s=s[1:]
        return remove(s,lastremoved)
    remstr=remove(s[1:],lastremoved)
    if len(remstr)!=0 and remstr[0]==s[0]:
        lastremoved=ord(s[0])
        return (remstr[1:])
    if len(remstr)==0 and lastremoved==ord(s[0]):
        return (remstr)
    return(s[0]+remstr)



s=input()
print (remove(s,0))
