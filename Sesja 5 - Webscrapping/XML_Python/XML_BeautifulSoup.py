# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 20:06:46 2024

@author: jakub
"""

from bs4 import BeautifulSoup
import pandas as pd
 
# Wybierzmy adres pliku - os.getcwd zapisuje adres gdzie odpalany jest skrypt
import os
filePath = os.getcwd() + "/" 
fileName =  "100838-2021.xml" # Zeby to uogulnic tu podasz liste

# Wczytujemy plik
with open(filePath + fileName, 'r', encoding="utf8") as f:
    data = f.read()
 
# Ustawiamy BS jako parser plikow XML
Bs_data = BeautifulSoup(data, "xml")
 
# Wszystkie Kody CPV`
CPV = Bs_data.find_all('ORIGINAL_CPV') 
print(CPV)
 
# Tekst
DESCR = Bs_data.find("SHORT_DESCR")
print(DESCR)
 
# Laczymy w Pandas 
# Tu bedzie sporo nawiasow - klamrowy robi slownik w tle, kwadratowy sprawia ze
# Tresc trafia do jednego elementu jako lista
df = pd.DataFrame({"Kody_CPV": [CPV]})
df["Opis"] = DESCR
df
