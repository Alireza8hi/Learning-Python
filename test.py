def two_sum(nums, target):
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]  # indices of the two numbers
        seen[num] = i
    return None
  
print(two_sum([1, 2, 3, 4], 5))