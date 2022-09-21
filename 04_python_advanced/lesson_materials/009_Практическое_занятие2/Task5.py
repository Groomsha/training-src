from bs4 import BeautifulSoup
import requests as r


responce = r.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%"
                 "82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")

soup = BeautifulSoup(responce.text, "lxml")
print(soup.title, "\n")
print(soup.title.name, "\n")
print(soup.title.text, "\n")
print(soup.title.parent, "\n")

print(soup.prettify(), "\n")
print(soup.find("li", id="footer-poweredbyico"))
# <li id="footer-poweredbyico">

search_tags = soup.find_all(["ul", "li"])
for elem in search_tags:
    print(" ".join(elem.text.split()))
