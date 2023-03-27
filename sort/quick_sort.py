def quick_sort(our_array):
    if len(our_array) <= 1:
        return our_array
    else:
        pivot = our_array.pop()

    items_greater = []
    items_lower = []

    for item in our_array:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


if __name__ == '__main__':
    result = quick_sort([2, 4, 2, 5, 6, 7, 4, 2, 1, 45, 6, 7])
    print(result)
