from typing import Any

from pls_base import PLSBase


class PLSFonts(PLSBase):
    def __init__(self) -> None:
        super().__init__()

    def plt_create(self, in_val: Any, data: Any) -> None:
        super().plt_create(in_val, data)

        self.ax.plot(in_val, data, linewidth=3)             # Товщина лінії графіка

        self.ax.set_title('Square Numbers', fontsize=24)    # Назва графіка
        self.ax.set_xlabel('Value', fontsize=14)            # Назва осі Х
        self.ax.set_ylabel('Square of Value', fontsize=14)  # Назва осі Y

        self.ax.tick_params(axis='both', labelsize=14)      # Шрифт та розмір графіка
