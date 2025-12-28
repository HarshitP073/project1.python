def determinant(lst):
    row=len(lst)
    column=len(lst[0])
    if(row!=column):
        print("invalid matrix ")

    if(row==1):
        print("the value of det : ",lst[0])    

    if(row==2):
        det=lst[0][0]*lst[1][1]-lst[0][1]*lst[1][0]
        print("the value of determinant is ; ",det)

    if(row==3):    
        det1=lst[0][0]*(lst[1][1]*lst[2][2]-lst[1][2]*lst[2][1])  
        det2=lst[0][1]*(lst[1][0]*lst[2][2]-lst[1][2]*lst[2][0])
        det3=lst[0][2]*(lst[1][0]*lst[2][1]-lst[1][1]*lst[2][0])
        print("the value of determinant is : ",det1-det2+det3)

index = int(input("Enter matrix size (2 for 2x2, 3 for 3x3): "))

print("Enter first matrix:")
lst = []
for i in range(index):
    row = list(map(int, input().split()))
    lst.append(row)

determinant(lst)
