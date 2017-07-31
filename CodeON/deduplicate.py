nums = [1, 1, 2,2,2,4,4,5]


def deduplicate_s(nums):
    if len(nums)<2:
        return nums

    head = nums[0]

    if nums[1]==head:
        return deduplicate_s([i for i in nums[1:] if i!=head])
    if nums[1]!=head:
        return deduplicate_s(nums[1:])+[head]

r = deduplicate_s(nums)

print(r)

def deduplicate(nums):
    i = 0

    while i<len(nums)-1:
        if nums[i]==nums[i+1]:
            nums.remove(i+1)
        i+=1
    print(len(nums))
deduplicate(nums)

## divide and conquer
def deduplicate_2(nums):
    if len(nums) <2:
        return nums

    head = nums[0]
    deduplicate_l = deduplicate_2([i for i in nums if i!=head])
    return deduplicate_l+[head]

l = deduplicate_2(nums)
print(l)

