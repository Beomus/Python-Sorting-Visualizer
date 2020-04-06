# There are different ways to do a Quick Sort partition, this implements the
# Hoare partition scheme. Tony Hoare also created the Quick Sort algorithm.
def partition(nums, low, high):
    # We select the middle element to be the pivot. Some implementations select
    # the first element or the last element. Sometimes the median value becomes
    # the pivot, or a random one. There are many more strategies that can be
    # chosen or created.
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # If an element at i (on the left of the pivot) is larger than the
        # element at j (on right right of the pivot), then swap them
        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums):
    # Create a helper function that will be called recursively
    def _quick_sort(items, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = partition(items, low, high)
            yield from _quick_sort(items, low, split_index)
            yield from _quick_sort(items, split_index + 1, high)

    yield from _quick_sort(nums, 0, len(nums) - 1)
    yield nums


def swap(A, i, j):
    """Helper function to swap elements i and j of list A."""

    if i != j:
        A[i], A[j] = A[j], A[i]

def quicksort(nums, start, end):
    if start >= end:
        return

    pivot = nums[end]
    pivot_index = start

    for i in range(start, end):
        if nums[i] < pivot:
            nums[i], nums[pivot_index] = nums[pivot_index], nums[i]
            pivot_index += 1
        yield nums
    nums[end], nums[pivot_index] = nums[pivot_index], nums[end]
    yield nums

    yield from quicksort(nums, start, pivot_index - 1)
    yield from quicksort(nums, pivot_index + 1, end)




if __name__ == "__main__":
    # Verify it works
    random_list_of_nums = [22, 5, 1, 18, 99]
    quick_sort(random_list_of_nums)
    print(random_list_of_nums)