from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from .base_page import BasePage



class Dashboard(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.__search_input_field = "//input[@name='search_term' and @placeholder='Введите запрос']"
        self.__search_button = "//div[@class='bgl-search__item-button']/button"
        self.__product_name = "//div[@class='ek-grid__item ek-grid__item_width_1-1']/h1[text()]"
        self.__product_picture = '//picture/img[@data-qaid="main-image"]'

    def choose_category(self, name_category: str) -> None:
        self._click((By.XPATH, f"//li[@class='ek-grid__item']/a[@data-analytics-action='click_sidebar_category' \
         and  @data-analytics-label and contains(text(), '{name_category}')]"))

    def choose_subcategory(self, name_subcategory: str):
        self._click((By.XPATH, f"//div[@class='bgl-category-list__title-container']/p[contains(text(), '{name_subcategory}')]"))

    def get_product(self, product_index: int):
        self._click((By.XPATH,  f"(//div[@class='bgl-product__body']/div[@class='ek-box ek-box_margin-bottom_m'])[{product_index}]"))


    def product_search(self, text: str):
        self._input_field((By.XPATH, self.__search_input_field), text)
        self._click((By.XPATH, self.__search_button))


    def scrolle_to_product(self, product_index: int):
        self._scroll_page((By.XPATH, f"(//div[@class='bgl-product__body']/div[@class='ek-box ek-box_margin-bottom_m'])[{product_index}]"))


    def display_product_picture(self):
        self._is_displayed((By.XPATH, self.__product_picture))







