num=int(input("enter the digit upto count"))
i=1
while(i<=num):
    if(i%15==0):
        print("FIZZBUZZ")
    elif(i%3==0):
        print("FIZZ")
    elif(i%5==0):
        print("BUZZ")
    else:
        print(i)

    i+=1    

print("THANK YOU !!")    
