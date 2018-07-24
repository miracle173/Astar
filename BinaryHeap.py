class BinaryHeap:
    def __init__(self):
        self._arridx = {}
        self._array = []

    def _swap(self, i, j):
        # swaps to entries of an array
        #and updates the index-dictionary accordingly
        self._arridx[self._array[i][1]] = j
        self._arridx[self._array[j][1]] = i
        self._array[i], self._array[j] = self._array[j], self._array[i]

    def _push(self, item, key):
        # appends an item to the array
        # and updates the index-dictionary accordingly
        self._array.append((
            key,
            item,
        ))
        self._arridx[item] = len(self._array) - 1

    def _pop(self):
        # removes the last element of the array
        # and updates the index-dictionary accordingly
        t = self._array[0]
        del self._arridx[self._array[0][1]]
        return t

    def _replaceFirstByLast(self):
        self._array[0] = self._array.pop()
        self._arridx[self._array[0][1]] = 0
        self._adjustFromLow()

    def _adjustFromLow(self):
        # swaps the first element of the heap array
        # to the right place in the heap
        # and updates the index-dictionary accordingly
        i = 0
        while True:
            j1 = 2 * i + 1
            j2 = j1 + 1
            if j1 >= len(self._array):
                # i< len(a) <= j1 < j2
                return
            elif j2 >= len(self._array):
                # i<  j1=len(a)-1 < j2
                if self._array[i] > self._array[j1]:
                    # a[j1] < a[i]
                    self._swap(i, j1)
                # else: a[i]<=a[j1]: nothing to do
                return
            else:
                # i<j1<j2<=len(a)-1
                if self._array[i] <= self._array[j1]:
                    # a[i]<=a[j1]
                    # j1 must not change
                    if self._array[i] <= self._array[j2]:
                        # a[i]<=a[j2]
                        # j2 must not change
                        return
                    else:
                        # j2 must change
                        self._swap(j2, i)
                        i = j2
                else:
                    # a[i]>a[j1]
                    if self._array[i] > self._array[j2]:
                        # a[i] > a[j2], a[i] > a[j1]
                        # a[i] has to be swapped
                        if self._array[j1] < self._array[j2]:
                            # a[j1] < a[j2] <a[i]
                            self._swap(j1, i)
                            i = j1
                        else:
                            # a[j2] <= a[j1] <a[i]
                            self._swap(j2, i)
                            i = j2
                    else:
                        # a[j2] >= a[i], a[i]>a[j1]
                        self._swap(i, j1)
                        i = j1

    def _adjustFromHigh(self, index=None):
        # takes an element of the heap array
        # that is to small for its current position,
        # swaps it to the right place in the heap
        # and updates the index-dictionary accordingly
        #
        if index is None:
            j = len(self._array) - 1
        else:
            j = index
        i = (j - 1) // 2
        while i >= 0 and self._array[i] > self._array[j]:
            self._swap(i, j)
            j = i
            i = (j - 1) // 2

    def extractMin(self):
        # return the smallest element
        # and remove it from the heap
        t = self._pop()
        if len(self._array) > 1:
            self._replaceFirstByLast()
        else:
            self._array.pop()
        return t

    def insert(self, item, key):
        # insert and item to the heap
        self._push(item, key)
        self._adjustFromHigh()

    def decreaseKey(self, item, key):
        #decrease the key of the iten
        self._array[self._arridx[item]] = (key,item) 
        self._adjustFromHigh(self._arridx[item])

    def containsItem(self, item):
        return item in self._arridx

    def isEmpty(self):
        return not self._array

def testme():
    Z = 1000
    N = 100000
    heap = BinaryHeap()
    for n in range(N):
        z = random.randint(0, Z)
        heap.insert(z, z)
    for n in range(N - 1, -1, 1):
        element = heap._array[n]
        heap.decreaseKey(element[1], *element[0] // 2)
    for n in range(N):
        z = heap.extractMin()


