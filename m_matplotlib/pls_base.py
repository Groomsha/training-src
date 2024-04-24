from typing import Any

import matplotlib.pyplot as plt


class PLSBase:
    def __init__(self) -> None:
        self.fig = None
        self.ax = None

    def plt_create(self, one_data: Any, two_data: Any) -> None:
        self.fig, self.ax = plt.subplots()
        self.ax.plot(one_data, two_data)

    @staticmethod
    def plt_show():
        plt.show()
