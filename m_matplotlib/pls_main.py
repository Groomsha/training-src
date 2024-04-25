# Щоб працювало, потрібно PyQT або інши аналоги
from typing import List

from pls_base import PLSBase
from pls_fonts import PLSFonts
from pls_dots import PLSDots


if __name__ == "__main__":
    # plt_src = PLSBase(3)
    # plt_src = PLSFonts(8)
    plt_src = PLSDots(9)

    one_values: List = [1, 2, 3, 4, 5]
    two_values: List = [1, 4, 9, 16, 25]
    tree_vales: List = [2, 4]

    plt_src.plt_style_tables()
    # plt_src.plt_create(one_values, two_values)    # task PLSFonts
    # plt_src.plt_create(one_values, two_values, s=50)  # task PLSDots One

    # task PLSDots Two
    one_values = range(1, 1001)
    two_values = [x**2 for x in one_values]
    xy_range: List = [0, 1100, 0, 1100000]
    # plt_src.plt_create(one_values, two_values, s=3, c='blue')
    plt_src.plt_create(one_values, two_values, s=3, c=two_values)
    plt_src.plt_xy_range(xy_range)

    plt_src.plt_style_fonts()
    plt_src.plt_show()
