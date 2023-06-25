from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from file_system import File_system

from dotenv import load_dotenv
import os
from faker import Faker


class Lazada_bot:
    username = None
    password = None
    driver = None

    def __init__(self):
        load_dotenv()
        self.username = os.environ.get("LA_USER_NAME")
        self.password = os.environ.get("LA_PASSWORD")
        option = Options()
        option.add_experimental_option("detach", True)
        # option.add_argument("--disable-feature=SensorPermissionPolicy")
        # option.add_argument(f"--user-agent={user_agent}")
        prefs = {
            "download.prompt_for_download": False,
            "download.default_directory": "/Users/fuqixuan/Documents/vscode/Kino_autobot/temp",
            "plugins.always_open_pdf_externally": True,
            "profile.default_content_settings.popups": 0,  # 设置为0，禁止弹出窗口
            # 'profile.default_content_setting_values.images': 2,#禁止图片加载
        }
        option.add_experimental_option("prefs", prefs)
        option.add_argument("--disable-blink-features=AutomationControlled")
        option.add_argument("--disable-infobars")
        option.add_argument("--disable-notifications")

        option.add_argument(
            "--user-data-dir=/Users/fuqixuan/Library/Application Support/Google/Chrome/"
        )
        webdriver_service = Service(executable_path="Chrome_driver/chromedriver")
        self.driver = webdriver.Chrome(service=webdriver_service, options=option)
        self.driver.set_window_size(1600, 1200)

    def login(self):
        self.driver.get("https://sellercenter.lazada.sg/apps/seller/login")  # 打开登录页面
        username_input = self.driver.find_element(
            by=By.XPATH, value="//input[@id='account']"
        )
        password_input = self.driver.find_element(
            by=By.XPATH, value="//input[@id='password']"
        )
        username_input.send_keys(self.username)
        password_input.send_keys(self.password)
        password_input.send_keys(Keys.ENTER)
        # try:
        #     # TODO: 识别是否有验证码
        #     time.sleep(5)

        #     self.driver.switch_to.frame(
        #         self.driver.find_element(by=By.ID, value="baxia-dialog-content")
        #     )
        #     button = self.driver.find_element(by=By.ID, value="nc_1_n1z")
        #     self.drag_and_drop(button)
        #     self.driver.switch_to.default_content()

        # except TimeoutException:
        #     print("no alert11111")
        #     return
        #     # 没有弹窗出现，继续执行其他操作
        # return

    def drag_and_drop(self, button):
        # 慢速滑动函数
        def slow_drag_and_drop(element, offset_x, offset_y, duration):
            actions = ActionChains(self.driver)
            actions.click_and_hold(element).perform()
            steps = int(duration / 100)
            for _ in range(steps):
                actions.move_by_offset(offset_x / steps, offset_y / steps).perform()
                time.sleep(0.1)  # 调整每一小步之间的等待时间
            actions.release().perform()

        slow_drag_and_drop(button, 300, 0, 1000)  # 调整滑动的偏移量和持续时间

        print("no alert")

    def step_to_business_advisor(self):
        # element = self.driver.find_element(
        #     by=By.XPATH,
        #     value="//i[contains(@class, 'a-l-icon-toggle-right')]",
        # )

        # element.click()

        self.driver.execute_script("window.scrollBy(0, 500);")
        list_element = self.driver.find_element(
            by=By.XPATH, value="//*[@id='layout-new-menu-content']/li[4]"
        )
        self.hover_element(list_element)
        print(list_element)
        # ul_element = self.driver.find_element(
        #     by=By.CSS_SELECTOR, value="ul#a-l-menu-content"
        # )
        # print(ul_element)
        # element = ul_element.find_element(by=By.TAG_NAME, value="li")[3]
        # print(element)
        # self.hover_element(element)
        # element.click()

        # time.sleep(3)

        element = self.driver.find_element(
            by=By.XPATH, value="//a[@title='Business Advisor']"
        )
        element.click()

    def step_to_day_item_set_earlist_day(self):
        self.driver.execute_script("window.scrollBy(0, 1000);")
        element = self.driver.find_element(
            by=By.CSS_SELECTOR, value=".SCBADatepicker_dropdownTrigger__LDxBI"
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def hover_element(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()


class Task1(Lazada_bot):
    def __init__(self):
        super().__init__()

    def step_to_day_item_set_earlist_day(self):
        self.driver.execute_script("window.scrollBy(0, 1000);")
        element = self.driver.find_element(
            by=By.CSS_SELECTOR, value=".SCBADatepicker_dropdownTrigger__LDxBI"
        )

        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        sub_element = self.driver.find_element(
            by=By.XPATH,
            value='//*[@id="main"]/section/div[2]/div/div[1]/div/div[2]/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div[4]',
        )
        sub_element.click()
        subsub_element = self.driver.find_element(
            by=By.XPATH,
            value='//*[@id="main"]/section/div[2]/div/div[1]/div/div[2]/div/div[3]/div/div/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]/table/tbody/tr[4]/td[6]',
        )
        subsub_element.click()
        time.sleep(3)
        # self.set_init_day()

    def download_file(self):
        self.driver.execute_script("window.scrollBy(0, 1000);")
        element = self.driver.find_element(
            by=By.XPATH,
            value='//*[@id="main"]/section/div[2]/div/div[1]/div/div[2]/div/div[4]/article/header/div[2]/div[2]/div',
        )
        element.click()
        self.__download_verify()

    def __download_verify(self):
        time.sleep(2)

        button_download = self.driver.find_element(
            by=By.XPATH,
            value="//button[contains(., 'Ok')]",
        )
        button_download.click()

    def set_init_day(self):
        element = self.driver.find_element(
            by=By.XPATH,
            value='//*[@id="main"]/section/div[2]/div/div[1]/div/div[2]/div/div[3]/div/div/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div/div[1]/svg',
        )

        for _ in range(10):
            element.click()


test = Task1()
test.login()
print(test.username)
time.sleep(3)
test.step_to_business_advisor()
# test.step_to_day_item_set_earlist_day()
temp_file = File_system("./temp")
test.download_file()
time.sleep(3)
new_files = temp_file.check_new_files()
if new_files:
    print("发现新的文件:")
    for file in new_files:
        print(file)
else:
    print("没有发现新的文件")
test.driver.quit()
