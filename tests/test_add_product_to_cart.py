import pytest

from pages.AddProductsInCart import AddProductsInCart

@pytest.mark.skip(reason="Skipping this test for now")
class TestAddProductToCart:
    def test_add_product_to_cart(self,init_driver):
        add_product=AddProductsInCart(init_driver)
        add_product.add_products_feature()
