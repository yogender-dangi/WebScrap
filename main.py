#Created by Yogender Dangi
from bs4 import BeautifulSoup
import requests
import time

def find_books():
    html_text = requests.get('https://books.toscrape.com/').text

    soup = BeautifulSoup(html_text, 'lxml')
    books = soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')
    for index, book in enumerate(books):
        price = book.find('p', class_='price_color').text.replace('Â', '').replace('£', '')
        book_name = book.find_all('a')
        if price < '30':
            with open(f'books/{index}.txt', 'w') as f:
                for name in book_name:
                    name = name.text.replace(' ', '')
                    f.write(f"Book Name:{name.strip()}\n")
                link = book.article.h3.a['href']
                f.write(f"Price:{price.strip()}\n")
                f.write(f"Link for more info:https://books.toscrape.com/{link}")
            print(f"File Saved:{index}")
        
if __name__ == '__main__':
    while True:
        find_books()
        time_wait = 1000
        print(f"Waiting for {time_wait} seconds")
        time.sleep(time_wait)


with open('page.html', 'r') as html_file:
    content = html_file.read()
    print(content)

soup = BeautifulSoup(content, 'lxml')
courses_html_tags = soup.find_all('h5')
print(courses_html_tags)
for course in courses_html_tags:
    print(course.text)
course_cards = soup.find_all('div', class_="card")
for course in course_cards:
    courses_names = course.h5.text
    courses_price = course.a.text.split()[-1]
    print(courses_names)
    print(courses_price)
    print(f"{courses_names} costs {courses_price}")