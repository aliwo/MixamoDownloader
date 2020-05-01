from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from config import DRIVER_PATH, ACCOUNT_PATH
from download import download
from login import login
from util.download_wait import wait_download
import time

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(DRIVER_PATH, chrome_options=opts)

login(driver)
for i in range(1, 52):
    print ('page', i)
    time.sleep(10)
    download(driver, i) # 다운로드할 페이지를 선택합니다.

