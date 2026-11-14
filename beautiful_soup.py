import requests
from bs4 import BeautifulSoup

# This is the first aproach to web scrapping
# We retrieve the content of the html of the eltiempo in a string
url = "https://www.eltiempo.es/vigo.html"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")
# print(soup)

# Now with the functions find() or find_all() from BeautifulSoup we are going to find the
# information we want from the html parsed
tag = soup.find("span", class_="c-tib-text degrees")
print(tag)
print(tag["data-temperature"])
print(tag.get("data-temperature"))

# table_tag = soup.find("table", class_="table")
# print(table_tag)
# Now we search for all table heads and find what information have
# Then if there is any data, we use get_text(strip=True) to retrieve clean data without the
# spaces

table_tag = soup.find_all("th", scope="col")
print(table_tag)
for cell in table_tag:
    day = cell.find("span", class_="text-poppins-bold")
    if day is not None:
        day = day.get_text(strip=True)

    date = cell.find("div", class_="datetime")
    if date is not None:
        date = date.get_text(strip=True)

    max_temperature = cell.find("div", class_="max-temperature")
    if max_temperature is not None:
        max_temperature = max_temperature.get_text(strip=True)

    min_temperature = cell.find("div", class_="min-temperature")
    if min_temperature is not None:
        min_temperature = min_temperature.get_text(strip=True)

    print(
        f"Day: {day}, date: {date}, max temperature: {max_temperature}, min temperature: {min_temperature}"
    )
