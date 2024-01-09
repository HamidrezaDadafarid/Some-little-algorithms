def max_sum_non_adjacent(arr):
    if not arr:
        return 0
    incl = arr[0]
    excl = 0
    for i in range(1, len(arr)):
        new_excl = max(incl, excl)
        incl = excl + arr[i]
        excl = new_excl
    return max(incl, excl)

arr = [-1, 2, 3, -4, -5, 7]
print("Maximum sum of non-adjacent elements:", max_sum_non_adjacent(arr))
