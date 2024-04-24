from typing import List, Any

from pls_base import PLSBase


class PLSFonts(PLSBase):
    def __init__(self, type_style: int) -> None:
        """Значення 'type_style' допустиме від 0 до 11"""
        self.type_style = type_style

        super().__init__()

    def plt_style(self) -> None:
        self.ax.set_title('Square Numbers', fontsize=24)  # Назва графіка
        self.ax.set_xlabel('Value', fontsize=14)  # Назва осі Х
        self.ax.set_ylabel('Square of Value', fontsize=14)  # Назва осі Y

        self.ax.tick_params(axis='both', labelsize=14)  # Шрифт та розмір графіка

    def plt_create(self, one_data: Any, two_data: Any) -> None:
        self.plt.style.use(self.plt.style.available[self.type_style])

        self.fig, self.ax = self.plt.subplots()
        self.ax.plot(one_data, two_data, linewidth=3)  # Товщина лінії графіка
