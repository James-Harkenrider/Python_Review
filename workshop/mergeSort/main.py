def merge_sort(array):
    array_length = int(len(array))
    mid_point = int(array_length / 2)
    array1 = array[0:mid_point]
    array2 = array[mid_point:]
    sorted_array = []
    if array_length > 1:
        array1 = merge_sort(array1)
        array2 = merge_sort(array2)
    else:
        print(f"{array1} {array2}")


array_test = [0, 3, 1, 7, 5, 6, 4, 8]
merge_sort(array_test)

