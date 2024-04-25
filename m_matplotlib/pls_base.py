from typing import Any

import matplotlib.pyplot


class PLSBase:
    def __init__(self, type_style: int) -> None:
        self.plt = matplotlib.pyplot
        self.type_style = type_style
        self.fig = None
        self.ax = None

    def plt_create(self, one_data: Any, two_data: Any) -> None:
        self.fig, self.ax = self.plt.subplots()
        # self.ax.plot(one_data, two_data)      # or
        # self.ax.scatter(one_data, two_data)   # or

    def plt_style_tables(self) -> None:
        self.plt.style.use(self.plt.style.available[self.type_style])

    def plt_show(self):
        self.plt.show()
