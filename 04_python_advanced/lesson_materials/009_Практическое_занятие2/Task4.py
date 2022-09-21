from bs4 import BeautifulSoup

with open("test2.html", "r", encoding="UTF-8") as f:
    data = f.read()

    soup = BeautifulSoup(data, "lxml")

    for child in soup.recursiveChildGenerator():
        if child.name:
            print(child.name)

    print()
    root = soup.html
    root_childs = [elem.name for elem in root.children if elem.name is not None]
    print(root_childs)

    root = soup.body
    root_childs = [elem.name for elem in root.children if elem.name is not None]
    print(root_childs)

    root_childs = [elem.name for elem in root.descendants if elem.name is not None]
    print(root_childs)
