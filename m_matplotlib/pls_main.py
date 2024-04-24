# Щоб працювало, потрібно PyQT або інши аналоги

from pls_base import PLSBase


if __name__ == "__main__":
    plt_src = PLSBase()
    plt_src.plt_create(plt_src.squares)

    plt_src.plt_show()
