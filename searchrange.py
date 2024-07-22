def searchRange(nums, target):
    def find_position(is_first):
        left, right = 0, len(nums) - 1
        position = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                position = mid
                if is_first:
                    right = mid - 1 
                else:
                    left = mid + 1   
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return position

    start = find_position(is_first=True)
    end = find_position(is_first=False) if start != -1 else -1
    return [start, end]
nums = [5, 7, 7, 8, 8, 10]
target = 8
print(searchRange(nums, target))  # Output: [3, 4]
