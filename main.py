import requests
from bs4 import BeautifulSoup as Bs
import lxml

# url = 'https://www.bbc.co.uk/sport/horse-racing/uk-ireland/results/2023-02-07'
#
headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0"
}
#
# req = requests.get(url, headers=headers)
# src = req.text
#
# with open(f"index.html", 'w', encoding='utf-8') as file:
#     file.write(src)

# with open(f"index.html", encoding='utf-8') as file:
#     src = file.read()
#
# soup = Bs(src, "lxml")
#
# my_links = soup.find_all(class_='gs-o-table__link')
#
# hrefs = []
# for a in my_links:
#     href = "https://www.bbc.co.uk" + a.get("href")
#     hrefs.append(href)


# reqTable = requests.get(url="https://www.bbc.co.uk/sport/horse-racing/race/EHRP1200381", headers=headers)
# src = reqTable.text
#
# with open(f"table.html", "w", encoding="utf-8") as file:
#     file.write(src)

with open(f"table.html", encoding="utf-8") as file:
    src = file.read()

soup = Bs(src, "lxml")
TableHeads = soup.table.thead(string=True)


print(TableHeads)
