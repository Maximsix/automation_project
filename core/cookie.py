

class Cookie:
    def __init__(self, driver):
        self.__driver = driver

    def get_all_cookie(self):
        return self.__driver.get_cookies()

    def get_cookie(self, name):
        cookies_list = self.__driver.get_cookies()
        cookies_dict = {}
        for cookie in cookies_list:
            cookies_dict[cookie['name']] = cookie['value']
        return cookies_dict[name]

    def add_cookie(self, name, value):
        self.__driver.add_cookie({'name': str(name), 'value': str(value)})


    def del_all_cookie(self):
        self.__driver.delete_all_cookies()

    def del_cookie(self, name: str):
        self.__driver.delete_cookie(name)



