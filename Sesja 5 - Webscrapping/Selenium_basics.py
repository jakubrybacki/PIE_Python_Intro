# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import chromedriver_autoinstaller

# 1. Instalacja automatycznego pobierania sterownika
# pip install chromedriver-autoinstaller
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()

# 2. Inicjujemy sterownik z przeglądarka
# pip install selenium
from selenium import webdriver
driver = webdriver.Chrome()

# 3. Kierujemy sie na dowolna strone internetowa 
driver.get("https://pie.net.pl/")

# 4. Zrobmy zdjecie najpiekniejszej podstrony
driver.get("https://pie.net.pl/makroekonomia/")
filepath = "D:/"
driver.save_screenshot(filepath + "screenshot.png")

# 5. Zalozmy, ze chce zobaczyc starsze komentarze. Wybieram:
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

# 6. Moze bysmy cos kliklneli - sprobujmy z ostatnim artykulem:
# Dobrze przejrzec: https://selenium-python.readthedocs.io/locating-elements.html 
from selenium.webdriver.common.by import By
artykuly = driver.find_elements(By.XPATH, "//a[@class = 'awb-custom-text-color awb-custom-text-hover-color']")
artykuly

# Tutaj mozemy zobaczyc drobne pulapki
artykuly[-1].text
artykuly[-1].get_attribute("href")

# Kliknijmy sobie w link - to moze nie zadzialac:
artykuly[-1].click()

#### ZADANIE - ZESKRAPUJ WSZYSTKIE TEKSTY Z PIERWSZEJ STRONY ZAKLADKI MAKROEKONOMIA


# 7. Zrobmy cos mocniejszego - wpiszmy cos do formularza
driver.get("https://www.google.com/")

inputElement = driver.find_element(By.CSS_SELECTOR ,"textarea")
inputElement.send_keys('Ulrop nad morzem')

# Wciskamy przycisk enter
from selenium.webdriver.common.keys import Keys
inputElement.send_keys(Keys.RETURN);

# 8. Zaznaczmy wszystko na stronie
from selenium.webdriver.common.action_chains import ActionChains
ActionChains(driver).key_down(Keys.CONTROL).send_keys("A").key_up(Keys.CONTROL).perform()

# 9, OTworzmy nowa karte
body = driver.find_element(By.TAG_NAME, "body")
body.send_keys(Keys.CONTROL + 't')

driver.switch_to.new_window('tab')
