index = int(input("Enter matrix size (2 for 2x2, 3 for 3x3): "))

print("Enter first matrix:")
mat1 = []
for i in range(index):
    row = list(map(int, input().split()))
    mat1.append(row)

print("Enter second matrix:")
mat2 = []
for i in range(index):
    row = list(map(int, input().split()))
    mat2.append(row)

sum = []
for i in range(index):
    row = []
    for j in range(index):
        row.append(mat1[i][j] + mat2[i][j])
    sum.append(row)

print("Resultant Matrix:")
for row in sum:
    print(row)

                         
                 

