import heapq


class MedianOfAStream:
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
    
    def insert_num(self, num):
        if not self.maxHeap or num <= -self.maxHeap[0]:
            # to create maxHeap we need to change the sign
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHimport heapq


class MedianOfAStream:
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
    
    def insert_num(self, num):
        if not self.maxHeap or num <= -self.maxHeap[0]:
            # to create maxHeap we need to change the sign
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)

        # either both the heap will have equal number of elements
        # or maxHeap will have one more number than minHeap
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heapq.heappush(
                self.minHeap,
                -heapq.heappop(self.maxHeap),

            )
        elif len(self.maxHeap) < len(self.minHeap):
            heapq.heappush(
                self.maxHeap,
                -heapq.heappop(self.minHeap),

            )
        print(self.maxHeap, self.minHeap)
        return -1
    
    def find_median(self):

        if len(self.minHeap) == len(self.maxHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        else:
            return -self.maxHeap[0]


def main():
    medianOfAStream = MedianOfAStream()
    medianOfAStream.insert_num(3)
    medianOfAStream.insert_num(1)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(5)

    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(4)
    medianOfAStream.insert_num(4)
    print("The median is: " + str(medianOfAStream.find_median()))


main()
eap, num)

        # either both the heap will have equal number of elements
        # or maxHeap will have one more number than minHeap
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heapq.heappush(
                self.minHeap,
                -heapq.heappop(self.maxHeap),

            )
        elif len(self.maxHeap) < len(self.minHeap):
            heapq.heappush(
                self.maxHeap,
                -heapq.heappop(self.minHeap),

            )
        print(self.maxHeap, self.minHeap)
        return -1
    
    def find_median(self):

        if len(self.minHeap) == len(self.maxHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        else:
            return -self.maxHeap[0]


def main():
    medianOfAStream = MedianOfAStream()
    medianOfAStream.insert_num(3)
    medianOfAStream.insert_num(1)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(5)

    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(4)
    medianOfAStream.insert_num(4)
    print("The median is: " + str(medianOfAStream.find_median()))


main()
