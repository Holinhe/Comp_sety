from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

option = Options()
option.add_argument("--disable-infobars")
browser = webdriver.Chrome('C:\webdr\chromedriver.exe',chrome_options=option)
# 'https://xn--90adear.xn--p1ai/check/auto' –  ГИБДД.РФ
browser.get('https://xn--90adear.xn--p1ai/check/auto')