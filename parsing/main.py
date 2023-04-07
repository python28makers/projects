from bs4 import BeautifulSoup
# тип данных для работы с тегами в HTML

with open('index.html', 'r') as html:
    html_code = html.read()
    soup = BeautifulSoup(html_code, 'html.parser')
    t1 = soup.find('p').text
    # print(t1)
    div_span = soup.find('div', class_='div1').find('span').text
    # print(div_span)
    link = soup.find('img').get('src')
    # print(link)
    site = soup.find('a').get('href')
    # print(site)
