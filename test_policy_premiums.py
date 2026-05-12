from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



def test_premiums():
    driver=webdriver.Edge()
    driver.maximize_window()
    driver.get("https://termlife.policybazaar.com/quotes/7rMVfMYfCfyfnDH8o3URaA==?refId=7rMVfMYfCfyfnDH8o3URaA==&custId=9M5Uy2NnDX7UHD9LW0XSiXeHDZXSLQgsEzBvOM5eqytWZCKi_lXF59FokKBV3mwM&isProgressiveJourney=true&isMobileDefault=true&iscom=1&refkey=1&payType=1&page=1&isDefaultCity=false")
    wait=WebDriverWait(driver, 30)
    prem=wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".pricehide2")))
    print(prem)
    for i in prem:
        print(i.text,end="")
    print("done")
    driver.quit()
