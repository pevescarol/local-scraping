from bs4 import BeautifulSoup

with open('index.html', 'r') as html_file:
    content = html_file.read()
    #print(content)

    soup = BeautifulSoup(content, 'lxml')
    #print(soup.prettify())

    #tags = soup.find('h5')
    #tags = soup.find_all('h5') #array de los h5
    #print(tags)
    #for tag in tags:
    #    print(tag.text)

    cards = soup.find_all('div', class_='card')
    for c in cards:
        course_name = c.h5.text
        price = c.a.text.split()[-1]
        print(f'{course_name} costs {price}')