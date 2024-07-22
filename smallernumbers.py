def smallerNumbersThanCurrent(nums):
    sorted_nums = sorted(nums)
    count_smaller = {}
    for i, num in enumerate(sorted_nums):
        if num not in count_smaller:
            count_smaller[num] = i
    result = [count_smaller[num] for num in nums]
    return result
nums = [8, 1, 2, 2, 3]
print(smallerNumbersThanCurrent(nums)) 
