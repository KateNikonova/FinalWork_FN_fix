from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import UI_URL


class ChitaiGorodUI:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def open_main_page(self):
        """
           Зайти на сайт
        """
        self.driver.get(UI_URL)

    def click_target_button(self):
        """
           Ожидане кликабельности кнопки Да, я здесь
        """
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, \
                 ".chg-app-button--block.chg-app-button--primary")
            )
        )
        button.click()

    def get_page_text(self):
        """
           Получить заглавие страницы
        """
        return self.driver.title

    def logo(self):
        """
           Логотип сайта
        """
        logo = self.driver.find_element(
            By.CSS_SELECTOR, ".header__logo-link"
            )
        logo.is_displayed()
        return

    def resize_browser(self, width, height):
        """
           Задать размеры экрана
        """
        self.driver.set_window_size(width, height)

    def maximize_browser(self):
        """
           Максимальный размер экрана
        """
        self.driver.maximize_window()

    def search_product(self, name):
        """
           Ввод названия товара
           Нажать на иконку Поиск
        """
        self.driver.find_element(
            By.CSS_SELECTOR, "input[name='search']"
            ).send_keys(name)
        self.driver.find_element(
            By.CSS_SELECTOR, "button[aria-label='Найти']"
            ).click()

    def add_product(self):
        """
           Ожидане кликабельности кнопки Купить
           Кликнуть на кнопку Купить
        """
        buttons = button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR,\
                  ".chg-app-button--brand-blue.product-buttons__main-action")
            )
        )
        for button in buttons:
            button.click()
        #     coun +=1
        #     return coun

    def click_basket(self):
        """
           Зайти в корзину
        """
        self.driver.find_element(
            By.CSS_SELECTOR, ".header-controls__btn[aria-label='Корзина']"
            ).click()

    def get_report(self):
        """
           Количество товара в корзине
        """
        txt = self._driver.find_element(
            By.CSS_SELECTOR, \
                "section.cart-sidebar__info \
                    div.info-item.cart-sidebar__item div.info-item__title"
                ).text
        count_text = txt.split()[0]
        return int(count_text)

    def empty_the_basket(self):
        """
           Очистить корзину
        """
        self.driver.find_element(
            By.CSS_SELECTOR, "span.cart-page__clear-cart-title"
            ).click()

    def button_auth(self):
        """
           Кнопка Входа и Авторизации
        """
        self.driver.find_element(
            By.CSS_SELECTOR, ".header-controls__btn[aria-label='Меню профиля']"
            ).click()

    def get_field_name(self):
        txt = self.driver.find_element(
            By.CSS_SELECTOR, "div.ui-header-modal__title"
            ).text
        return(txt)

    def close_browser(self):
         """
           Закрыть браузер
        """
         self.driver.quit()
