n=int(input())
c=0
l=0
m=0
k=0
while(n>0):
    r=n%10
    c+=1
    n=n//10
    if(r%2==0):
        l+=1
    elif(r%2!=0):
        m+=1
    else:
        k+=1
if(c==l):
    print("Even")
elif(c==m):
    print("Odd")
else:
    print("Mixed")