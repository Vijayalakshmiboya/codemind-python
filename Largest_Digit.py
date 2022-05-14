n=int(input())
largest=0
while(n):
    r=n%10
    n=n//10
    if(largest<r):
        largest=r
print(largest)