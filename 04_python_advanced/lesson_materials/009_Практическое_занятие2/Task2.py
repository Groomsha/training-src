from bs4 import BeautifulSoup
import re

result = ''
with open("test2.html", "r", encoding="UTF-8") as f:
    data = f.read()
    soup = BeautifulSoup(data, "lxml")

    # print("html: {}, \nname: {}, \ntext: {}".format(soup.html, soup.name, soup.text))
    result = soup.text
    print(type(result))

print(result)

phone_numbers = re.findall(r"\d{3}-\d{3}-\d{2}-\d{2}", result)
print("Phone numbers are:", phone_numbers)

emails = re.findall(r"-\d{2}(\w+@\w+\.\w+)", result)
print("emails are:", emails)
