from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

options = webdriver.ChromeOptions()

driver_path = 'C:\\Users\\GonzaloRS\\Desktop\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, options=options)

driver.get("https://mercadolibre.com.pe")

