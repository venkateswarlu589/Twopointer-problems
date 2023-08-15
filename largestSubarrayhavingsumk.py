nums = [1,2,4,6,3,7,8]
k = 7
i = 0
j = 0
res = 0
sum = 0
while i < len(nums):
    while j < len(nums) and sum <= k:
        sum += nums[j]
        j += 1
    res = max(res,j-i)
    sum -= nums[i]
    i += 1
print(res)
     