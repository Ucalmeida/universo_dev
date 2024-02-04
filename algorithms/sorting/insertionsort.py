class InsertionSort:
    def __init__(self, array):
        self.array = array

    def insertion_sort(self):
        for i in range(1, len(self.array)):
            j = i
            while self.array[j - 1] > self.array[j] and j > 0:
                self.array[j - 1], self.array[j] = self.array[j], self.array[j - 1]
                j -= 1


array_test = [5, 3, 4, 8, 12, 1, 7]
ordered = InsertionSort(array_test)
ordered.insertion_sort()
print(ordered.array)
