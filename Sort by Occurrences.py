def sort_by_frequency(nums):
    return sorted(nums, key=nums.count, reverse=True)
list = [1, 1, 2, 2, 2, 3]
result = sort_by_frequency(list)
print(result)
