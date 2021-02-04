import pandas as pd
import datetime
import openpyxl

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import WebDriverException

def main():
	try:	
		cities_data = pd.read_excel('cities.xlsx', index_col=None, header=0) 
	except FileNotFoundError:
		print("Файл cities.xlsx не найден")
		return

	try:
		cities_temp = parse_cities_temp(cities_data)
		save_cities(cities_temp)
	except WebDriverException as e:
		print(f"Проблема драйвера Google Chrome.\n{str(e)}")
		return

def get_temp(driver, city, temp_type):
	search = driver.find_element_by_name("q")
	search.clear()
	search.send_keys(f"{city} temperature {temp_type}")
	search.send_keys(Keys.ENTER)
	element = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.ID, "wob_tm")))
	return int(element.text)

def parse_cities_temp(cities_data):
	driver = webdriver.Chrome(executable_path='chromedriver.exe')
	driver.get("https://www.google.com/")
	cities_temp = []
	for city in cities_data['City']:
		tempC = get_temp(driver, city, "celsius")
		tempF = get_temp(driver, city, "fahrenheit")
		cities_temp.append([tempC, tempF])
	driver.close()
	return cities_temp

def save_cities(cities_temp):
	dt = datetime.datetime.now().strftime("%d.%m.%Y_%H.%M")
	new_file_name = f"cities_{dt}.xlsx"

	wb = openpyxl.load_workbook('cities.xlsx')
	sheet = wb[wb.sheetnames[0]]

	for id, [tempC, tempF] in enumerate(cities_temp, start = 2):
		sheet[f"B{id}"] = tempC
		sheet[f"C{id}"] = tempF

	print(new_file_name)
	wb.save(new_file_name)

if __name__ == "__main__":
	main()
