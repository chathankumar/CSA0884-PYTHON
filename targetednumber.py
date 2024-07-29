def search_range(nums, target):
    def find_boundary(nums, target, find_start):
        left, right = 0, len(nums) - 1
        pos = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                pos = mid
                if find_start:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return pos

    start = find_boundary(nums, target, True)
    end = find_boundary(nums, target, False)
    return [start, end] if start != -1 else [-1, -1]

nums = [5, 7, 7, 8, 8, 10]
target = 8
print(search_range(nums, target))
