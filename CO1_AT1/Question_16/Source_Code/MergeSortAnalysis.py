def merge(arr, left, mid, right):
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1


def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)

        merge(arr, left, mid, right)


def main():
    arr = [45, 12, 67, 23, 89, 10, 5]

    print("Original Array:")
    print(arr)

    merge_sort(arr, 0, len(arr) - 1)

    print("\nSorted Array:")
    print(arr)

    print("\nComplexity Analysis")
    print("-------------------")
    print("Best Case    : O(n log n)")
    print("Average Case : O(n log n)")
    print("Worst Case   : O(n log n)")
    print("Space Complexity : O(n)")


if __name__ == "__main__":
    main()