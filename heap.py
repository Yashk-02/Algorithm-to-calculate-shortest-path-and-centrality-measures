class Heap:
    def __init__(self):
        self.elements = []
        self.size = len(self.elements)

    def insert(self, n):
        self.elements.append(n)
        self.size += 1
        self.siftup(self.size - 1)
    # n is a list containing two elements, first is the distance from , second is the root

    def popmin(self):
        min = self.elements[0]
        self.elements[0] = self.elements[-1]
        self.size -= 1
        del self.elements[-1]
        self.siftdown(0)
        return min
    # pop out the min node and reconstruct the heap

    def swap(self, index1, index2):
        self.elements[index1], self.elements[index2] = self.elements[index2], self.elements[index1]
        
    def siftup(self, index):
        parent = (index - 1) // 2
        if parent >= 0 and self.elements[parent][1] > self.elements[index][1]:
            self.swap(index, parent)
            self.siftup(parent)

    def siftdown(self, index):
        child = index * 2 + 1
        if child == self.size - 1 and self.elements[child][1] < self.elements[index][1]:
            self.swap(index, child)
            self.siftdown(child)
        elif child < self.size - 1:
            if self.elements[child][1] > self.elements[child + 1][1]:
                self.swap(child, child + 1)
            if self.elements[child + 1][1] < self.elements[index][1]:
                self.swap(index, child + 1)
                self.siftdown(child + 1)
            elif self.elements[child][1] < self.elements[index][1]:
                self.swap(index, child)
                self.siftdown(child)

if __name__ == "__main__":
    pass