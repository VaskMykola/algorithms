def binary_search(our_array, item):
    """
    basic binary search algorithm.

    :param our_array: sorter in not decreasing order list of items to search
    :param item: item to search for
    :return: index of item if found, else -1
    """
    low = 0
    high = len(our_array) - 1

    while low <= high:
        mid = (low + high) >> 1  # bit shift to divide by 2, it's faster and prevents from overflow
        guess = our_array[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return -1


if __name__ == '__main__':
    result = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7)
    print(result)
