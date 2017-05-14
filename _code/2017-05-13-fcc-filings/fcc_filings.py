'''
Quick script for scraping FCC filings about docket 17-108 with Python
'''

import requests 
import pandas as pd


def get_filings(endpoint, offset, n_records, proceeding): 
	''' 
	Gets FCC filings about given proceeding from endpoint, starting 
	at offset and collecting n_records (breaks if n_records too large)
	'''

	print "Trying to get filings {} to {}".format(str(offset), str(offset + n_records))

	payload = {'limit':n_records, 'proceedings.name': proceeding, 'offset':offset}
	return requests.get('https://ecfsapi.fcc.gov/filings', params = payload).json()['filings']

def clean_data(filings): 
	''' 
	Clean up the raw scraped data for analysis
	'''

	df = pd.DataFrame(filings)

	df_filtered = df[['contact_email', 'date_submission', 'text_data', 'addressentity']]

	# Extract geo data 
	df_filtered['city'] = df_filtered.addressentity.apply(lambda x: x['city'] if 'city' in x.keys() else None)
	df_filtered['state'] = df_filtered.addressentity.apply(lambda x: x['state'] if 'state' in x.keys() else None)
	df_filtered['zip_code'] = df_filtered.addressentity.apply(lambda x: x['zip_code'] if 'zip_code' in x.keys() else None)

	df_clean = df_filtered.drop(['addressentity'], axis = 1)

	return df_clean

if __name__ == '__main__': 

	# static params
	proceeding = '17-108'
	endpoint = 'https://ecfsapi.fcc.gov/filings'

	# initialize
	offset = 0
	n_records = 10000 # larger than this seems to break the API
	filings = []

	# Main Loop
	while True: 

		new_filings = get_filings(endpoint, offset, n_records, proceeding)

		if new_filings: 

			filings += new_filings
			offset += n_records

		else: 

			break 

	# clean the data up & write it to a file for analysis
	df_clean = clean_data(filings)
	df_clean.to_csv('raw_data_5_11_2AM.csv', encoding = 'utf-8')



