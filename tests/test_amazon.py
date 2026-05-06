from pages.AddProductsInAmazon import AddProductsInAmazon
from pages.AddProductsInCart import AddProductsInCart


class TestAddProductToCart:
    def test_add_product_to_cart2(self,init_driver):
        add_product=AddProductsInAmazon(init_driver)
        add_product.add_products_feature2()
