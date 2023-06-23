from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import os

# 加载 .env 文件
load_dotenv()

api_key = os.environ.get("API_KEY")
secret_key = os.environ.get("SECRET_KEY")

option = Options()
option.add_argument("--disable-gpu")
option.add_experimental_option("detach", True)

webdriver_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=webdriver_service, options=option)
driver.set_window_size(1280, 800)
url = "https://sellercenter.lazada.sg/apps/seller/login"
driver.get(url)

driver.quit()
