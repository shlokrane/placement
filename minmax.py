def minmax(a):
    min_element = max_element = a[0]

    for i in a:
        if i < min_element:
            min_element = i
        if i > max_element:
            max_element = i

    print("Minimum element: ", min_element)
    print("Maximun element: ", max_element)
    #return min_element, max_element

a=[]
n=int(input("Enter number of elements in array: \n"))
for i in range(n):
    x=int(input("Enter element: "))
    a.append(x)

minmax(a)