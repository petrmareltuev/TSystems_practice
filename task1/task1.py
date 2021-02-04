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
		cities_temperatures = parse_cities_temperatures(cities_data)
		save_cities(cities_temperatures)
	except WebDriverException as e:
		print(f"Проблема драйвера Google Chrome.\n{str(e)}")
		return

def get_temperature(driver, city, temperature_type):
	search_element = driver.find_element_by_name("q")
	search_element.clear()
	search_query = f"{city} temperature {temperature_type}"
	search_element.send_keys(search_query)
	search_element.send_keys(Keys.ENTER)
	temperature_element = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.ID, "wob_tm"))
	)
	temperature = int(temperature_element.text)
	return temperature

def parse_cities_temperatures(cities_data):
	driver = webdriver.Chrome(executable_path='chromedriver.exe')
	driver.get("https://www.google.com/")
	cities_temperatures = []
	for city in cities_data['City']:
		temperature_celsius = get_temperature(driver, city, "celsius")
		temperature_fahrenheit = get_temperature(driver, city, "fahrenheit")
		cities_temperatures.append([temperature_celsius, temperature_fahrenheit])
	driver.close()
	return cities_temperatures

def save_cities(cities_temperatures):
	current_time = datetime.datetime.now().strftime("%d.%m.%Y_%H.%M")
	new_file_name = f"cities_{current_time}.xlsx"

	wb = openpyxl.load_workbook('cities.xlsx')
	sheet = wb[wb.sheetnames[0]]

	for id, [temperature_celsius, temperature_fahrenheit] in enumerate(cities_temperatures, start = 2):
		sheet[f"B{id}"] = temperature_celsius
		sheet[f"C{id}"] = temperature_fahrenheit

	print(new_file_name)
	wb.save(new_file_name)

if __name__ == "__main__":
	main()
