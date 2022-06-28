n=int(input())
sum=0
d=n*n
while(d>0):
    r=d%10
    sum=sum+r
    d=d//10
if(sum==n):
    print("Neon Number")
else:
    print("Not Neon Number")