# 82135524

def broken_search(nums: list, target: int) -> int:
    start_idx = 0
    end_idx = len(nums) - 1
    while start_idx <= end_idx:
        mid_idx = (start_idx + end_idx) // 2
        if nums[mid_idx] == target:
            return mid_idx
        elif nums[start_idx] <= nums[mid_idx]:
            if nums[start_idx] <= target < nums[mid_idx]:
                end_idx = mid_idx - 1
            else:
                start_idx = mid_idx + 1
        else:
            if nums[mid_idx] < target <= nums[end_idx]:
                start_idx = mid_idx + 1
            else:
                end_idx = mid_idx - 1
    return -1


if __name__ == '__main__':
    count_array = int(input())
    target_number = int(input())
    numbers_array = [int(num) for num in input().split()]

    print(broken_search(numbers_array, target_number))