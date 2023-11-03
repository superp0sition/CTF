def find_subset_with_target(numbers, target, current_sum, index, subset):
    if current_sum == target:
        return subset
    if current_sum > target or index == len(numbers):
        return None

    # Include the current number in the subset
    include = find_subset_with_target(numbers, target, current_sum + numbers[index], index + 1, subset + [numbers[index]])
    if include:
        return include

    # Exclude the current number from the subset
    exclude = find_subset_with_target(numbers, target, current_sum, index + 1, subset)
    if exclude:
        return exclude

    return None

# Your shuffled choices
choices = [19728964, 30673077, 137289540, 195938621, 207242611, 237735979, 298141799, 302597011, 387047012, 405520686, 424852916, 461998372, 463977415, 528505766, 557896298, 603269308, 613528675, 621228168, 654758801, 670668388, 741571487, 753993381, 763314787, 770263388, 806543382, 864409584, 875042623, 875651556, 918697500, 946831967]

# Target sum
target = 7627676296

# Initialize the search
result = find_subset_with_target(choices, target, 0, 0, [])

if result:
    print("Winning Subset:", result)
    print("Sum of Winners:", sum(result))
    flag = "UDCTF{%s}" % ("_".join(map(str, result)))
    print(flag)
else:
    print("No subset found that sums to the target.")