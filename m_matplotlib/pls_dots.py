from typing import List, Any

from pls_fonts import PLSFonts


class PLSDots(PLSFonts):
    def __init__(self, type_style: int) -> None:
        super().__init__(type_style)
        self.plt_cmap = self.plt.cm

    def plt_create(self, one_data: Any, two_data: Any, s: int = 5, c='black') -> None:
        self.fig, self.ax = self.plt.subplots()
        self.ax.scatter(one_data, two_data, s, c, cmap=self.plt.cm.Blues)

    def plt_xy_range(self, xy_pos: List) -> None:
        self.ax.axis(xy_pos)
