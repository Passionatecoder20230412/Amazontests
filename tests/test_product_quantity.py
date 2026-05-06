import pytest

from pages.VerifyProductQuantity import VerifyProductQuantity

@pytest.mark.parametrize("text,repeat",[("casio",4),("casio",10)])
class TestProductQuantity:
    def test_quantity(self,init_driver,text,repeat):

        quantity=VerifyProductQuantity(init_driver)
        quantity.get_url()
        result=quantity.verify_product_quantity(text,repeat)
        print(result)