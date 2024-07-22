from functools import cmp_to_key

def largestNumber(nums):
    if not any(nums):
        return "0"
    
    def compare(a, b):
        return (a + b > b + a) - (a + b < b + a)
    
    nums = map(str, nums)
    sorted_nums = sorted(nums, key=cmp_to_key(compare), reverse=True)
    return ''.join(sorted_nums)

# Example Usage:
nums = [3, 30, 34, 5, 9]
print(largestNumber(nums))  # Output: "9534330"
