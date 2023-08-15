nums = [100,200,300,400]
k = 2
i= 0
j = 0
sum = 0
maxii = 0
while j < len(nums):
    sum += nums[j]
    if j - i+1 <k:
        j += 1
    elif j-i+1 == k:
        maxii = max(maxii,sum)
        sum -= nums[i]
        i += 1
        j += 1
print(maxii)