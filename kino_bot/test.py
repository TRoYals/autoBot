from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


option = Options()
option.add_argument("--disable-gpu")
option.add_experimental_option("detach", True)

webdriver_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=webdriver_service, options=option)
driver.set_window_size(800, 600)
url = "https://doc.yonisv.com/mybook/flow/suportnotice.html"
driver.get(url)

href_list = []


def traverse_element(element):
    # 找到所有子节点的 <a> 元素
    child_elements = element.find_elements(By.TAG_NAME, "a")

    # 遍历子节点
    for child_element in child_elements:
        href = child_element.get_attribute("href")
        href_list.append(href)
        # 递归遍历子节点的子节点
        traverse_element(child_element)


elements_nav = driver.find_elements(By.CSS_SELECTOR, "div.book-summary")
traverse_element(elements_nav[0])
for href in href_list:
    url = href
    driver.get(url)
    elements = driver.find_elements(
        by=By.CSS_SELECTOR,
        value="section.normal.markdown-section:not(.treeview__container)",
    )
    with open("output.txt", "a") as file:
        for element in elements:
            content = element.text
            file.write(content)


driver.quit()
