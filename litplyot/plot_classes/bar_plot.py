import matplotlib.pyplot as plt

from .base_plot import BasePlotClass


class BarPlot(BasePlotClass):
    def __init__(self, data):
        super().__init__()
        self.data = data

    def plot(self, x, y):
        plt.figure(figsize=(10, 6))
        plt.bar(self.data[x], self.data[y])
        plt.xlabel(x)
        plt.ylabel(y)
        plt.title('Bar Plot')
        plt.show()