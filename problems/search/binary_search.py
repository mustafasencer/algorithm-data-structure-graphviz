def binary_search(array, start_index, end_index, value):
    while start_index <= end_index:
        mid = start_index + (end_index - start_index)

        if array[mid] == value:
            return mid

        if array[mid] < value:
            start_index = mid + 1

        else:
            end_index = mid - 1

    return -1


if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40, 50, 60]
    x = 50

    result = binary_search(arr, 0, len(arr) - 1, x)

    assert result == -1
