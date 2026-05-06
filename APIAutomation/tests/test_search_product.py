import pytest

from APIAutomation.Utilities.SearchProductApi import SearchProductApi

@pytest.mark.parametrize("text",["top","men"])
class TestSearchProduct:

    def test_search_product(self,text):
        data = {
            "search_product":text
        }

        search=SearchProductApi()
        resp=search.search_product_by_text(data)
        print(resp)
        print(resp.status_code)
        # print(resp.json())
        prod=resp.json()["products"]
        countm=0
        countw=0
        for i in prod:
            print(i)
            if (i["category"]["usertype"]["usertype"])=="Men":
                countm+=1
            else:
                countw+=1
        print(f"men count of search text {text} is {countm}")
        print(f"women count of search text {text} is {countw}")