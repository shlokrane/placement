def reverse(A,  start, end):
    while start<end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1

A=[]
n=int(input("Enter number of elements in array: \n"))
for i in range(n):
    x=int(input("Enter element: "))
    A.append(x)

reverse(A,0,n-1)
for i in range(n):
    print(A[i], end=" ")

