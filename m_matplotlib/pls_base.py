from typing import Any

import matplotlib.pyplot


class PLSBase:
    def __init__(self) -> None:
        self.plt = matplotlib.pyplot
        self.fig = None
        self.ax = None

    def plt_create(self, one_data: Any, two_data: Any) -> None:
        self.fig, self.ax = self.plt.subplots()
        # self.ax.plot(one_data, two_data)      # or
        # self.ax.scatter(one_data, two_data)   # or

    def plt_show(self):
        self.plt.show()
