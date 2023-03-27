def bubble_sort(our_array):
    for i, _ in enumerate(our_array):
        for j, _ in enumerate(our_array):
            if our_array[i] < our_array[j]:
                our_array[i], our_array[j] = our_array[j], our_array[i]
    return our_array


if __name__ == '__main__':
    result = bubble_sort([2, 4, 2, 5, 6, 7, 4, 2, 1, 45, 6, 7])
    print(result)
