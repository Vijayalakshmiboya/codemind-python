n=int(input())
s=0
while(n!=1 and n!=4):
    s=0
    while(n):
        j=n%10
        s=s+j*j
        n=n//10
    n=s
if(s==1):
    print("True")
else:
    print("False")