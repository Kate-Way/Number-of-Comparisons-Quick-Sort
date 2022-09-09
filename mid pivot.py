from numpy import loadtxt

# load your txt file
arr = loadtxt('QuickSort.txt', dtype='int')
# To test code on smaller sample of 4 units from the file or an array
# arr = the_arr[:4]
# print(arr)
# arr = [1408, 9058, 7742, 3153, 624, 609, 7628, 5469, 17, 5004]


def median_of_three(array, left, right):
    middle = left + (right - left)//2
    if array[right] < array[left] < array[middle] or array[middle] < array[left] < array[right]:
        return left
    elif array[right] < array[middle] < array[left] or array[left] < array[middle] < array[right]:
        return middle
    else:
        return right


# median of three pivot
def partition(array, left, right, comparisons):
    if left != right:
        x = median_of_three(array, left, right)
        array[left], array[x] = array[x], array[left]
        pivot = left
        i = left + 1   # pointer
        for j in range(i, len(array)):
            if array[j] < array[pivot]:
                array[j], array[i] = array[i], array[j]  # swap items
                i += 1
        array[left], array[i-1] = array[i-1], array[left]  # put pivot into position
        comparisons += right - left
        return i - 1, comparisons


def qs(arr, left, right, comparisons):
    if left >= right:
        return comparisons
    p, comparisons = partition(arr, left, right, comparisons)
    comparisons = qs(arr, left, p - 1, comparisons)
    comparisons = qs(arr, p + 1, right, comparisons)
    return comparisons


print(qs(arr, 0, len(arr)-1, 0))
