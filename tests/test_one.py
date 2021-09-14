
def test_check_product_in_category(dashboard):

    dashboard.choose_category('Одежда и обувь')

    dashboard.choose_subcategory('Мужская одежда')

    dashboard.choose_subcategory('Мужские футболки и майки')

    dashboard.scrolle_to_product(8)

    dashboard.get_product(8)

    dashboard.display_product_picture()


def test_search_product_in_category(dashboard):

    dashboard.choose_category('Одежда и обувь')

    dashboard.choose_subcategory('Мужская одежда')

    dashboard.choose_subcategory('Мужские футболки и майки')

    dashboard.product_search("Adidas")

    dashboard.scrolle_to_product(8)

    dashboard.get_product(8)

    dashboard.display_product_picture()


