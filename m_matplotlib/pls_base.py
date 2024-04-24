from typing import List, Any

import matplotlib.pyplot as plt


class PLSBase:
    def __init__(self) -> None:
        self.squares: List = [1, 4, 9, 16, 25]

    @staticmethod
    def plt_create(data: Any) -> None:
        fig, ax = plt.subplots()
        ax.plot(data)

    @staticmethod
    def plt_show():
        plt.show()
