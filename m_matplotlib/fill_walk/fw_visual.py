from typing import Any

from m_matplotlib.pls_base import PLSBase


class FWVisual(PLSBase):
    def __init__(self, type_style: int, axis_visible: bool = True) -> None:
        super().__init__(type_style)

        self.axis_visible: bool = axis_visible

    def plt_style_fonts(self) -> None:
        self.ax.set_title('Fill Walk', fontsize=24)
        self.ax.set_xlabel('X Value', fontsize=14)
        self.ax.set_ylabel('Y Value', fontsize=14)

        self.ax.tick_params(axis='both', labelsize=14)

    def plt_create(self, one_data: Any, two_data: Any, s: int = 3, c: Any = None) -> None:
        super().plt_create(one_data, two_data)

        self.ax.scatter(one_data, two_data, s, c, cmap=self.plt.cm.Blues, edgecolors='none')
        self.ax.scatter(one_data[0], two_data[0], s=15, c='green', edgecolors='none')
        self.ax.scatter(one_data[-1], two_data[-1], s=15, c='red', edgecolors='none')

        if not self.axis_visible:
            self.ax.get_xaxis().set_visible(self.axis_visible)
            self.ax.get_yaxis().set_visible(self.axis_visible)
