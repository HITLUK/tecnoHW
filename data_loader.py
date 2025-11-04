import requests
from bs4 import BeautifulSoup

def get_currency_rates():
    url = 'https://www.cbr.ru/currency_base/daily/'
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', {'class': 'data'})
    rates = {}
    print(table.find_all('td'))
    for row in table.find_all('tr')[1:]:
        cells = row.find_all('td')
        code = cells[1].text.strip()
        name = cells[3].text.strip()
        nominal = int(cells[2].text.strip())
        value = float(cells[4].text.replace(',', '.').strip())
        rates[code] = {"name": name, "nominal": nominal, "value": value}

    rates['RUB'] = {"name": "Российский рубль", "nominal": 1, "value": 1.0}
    return rates