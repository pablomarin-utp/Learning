def backtrack(nums, target, path, result):
    if target < 0:
        return
    if target == 0:
        result.append(path)
        return
    for i in range(len(nums)):
        backtrack(nums[i+1:], target - nums[i], path + [nums[i]], result)

def combination_sum(nums, target):
    result = []
    backtrack(nums, target, list(), result)
    return result

# Ejemplo de uso:
nums = [2, 3, 1, 6, 7]
target = 10
print("Combinaciones que suman", target, ":")
print(combination_sum(nums, target))
