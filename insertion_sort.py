def sort1(nums):
    n=len(nums)
    for i in range(1,n):
        j=i
        while nums[j-1]>nums[j] and j>0:
            nums[j-1],nums[j]=nums[j],nums[j-1]
            j=j-1
arr=[6,5,4,3,2,1]
sort1(arr)
print(arr)