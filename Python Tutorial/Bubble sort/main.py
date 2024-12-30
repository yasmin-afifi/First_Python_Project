import random
def bubble_sort(arr):
        for iteration in range(len(arr)):
            for (step) in range(len(arr)-iteration -1):
                if arr[step] > arr[step+1]:
                    arr[step],arr[step+1] = arr[step+1],arr[step] 
                    

        return arr



my_list = [random.randint(1,20) for item in range(10)]
print(my_list)

my_list = bubble_sort(my_list)
print(my_list)