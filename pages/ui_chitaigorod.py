from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import UI_URL


class ChitaiGorodUI:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(4)

    def open_main_page(self):
        """
           Зайти на сайт
        """
        self.driver.get(UI_URL)

    def close_popups(self):
        """Закрыть всплывающие окна (если есть)"""
        for selector in [
            ".chg-app-button--block.chg-app-button--primary",
            ".popmechanic-close[data-popmechanic-close]",
            ".agreement-notice__button"
        ]:
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, selector))).click()
            except:
                pass

    def get_page_text(self):
        """
           Получить заголовок страницы
        """
        return self.driver.title

    def logo(self):
        """
        Логотип сайта
        """
        logo = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".header__logo"))
        )
        return logo.is_displayed()

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

    def search_product(self, search_phrase):

        input_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='search']"))
        )

        input_field.clear()
        input_field.send_keys(search_phrase)
        input_field.send_keys(Keys.ENTER)

        self.driver.find_element(
            By.CSS_SELECTOR, "svg.search-form__icon-search"
        ).click()

    def add_product(self, num):

        buy_buttons = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//button[contains(., 'Купить')]")
            )
        )

        buttons_to_click = min(max(num, 1), 10)
        clicked = 0

        for i in range(buttons_to_click):
            button = buy_buttons[i]
            self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(button))
            self.driver.execute_script("arguments[0].click();", button)
            clicked += 1

        self.driver.execute_script("window.scrollTo(0, 0);")

        return clicked

    def click_basket(self):
        basket = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Корзина']"))
            )

        basket.click()
        self.driver.execute_script("window.scrollTo(0, 0);")

    def get_report(self):
        """
           Количество товара в корзине
        """
        txt = self.driver.find_element(
            By.CSS_SELECTOR, ".cart-page__title--append").text
        count_text = txt.split()[0]
        return int(count_text)

    def empty_the_basket(self):
        """
        Очистить корзину
        """
        clear_element = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, ".cart-page__clear-cart-title")))
        clear_element.click()

    def get_empty_basket_message(self):
        """
        Получить сообщение очищенной корзины
        """
        return WebDriverWait(self.driver, 15).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".cart-multiple-delete__title"),
                "Корзина очищена"
            ))

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
        return txt

    def close_browser(self):
        """
           Закрыть браузер
        """
        self.driver.quit()
