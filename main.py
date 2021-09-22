import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

query = input("введите ключевые слова: ")


class TwoGisParser:
    """ Класс по парсингу мест с 2gis """

    def __init__(self, driver, query):
        self.driver = driver
        self.query = query

    def parse(self):  # запускаем, чтобы запустить в работу парсер
        self.go_to_search_page()

    def go_to_search_page(self):
        self.driver.get(f"https://2gis.ru/moscow/search/{self.query}")


def init_driver_Chrome():
    driver = webdriver.Chrome()  # создаем экземпляр драйвера
    """Добавляется функция WebDriverWait в качестве атрибута драйвера, так что доступ к нему станет намного проще. Эта 
    функция используется для того, чтобы дать драйверу подождать 5 секунд, перед следующим действием;"""
    driver.wait = WebDriverWait(driver, 5)
    return driver


""" функция lookup берет два аргумента: драйвер и запрос (строка) 
открывает поисковую страницу Google """

""" затем ждет, пока будет найден элемент окна запроса, а также кнопку для нажатия. 
Мы используем функцию WebDriverWait именно для того, чтобы дождаться появления этих элементов """


def lookup(driver, query):
    driver.get('https://2gis.ru/search/места%20для%20детей')
    # link = driver.find_element_by_class_name('_pbcct4')  # пробуем нажимать на ссылку
    # link.click()
    # title = driver.find_element_by_tag_name('h1')  # получаем текст из тега h1 на странице
    # print(title.text)


if __name__ == "__main__":
    driver_result = init_driver_Chrome()
    lookup(driver_result, query)
    time.sleep(5)
    driver_result.quit()

# url = 'https://minfin.com.ua/currency/nbu/'
# html = 'https://2gis.ru/moscow'
# html = 'https://3dnews.ru/'

# source = requests.get(html)
# print(source)
# main_text = source.text
# soup = BeautifulSoup(main_text)

# html = 'https://2gis.ru/'

# tree = etree.HTML(html)
