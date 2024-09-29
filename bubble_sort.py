def bubble_sort(array):
    swapped = True
    array_adj = array[:]
    while swapped:
        for i in range(len(array_adj)-1):
            while (array_adj[i] > array_adj[i+1]): 
                array_adj[i], array_adj[i+1] = array_adj[i+1], array_adj[i]
        if array == array_adj:
            swapped = False
        else:
            array = array_adj[:]
    return array