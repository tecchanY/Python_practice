from selenium import webdriver  # pip install seleniumで入れたseleniumのwebdriverを使う
from time import sleep

driver = webdriver.Chrome("./chromedriver.exe")  # webdriver.exeの利用とパスの指定
driver.get("http://www.yahoo.co.jp")  # chrome起動してyahooに遷移

print(driver.current_url)  # URLを確認する

sleep(3)  # 読み込みを待つために3秒間処理を停止、普通はwaitを使う

searchBox = driver.find_element_by_class_name(
    "_1wsoZ5fswvzAoNYvIJgrU4"
)  # 検索入力ボックスのhtmlを検索
searchBox.send_keys("今日のニュース")  # 検索したいワードを入力、空白スペースあっても大丈夫

searchBotton = driver.find_element_by_class_name(
    "_63Ie6douiF2dG_ihlFTen"
)  # htmlから検索ボタンを探す
searchBotton.click()  # 検索ボタンのクリック

print(driver.current_url)  # URLを確認する

sleep(3)
driver.quit()
