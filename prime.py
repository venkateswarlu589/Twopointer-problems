array = [3,4,5,6,7,8,9,10,11,12,13]
stack = []
for i in range(len(array)):
    stack.append([array[i],i])
print(stack)