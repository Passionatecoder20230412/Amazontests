from pages.AddProductsInCart import AddProductsInCart


class TestAddProductToCart:
    def test_add_product_to_cart(self,init_driver):
        add_product=AddProductsInCart(init_driver)
        add_product.add_products_feature()
