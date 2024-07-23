def findDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)

def main():
    nums = [1, 3, 4, 2, 2]
    print(f"The repeated number is: {findDuplicate(nums)}")

if __name__ == "__main__":
    main()
