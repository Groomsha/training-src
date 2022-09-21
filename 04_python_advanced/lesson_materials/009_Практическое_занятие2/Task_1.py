from bs4 import BeautifulSoup

result = ""

with open("test.html", "r", encoding="UTF-8") as f:
    data = f.read()
    soup = BeautifulSoup(data, 'lxml')
    print(soup.html, "\n")
    print(soup.head, "\n")
    print(soup.body, "\n")
    print(soup.p, "\n")
    print(soup.li, "\n")
    print(soup.table, "\n")
    print(soup.title, "\n")
    result = soup.tr
    print(result)




