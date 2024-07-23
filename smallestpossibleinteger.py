def removeKdigits(num, k):
    stack = []
    for digit in num:
        while k > 0 and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    stack = stack[:-k] if k else stack
    return ''.join(stack).lstrip('0') or '0'
def main():
    num = "1432219"
    k = 3
    print(f"Smallest possible integer after removing {k} digits: {removeKdigits(num, k)}")
if __name__ == "__main__":
    main()
