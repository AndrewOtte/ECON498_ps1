import os 
from bs4 import BeautifulSoup
import glob
import pandas as pd


if not os.path.exists("parsed_results"):
	os.mkdir("parsed_results")

df = pd.DataFrame()

for one_file_name in glob.glob("html_files/*.html"):
	print("parsing: " + one_file_name)
	scrapping_time = os.path.splitext(os.path.basename(one_file_name))[0].replace("cmc","")
	f = open(one_file_name, "r", encoding="utf-8")
	soup = BeautifulSoup(f.read(), 'html.parser')
	f.close()
	currencies_table = soup.find("table", {"id": "currencies-all"})
	# print(currencies_table)
	currencies_tbody = currencies_table.find("tbody")
	currency_rows = currencies_tbody.find_all("tr")
	
	for r in currency_rows:
		currency_symbol = r.find("td", {"class": "currency-name"}).find("span",{"class":"currency-symbol"}).find("a").text
		currency_name = r.find("td", {"class": "currency-name"}).find("a",{"class":"currency-name-container"}).text
		currency_market_cap = r.find("td", {"class":"market-cap"})['data-sort']
		currency_price = r.find("a",{"class": "price"}).text
		currency_supply = r.find("td", {"class": "circulating-supply"}).find("span")['data-supply']
		currency_volume = r.find("a",{"class": "volume"}).text

		df = df.append({
			'Scrapping_Time': scrapping_time, 
			'Symbol': currency_symbol,
			'Name': currency_name,
			'Market_Cap': currency_market_cap,
			'Price': currency_price,
			'Circulating_Supply': currency_supply,
			'Volume': currency_volume
			}, ignore_index=True)

df.to_csv("parsed_results/cmc_dataset.csv")