print("enter the number by spaces from which mean is to be calculate.  ")
num=list(map(float,input().split()))
i=0
sum=0
while(i<len(num)) :
    sum+=num[i]
    i+=1

x=sum/len(num)   

total=0
k=0
while(k<len(num)):
    total+=(num[k]-x)**2
    k+=1

print("the standard derivation is : ", (total/len(num))**(1/2) )    