import requests
from bs4 import BeautifulSoup


def get_dw_pretext():
    response = requests.get('https://habr.com/ru/all')
    soup = BeautifulSoup(response.text, 'html.parser')
    DESIRED_WORDS = ['компьютер', 'игры', 'бизнес', 'момент']
    posts = soup.find_all('article', class_='post')  # нашли все посты
    for post in posts:
        post_texts = post.find_all('div', class_="post__text") # нашли все тексты постов
        post_text = list(map(lambda x: x.text.strip().lower(), post_texts))
        for texts in post_text:
            if any(dw in texts for dw in DESIRED_WORDS):
                date_time = post.find('span', class_='post__time').text.strip()
                link = post.find('a', class_="post__title_link")  # ссылка на пост,берём информацию из постов, а не из текста поста
                link_link = link.attrs.get('href')  # берём информацию уже из линка
                link_name = link.text  # берём информацию уже из линка
                print(date_time, link_name, link_link)
                break


def get_dw_in_text():
    response = requests.get('https://habr.com/ru/all')
    soup = BeautifulSoup(response.text, 'html.parser')
    DESIRED_WORDS = ['игры', 'бизнес', 'процесс']
    posts = soup.find_all('article', class_='post')  # нашли все посты
    for post in posts:
        link = post.find('a', class_="post__title_link")
        link_URL = link.attrs.get('href')
        link_name = link.text
        response2 = requests.get(link_URL)
        soup1 = BeautifulSoup(response2.text, 'html.parser')
        post_text = soup1.find('div', class_="post__text").text
        if any(dw in post_text for dw in DESIRED_WORDS):
            date_time = post.find('span', class_='post__time').text.strip()
            print(date_time, link_name, link_URL)


if __name__ == '__main__':
    get_dw_in_text()
    get_dw_pretext()
