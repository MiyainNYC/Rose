nums = [1, 1, 2]

def deduplicate(nums):
    i = 0

    while i<len(nums)-1:
        if nums[i]==nums[i+1]:
            nums.remove(i+1)
        i+=1
    print(len(nums))
deduplicate(nums)