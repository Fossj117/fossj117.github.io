'''
Script for sending spam FCC emails to haveibeenpwned API and 
checking which breaches were included 
'''

import requests
import time
import pandas as pd

def get_data_about_email(email): 
	"""
	Given an email, return list of breaches it was included in from API
	"""

	print "Checking account {}...".format(email)

	api_call = 'https://haveibeenpwned.com/api/v2/breachedaccount/{account}'.format(account = email)

	response = requests.get(api_call, headers = {'User-Agent': 'FCC Botting Investigation'})

	try: 
		breach_names = [b['Name'] for b in response.json()] # try to get all the breach names
	except ValueError: 
		breach_names = [] # no breaches

	print "... found breaches {} [Response {}".format(breach_names, response)
	time.sleep(1.6) # sleep to avoid hitting rate limit on have I been pwnd :(

	return breach_names


if __name__ == "__main__": 

	# Get the emails dumped from R 
	with open('spam_email_sample.csv', 'r') as f:
		emails = f.readlines()

	# Clean up the emails 
	emails = emails[1:]
	emails_clean = [e.strip('"\n') for e in emails]

	results_dic = [(e, get_data_about_email(e)) for e in emails_clean]

	results_df = pd.DataFrame(results_dic)

	results_df['in_RCM'] = results_df.breaches.apply(lambda x: 1 if 'RiverCityMedia' in x else 0)
	results_df['in_SpecialK'] = results_df.breaches.apply(lambda x: 1 if 'SpecialKSpamList' in x else 0)
	results_df['in_RCM_or_SpecialK'] = results_df.breaches.apply(lambda x: 1 if ('SpecialKSpamList' in x or 'RiverCityMedia' in x)  else 0)
	results_df['in_any_dump'] = results_df.breaches.apply(lambda x: 1 if len(x) > 0  else 0)

	results_df.to_csv('pwned_email_results.csv')

