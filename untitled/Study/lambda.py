import requests
import re

a = input()
b = input()
res_a = requests.get(a).text
pattern = "<a href=\"[\w]\">"
print(pattern)
search_b = re.search(pattern, res_a)
if search_b:
    print("No")
else:
    print("Yes")

from bs4 import BeautifulSoup
soup = BeautifulSoup(res_a, 'html.parser')

print(soup.prettify())