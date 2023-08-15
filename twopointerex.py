nums1 = [1,3,6,8]
nums2 = [5,2,2,4,]
target = 9
maxii = 0
for i in range(len(nums1)):
    for j in range(len(nums2)):
        summ = nums1[i] + nums2[j]
        if summ <= 9:
            maxii = max(maxii,summ)
print(maxii)

