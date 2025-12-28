print("enter the number by spaces from which mean is to be calculate.  ")
num=list(map(int,input().split()))
i=0
sum=0
while(i<len(num)) :
    sum+=num[i]
    i+=1

print("Mean of the observation is : ",sum/len(num))    
        