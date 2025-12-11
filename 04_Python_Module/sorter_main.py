from sorter.sorter import Sorter
from sorter.strategies.quick import QuickSort
from sorter.strategies.bubble import BubbleSort

data = [3,2,1,5,6,4]

qs = Sorter(QuickSort())
bs = Sorter(BubbleSort())

print(qs.run(data))
print(bs.run(data))
