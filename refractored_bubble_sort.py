def bubble_sort(array):
    while(1):
        swapped = False
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                swapped = True
        if not swapped:
            return array
        
print(bubble_sort([1,2,7,4,3,2,2,89,664,3,3,55,6,777,4,3,5]))