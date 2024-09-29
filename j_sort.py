def lowest_to_highest(array):
    swaps = 0
    iterations = 0
    while (1):
        swapped = False
        for i in range(len(array)-1):
            iterations += 1
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                swapped = True
                swaps+=1
        if not swapped:
            print(swaps)
            print(iterations)
            return array


print(lowest_to_highest([10,5,4,2,32,43,6,77,12,67,87,123,44,55,6,4,6,4,3,2,1,98,44,12,52]))