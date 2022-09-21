from bs4 import BeautifulSoup

with open("test2.html", "r", encoding="UTF-8") as f:
    data = f.read()
    soup = BeautifulSoup(data, "lxml")

    print(soup.h1)
    print(soup.h2)
    print(soup.h3)
    print(soup.h4)
    print(soup.h5)
    print(soup.h6)
    print(soup.head)
    print(soup.title)
    print(soup.table)

