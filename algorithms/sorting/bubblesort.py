class BubbleSort:
    def __init__(self, array):
        self.array = array

    def bubblesort(self):
        n = len(self.array)
        for i in range(n - 1):
            swapped = False
            for j in range(n - i - 1):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    swapped = True

            if not swapped:
                return self.array


array_test = [5, 3, 4, 8, 12, 1, 7]
chamada = BubbleSort(array_test)
print(chamada.bubblesort())
