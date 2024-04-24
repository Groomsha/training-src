# Щоб працювало, потрібно PyQT або інши аналоги

from pls_base import PLSBase
from pls_fonts import PLSFonts


if __name__ == "__main__":
    # plt_src = PLSBase()
    plt_src = PLSFonts()

    plt_src.plt_create(plt_src.in_values, plt_src.squares)
    plt_src.plt_show()
