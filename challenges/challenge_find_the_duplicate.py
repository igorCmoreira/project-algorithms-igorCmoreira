def find_duplicate(nums):
    nums.sort()
    counter = range(len(nums)-1)
    for i in counter:
        if nums[i] == nums[i+1] and nums[i] > 0:
            return nums[i]
    return False
