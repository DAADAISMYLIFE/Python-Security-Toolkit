class Sorter:
    def __init__(self, strategy):
        self.strategy = strategy

    def run(self, data):
        return self.strategy.sort(data)
