def merge_sort(nums, start, end):
    # If the list is a single element, return it
    if end <= start:
        return

    mid = start + ((end - start + 1) // 2) - 1
    yield from merge_sort(nums, start, mid)
    yield from merge_sort(nums, mid + 1, end)
    yield from merge(nums, start, mid, end)
    yield nums

def merge(nums, start, mid, end):
    sorted_list = []
    l_ind = start
    r_ind = mid + 1

    while l_ind <= mid and r_ind <= end:
        if nums[l_ind] < nums[r_ind]:
            sorted_list.append(nums[l_ind])
            l_ind += 1
        else:
            sorted_list.append(nums[r_ind])
            r_ind += 1

    while l_ind <= mid:
        sorted_list.append(nums[l_ind])
        l_ind += 1

    while r_ind <= end:
        sorted_list.append(nums[r_ind])
        r_ind += 1

    for i, sorted_val in enumerate(sorted_list):
        nums[start + i] = sorted_val
        yield nums


if __name__ == "__main__":
    # Verify it works
    random_list_of_nums = [1,4,77,2,344,12,35,345,8,12,356,2]
    random_list_of_nums = merge_sort(random_list_of_nums, 0, len(random_list_of_nums)- 1)
    print(random_list_of_nums)