
class LocalStorage:
    def __init__(self, driver):
        self.__driver = driver

    def add_local_storage(self, name, value):
        self.__driver.execute_script(f"window.localStorage['{str(name)}'] = '{str(value)}'")

    def get_local_storage(self, name):
        self.__driver.execute_script(f"return window.localStorage['{name}']")

    def get_all_storage(self):
        self.__driver.execute_script("return window.localStorage")




