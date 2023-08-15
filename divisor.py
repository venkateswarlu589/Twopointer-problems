list_1 = [2,3,5]
n=14
stack =[]
for i in range(2,n+1):
    if n % i == 0:
        stack.append(i)
print(stack)