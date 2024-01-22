def find_first_last_occurrences(arr, x):
    def binary_search_first(arr, x):
        low, high, result = 0, len(arr) - 1, -1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == x:
                result = mid
                high = mid - 1
            elif arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1

        return result

    def binary_search_last(arr, x):
        low, high, result = 0, len(arr) - 1, -1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == x:
                result = mid
                low = mid + 1
            elif arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1

        return result

    first_occurrence = binary_search_first(arr, x)
    last_occurrence = binary_search_last(arr, x)

    return first_occurrence, last_occurrence

# Example usage:
n = 9
x = 5
arr = [ 1, 3, 5, 5, 5, 5, 67, 123, 125 ]
result = find_first_last_occurrences(arr, x)
print("First occurrence:", result[0])
print("Last occurrence:", result[1])
