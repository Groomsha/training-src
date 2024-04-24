from typing import List, Any

import matplotlib.pyplot as plt


class PLSBase:
    def __init__(self) -> None:
        self.in_values: List = [1, 2, 3, 4, 5]
        self.squares: List = [1, 4, 9, 16, 25]

        self.fig = None
        self.ax = None

    def plt_create(self, in_val: Any, data: Any) -> None:
        self.fig, self.ax = plt.subplots()
        self.ax.plot(in_val, data)

    @staticmethod
    def plt_show():
        plt.show()
