def mean(lst):
   p=len(lst) 
   if(p==0):
      print("list is empty")
    
   else:
      i=0
      sum=0
      while(i<p):
         sum+=lst[i]
         i+=1

      print("the mean is : ", sum/p)
   

def median(lst):
   p=len(lst)
   if(p==0):
      print("NO MEDIAN LIST IS EMPTY") 

   else:
      i=0
      k=0
      p=len(lst)
      for i in range(p):
         for k in range(p-1):
            if(lst[k] > lst[k+1]):
               temp=lst[k]
               lst[k]=lst[k+1]
               lst[k+1]=temp
      if(p%2!=0):
         med=(p+1)//2
         print("the median : ",lst[med-1]) 
      else:
         med=p/2
         med2=p/2+1
         print("the median : ",(lst[med-1]+lst[med2-1])/2)           
        
def mode(lst):  
    if len(lst) == 0:
        print("No mode, list is empty")
        return

    freq = {}
    for num in lst:
        freq[num] = freq.get(num, 0) + 1

    max_freq = max(freq.values())
    modes = []

    for key in freq:
        if freq[key] == max_freq:
            modes.append(key)

    if len(modes) == len(lst):
        print("No mode (all values appear equally)")
    else:
        print("Mode:", modes)





print("ENTER THE NUMBER : ")
lst=list(map(int,input().split()))   
mean(lst)
median(lst)
mode(lst)







