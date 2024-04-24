from typing import Any

import matplotlib.pyplot as plt

from pls_fonts import PLSFonts


class PLSDots(PLSFonts):
    def __init__(self, type_style: int) -> None:
        super().__init__(type_style)

    def plt_create(self, one_data: Any, two_data: Any) -> None:
        super().plt_create(one_data, two_data)

        self.ax.scatter(one_data, two_data)
