#Program to add two 3D arrays.

A = [[[1,2,3],[0,9,2],[1,4,9]]]
B = [[[0,0,0],[0,0,0],[1,0,0]]]
C = []

for i in range(1):
    list1=[]
    for j in range(3):
        list2=[]
        for k in range(3):
            list2.append(A[i][j][k]+B[i][j][k])
    
        list1.append(list2)
    C.append(list1)

print(C)