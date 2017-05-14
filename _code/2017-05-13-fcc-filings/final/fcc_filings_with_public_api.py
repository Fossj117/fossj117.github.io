'''
Quick script for scraping FCC filings about docket 17-108 with Python using the 
FCC's public API https://www.fcc.gov/ecfs/public-api-docs.html

Note: 
'''

import requests 
import pandas as pd

def get_filings(endpoint, offset, n_records, proceeding, api_key): 
	''' 
	Gets FCC filings about given proceeding from endpoint, starting 
	at offset and collecting n_records (breaks if n_records too large)
	'''

	print "Trying to get filings {} to {}...".format(str(offset), str(offset + n_records))

	payload = {'limit':n_records, 'proceedings.name': proceeding, 'offset':offset, 'api_key': api_key, "sort": "date_submission,ASC"}

	r = requests.get(endpoint, params = payload)
	filings = r.json()['filings']

	print "...got {}, returned {} filings".format(r.reason, len(filings))

	return filings


def clean_data(filings): 
	''' 
	Clean up the raw scraped data for analysis
	'''

	df = pd.DataFrame(filings)

	df_filtered = df[['id_submission', 'contact_email', 'date_submission', 'date_received', 'date_disseminated','text_data', 'addressentity']]

	# Extract geo data 
	df_filtered['city'] = df_filtered.addressentity.apply(lambda x: x['city'] if 'city' in x.keys() else None)
	df_filtered['state'] = df_filtered.addressentity.apply(lambda x: x['state'] if 'state' in x.keys() else None)
	df_filtered['zip_code'] = df_filtered.addressentity.apply(lambda x: x['zip_code'] if 'zip_code' in x.keys() else None)

	df_clean = df_filtered.drop(['addressentity'], axis = 1)

	return df_clean

if __name__ == '__main__': 

	# static params
	PROCEEDING = '17-108'
	ENDPOINT = 'https://publicapi.fcc.gov/ecfs/filings'

	API_KEY = "" # Your API Key Here 

	# initialize
	OFFSET = 0
	N_RECORDS = 10000 # larger than this seems to break the API

	filings = []

	# Main Loop
	while True: 

		new_filings = get_filings(ENDPOINT, OFFSET, N_RECORDS, PROCEEDING, API_KEY)

		if new_filings: 

			filings += new_filings
			OFFSET += N_RECORDS

		else: 

			break 

	# clean the data up & write it to a file for analysis
	df_clean = clean_data(filings)
	df_clean.to_csv('raw_data_pub_api_sorted_5_14_2AM.csv', encoding = 'utf-8')



