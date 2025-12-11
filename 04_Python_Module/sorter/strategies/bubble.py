from .base import SortStrategy

class BubbleSort(SortStrategy):
    def sort(self, data):
        length = len(data)
        for i in range(length):
            is_ordered = True
            for j in range(length - i  - 1):
                if data[j] > data[j+1]:
                    is_ordered = False
                    temp = data[j]
                    data[j] = data[j+1]
                    data[j+1] = temp
            if is_ordered:
                break

        return data
