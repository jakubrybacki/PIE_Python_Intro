# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 20:42:44 2021

@author: Jakub
"""

import time
import pandas as pd
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# DATA IMPUT
filePath = os.getcwd() + "\\"
categoryName = "procesory"

#Ustawienie ostatniej strony wymaga ręcznego sprawdzenia do jakiej daty ostatnio były zbierane dane i ustawienie tego tutaj z pewnym zapasem (duplikaty i tak potem sie same usuną)
lastPage = 21

# DOWNLOADING CLASS
class PepperInfoSelenium():
    
    def __init__(self, InfoCategory, InfoPageNumber):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        
        self.page = str(InfoPageNumber)
        self.webURL = "https://www.pepper.pl/grupa/" + InfoCategory + "?page=" + self.page 
        self.driver = webdriver.Chrome(options=chrome_options)
        #self.driver.minimize_window()
        self.driver.get(self.webURL)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        
    def __cleanDataFrame(self, _t):
        _t = _t.replace('\\n',' ', regex=True)
        _t = _t.replace('\\t',' ', regex=True)
        _t = _t.replace("\xa0", ";" , regex = True)
        _t = _t.replace("\xa3", "" , regex = True)
        return _t
       
    def getData(self):
        NamesList = self.driver.find_elements(By.XPATH,".//strong[contains(@class,'thread-title')]")
        DatesList = self.driver.find_elements(By.XPATH,".//div[contains(@class,'threadGrid-headerMeta')]")
        InfoList = self.driver.find_elements(By.XPATH,".//span[contains(@class,'overflow--fade')]")

        #print(len(NamesList), len(DatesList), len(InfoList))

        if len(DatesList) > len(NamesList):
            DatesList = DatesList[0:len(NamesList)]
                             
        Names = [el.get_attribute("textContent") for el in NamesList]
        Dates = [el.get_attribute("textContent") for el in DatesList]
        Info = [el.get_attribute("textContent") for el in InfoList]
        
        DealsList = pd.DataFrame({
            "Date": Dates,
            "Name": Names,
            "Desc": Info
        })
        self.DealsList = self.__cleanDataFrame(DealsList)
        return self.DealsList    

# FIRST DOWNLOAD
a = PepperInfoSelenium(categoryName,1)
deals =  a.getData()
deals.head(10)
a.driver.close() 

for i in range(2, lastPage + 1):
    print(f"pobrano stronę: {i}")
    a = PepperInfoSelenium(categoryName, i)
    deals = pd.concat([deals, a.getData()])
    time.sleep(1)
    a.driver.close() 
#    updated_years=pd.concat([deals, old_df], copy=False)

# SAVE
deals.to_csv(filePath + "Okazje2.csv", index = False, encoding="windows-1250")