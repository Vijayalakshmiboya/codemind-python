n=int(input())
f=1
sum=0
temp=n
while(n):
    r=n%10
    for i in range(1,r+1):
        f=f*i
    sum=sum+f
    f=1
    n=n//10
n=temp
if(n==sum):
    print("The number %d is a strong number"%n)
else:
    print("The number %d is not a strong number"%n)