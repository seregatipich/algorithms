def find_min_index(arr):
    n = len(arr)
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < arr[(mid + 1) % n] and arr[mid] < arr[(mid - 1 + n) % n]:
            return mid
        elif arr[mid] < arr[high]:
            high = mid - 1
        else:
            low = mid + 1

    return -1


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def main(arr, target):
    n = len(arr)
    min_index = find_min_index(arr)

    if target >= arr[min_index] and target <= arr[n - 1]:
        return binary_search(arr[min_index:], target)
    else:
        return binary_search(arr[:min_index], target)


if __name__ == '__main__':
    main()
