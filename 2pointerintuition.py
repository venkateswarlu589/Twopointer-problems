n = int(input())
a = [0] * (n + 1)
b = [0] * (n + 1)
 
i = 1
while i <= n:
    a[i] = int(input())
    i += 1
 
i = 1
while i <= n:
    b[i] = int(input())
    i += 1
 
y = int(input())
first = 0
second = 0
v = 0
j = n
i = 1
kk = 0
while i <= n and j >= 1:
    if a[i] + b[j] <= y:
        sum = a[i] + b[j]
        if sum > v:
            v = sum
            first = a[i]
            second = b[j]
        i += 1
    else:
        j -= 1
 
print(v)