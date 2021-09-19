
def test_cookie(dashboard):
    print(dashboard._cookie.get_all_cookie())
    print('----------------------------------')
    dashboard._cookie.add_cookie("Name", "John")
    print(dashboard._cookie.get_all_cookie())
    print('----------------------------------')
    print(dashboard._cookie.get_cookie('Name'))
    print('----------------------------------')
    print(dashboard._cookie.get_cookie('Name'))










