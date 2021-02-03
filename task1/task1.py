import pandas as pd
import datetime
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# get cities list from excel file
cities_data = pd.read_excel('cities.xlsx', index_col=None, header=0)  

# using google search
driver = webdriver.Chrome(executable_path='chromedriver.exe')
url = "https://www.google.com/"
driver.get(url)

def get_temp(driver, city, temp_type):
	search = driver.find_element_by_name("q")
	search.clear()
	search.send_keys(f"{city} temperature {temp_type}")
	search.send_keys(Keys.ENTER)
	element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "wob_tm")))
	return int(element.text)

cities_temp = []
for city in cities_data['City']:
	tempC = get_temp(driver, city, "celsius")
	tempF = get_temp(driver, city, "fahrenheit")
	cities_temp.append([tempC, tempF])
driver.close()

dt = datetime.datetime.now().strftime("%d.%m.%Y_%H.%M")
new_file_name = f"cities_{dt}.xlsx"

wb = openpyxl.load_workbook('cities.xlsx')
sheet = wb[wb.sheetnames[0]]

for id, [tempC, tempF] in enumerate(cities_temp, start = 2):
	sheet[f"B{id}"] = tempC
	sheet[f"C{id}"] = tempF

print(new_file_name)
wb.save(new_file_name)