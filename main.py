from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# ----- 取消網頁彈出式試窗 ------
options = Options()
options.add_argument("--disable-notifications")

chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
chrome.get('https://www.instagram.com/?hl=zh-tw')
time.sleep(5)

chrome.close()
