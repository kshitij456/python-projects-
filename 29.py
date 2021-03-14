def sort(nums):
    for i in range(len(nums)-1):
        minpos=i
        for j in range(i,len(nums)):
            if nums[j]<nums[minpos]:
                minpos=j

        temp=nums[i]
        nums[i]=nums[minpos]
        nums[minpos]=temp

nums=[5,8,9,2,4,1,3,45,89,63,23,87,75,64]
sort(nums)

print(nums)
print('"selection sort"')