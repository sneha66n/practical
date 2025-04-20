'''num = input("Enter numbers separated by spaces: ").split()
largest=max(num)
smallest=min(num)
print(largest)
print(smallest)
'''
'''
L = [ ]
Element = input("number of element in list ")
For i in range(Element)
     Y = Input("Enter in list ")
     L.append(Y)
largest=max(L)
smallest=min(L)
print(largest)
print(smallest)'''


L = []
elements = int(input("Number of elements in list: "))

for i in range(elements):
    y = int(input("Enter element"))
    L.append(y)

largest = max(L)
smallest = min(L)

print("Largest element:", largest)
print("Smallest element:", smallest)


