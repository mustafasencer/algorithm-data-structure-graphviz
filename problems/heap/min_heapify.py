from heapq import heappop, heappush


class MinHeap:
    def __init__(self) -> None:
        self.heap = []

    def parent(self, i):
        return (i - 1) / 2

    def insert_key(self, k) -> None:
        heappush(self.heap, k)

    def decrease_key(self, i, new_val) -> None:
        self.heap[i] = new_val
        while i != 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = (
                self.heap[self.parent(i)],
                self.heap[i],
            )

    def extract_min(self):
        return heappop(self.heap)

    def delete_key(self, i) -> None:
        self.decrease_key(i, float("-inf"))
        self.extract_min()

    def get_min(self):
        return self.heap[0]


if __name__ == "__main__":
    heapObj = MinHeap()
    heapObj.insert_key(3)
    heapObj.insert_key(2)
    heapObj.delete_key(1)
    heapObj.insert_key(15)
    heapObj.insert_key(5)
    heapObj.insert_key(4)
    heapObj.insert_key(45)

    heapObj.extract_min()
    heapObj.get_min()
    heapObj.decrease_key(2, 1)
    heapObj.get_min()
