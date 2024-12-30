def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_value = arr[i]

        j = i - 1
        
        while j >= 0 and arr[j] > current_value:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insert the current value into its proper position
        arr[j + 1] = current_value

# Example usage
import random
array = [random.randint(1, 100) for _ in range(10)]
print("Original array:", array)
insertion_sort(array)
print("Sorted array:", array)