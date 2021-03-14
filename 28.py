def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp

nums=[5,8,9,2,4,1,3,45,89,63,23,87,75,64]
sort(nums)

print(nums)
print('"Bubble sort"')