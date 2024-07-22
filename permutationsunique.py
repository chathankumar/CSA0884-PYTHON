def permuteUnique(nums):
    def backtrack(path):
        if len(path) == len(nums):
            result.append(path[:]) 
            return
        for i in range(len(nums)):
            if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
                continue
            path.append(nums[i])
            used[i] = True
            backtrack(path)
            path.pop()
            used[i] = False
    nums.sort()
    result = []
    used = [False] * len(nums)
    backtrack([])
    return result
nums = [1, 1, 2]
print(permuteUnique(nums))  
