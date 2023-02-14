# 82138186

def broken_search(nums: list, target: int) -> int:
    if len(nums) == 1 and nums[0] != target:
        return -1

    left, right = 0, len(nums) - 1

    while left <= right:
        if nums[left] == target:
            return left

        if nums[right] == target:
            return right

        mid_index = (left + right) // 2
        mid_number = nums[mid_index]

        if mid_number == target:
            return mid_index

        if nums[left] <= mid_number:
            if nums[left] < target < mid_number:
                right = mid_index - 1
            else:
                left = mid_index + 1

        else:
            if mid_number < target < nums[right]:
                left = mid_index + 1
            else:
                right = mid_index - 1
    return -1


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
