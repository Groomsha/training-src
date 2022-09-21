from bs4 import BeautifulSoup
import re

result = ""
with open("test.html", "r", encoding="UTF-8") as f:
    data = f.read()

    soup = BeautifulSoup(data, 'lxml')

    # print("html: {0}, \n\nname:{1}, \n\ntext:{2}\n\n".format(soup.html, soup.html.name, soup.html.text))

    print(type(soup.html.text))

    result = soup.html.text

print("\nResult is:", result)

phone_numbers = []
phone_numbers += re.findall(r"\d{3}-\d{3}-\d{2}-\d{2}", result)
print("Phone_results is:", phone_numbers)

emails = []
emails += re.findall(r"\d+(\w+@\w+\.\w+)", result)
print("email_results is:", emails)
