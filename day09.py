with open("inputs/09.txt", "r") as File:
    lines = [[int(num) for num in line.split()] for line in File]

def next(nums):
    if not any(num for num in nums):
        return 0
    return nums[-1] + next([nums[i+1] - nums[i] for i in range(len(nums) - 1)])

def previous(nums):
    if not any(num for num in nums):
        return 0
    return nums[0] - previous([nums[i+1] - nums[i] for i in range(len(nums) - 1)])

print("Part 1 Answer:")
print(sum([next(nums) for nums in lines]))
print("Part 2 Answer:")
print(sum([previous(nums) for nums in lines]))