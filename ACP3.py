nums = [2, -5, 3, 4, -1, 6, -3]

current_sum = 0
max_sum = nums[0]

for num in nums:
    current_sum += num

    if current_sum > max_sum:
        max_sum = current_sum

    if current_sum < 0:
        current_sum = 0

print("Maximum Subarray Sum:", max_sum)