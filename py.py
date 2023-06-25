##Question: 01:


def moveZeroes(nums):
    next_non_zero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[next_non_zero] = nums[i]
            next_non_zero += 1
    while next_non_zero < len(nums):
        nums[next_non_zero] = 0
        next_non_zero += 1

# Example:
nums = [0]
moveZeroes(nums)
print(nums)

nums = [0,1,0,3,12]
moveZeroes(nums)
print(nums)
