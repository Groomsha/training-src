# Щоб працювало, потрібно PyQT або інши аналоги
from typing import List

from pls_base import PLSBase
from pls_fonts import PLSFonts
from pls_dots import PLSDots


if __name__ == "__main__":
    # plt_src = PLSBase()
    # plt_src = PLSFonts(8)
    plt_src = PLSDots(4)

    one_values: List = [1, 2, 3, 4, 5]
    two_values: List = [1, 4, 9, 16, 25]
    tree_vales: List = [2, 4]

    # plt_src.plt_create(one_values, two_values)
    plt_src.plt_create(one_values, two_values, s=50)

    plt_src.plt_style()
    plt_src.plt_show()
