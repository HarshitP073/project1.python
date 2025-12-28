def fibonacci(n):
    if(n==1 or n==2):
        return n-1
    
    return fibonacci(n-1) + fibonacci(n-2)

print("enter the number upto which fibo is require")
n=int(input())
i=1
while(i<=n):
    print(fibonacci(i))
    i+=1