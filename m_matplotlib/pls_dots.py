from typing import Any

from pls_fonts import PLSFonts


class PLSDots(PLSFonts):
    def __init__(self, type_style: int) -> None:
        super().__init__(type_style)

    def plt_create(self, one_data: Any, two_data: Any, s: int = None) -> None:
        self.fig, self.ax = self.plt.subplots()
        self.ax.scatter(one_data, two_data, s)
