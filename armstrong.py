n = int(input())
number = str(n)
sum = 0
length = len(number)
for i in number:
    a = int(i)
    sum += a ** length
if sum == n:
    print("It is an Armstrong number")
else:
    print("NOT")