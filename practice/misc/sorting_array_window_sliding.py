

from typing import List

import heapq
def sort_array(arr:List[int], k:int) -> List[int]:

    output = []

    heap = []

    for i,n in enumerate(arr):

        heapq.heappush(heap,n)
        if i>k-1:
            output.append(heapq.heappop(heap))

    while heap:
        output.append(heapq.heappop(heap))
    
    return output

sort_array([2,3,1,5,4,6],5)
sort_array([10, 9, 8, 7, 4, 70, 60, 50],4)


def insertionSort(A, size):
    i, key, j = 0, 0, 0
    for i in range(size):
        key = A[i]
        j = i-1
 
        # Move elements of A[0..i-1], that are
        # greater than key, to one position
        # ahead of their current position.
        # This loop will run at most k times
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = key
    return A

insertionSort([10, 9, 8, 7, 4, 70, 60, 50],4)


