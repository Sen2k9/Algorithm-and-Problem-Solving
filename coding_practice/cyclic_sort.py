def cyclic_sort(nums):
    # TODO: Write your code here
    idx = 0
    while idx < len(nums):
        # import pdb;pdb.set_trace()
        curr_idx = nums[idx] - 1
        if idx == curr_idx:
            idx += 1
        else:
            nums[idx], nums[curr_idx] = nums[curr_idx], nums[idx]
        print(nums)
    return nums

print(cyclic_sort([1, 5, 6, 4, 3, 2]))