def sort1(nums):
    n=len(nums)
    for i in range(n):
        minpos=i
        for j in range(i,n):
            if nums[j]<nums[minpos]:
                minpos=j
        nums[i],nums[minpos]=nums[minpos],nums[i]
arr=[6,5,4,3,2,1]
sort1(arr)
print(arr)