class maxHeap:
    # start algo with node ata lowest level of tree and has children nodes
    # continue process up to root and make sure all subtrees are following max-heap property
    def heapify(self, arr, n, i):
        largest = i
        l = 2*i + 1
        r = 2*i + 2

        # find largest of root, left, right, if not root, swap largest with root
        if l < n and arr[i] < arr[l]:
            largest = l
        if r < n and arr[largest] < arr[r]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)
    def insert(self, arr, newNum):
        size = len(array)
        if size == 0:
            array.append(newNum)
        else:
            array.append(newNum)
            for i in range((size//2)-1, -1, -1):
                heapify(array, size, i)
    def deleteNode(array, num):
        size = len(array)
        i = 0
        # find node to delete
        for i in range(0, size):
            if num == array[i]:
                break
        array[i], array[size-1] = array[size-1], array[i] # swap with last leaf node
        for i in range((size//2)-1, -1, -1):
            heapify(array, size, i)