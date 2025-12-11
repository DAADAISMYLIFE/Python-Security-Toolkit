from .base import SortStrategy

class QuickSort(SortStrategy):
    def sort(self, data):
        return sorted(data)
