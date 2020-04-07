
def reverse(s):
    if (len(s)==0):
        print (" ")
    else:
        temp=s[0]
        reverse(s[1:])
        print (temp,end='')

s=input()
reverse(s)

