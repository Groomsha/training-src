from typing import List

import matplotlib.pyplot as plt


class PLSBase:
    def __init__(self) -> None:
        self.squares: List = [1, 4, 9, 16, 25]

    def plt_show(self) -> None:
        fig, ax = plt.subplots()
        ax.plot(self.squares)

        plt.show()


if __name__ == "__main__":
    plt_src = PLSBase()
    plt_src.plt_show()
