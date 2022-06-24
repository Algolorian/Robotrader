from tda import auth, client
import json
import datetime
from config import *


try:
    td = auth.client_from_token_file(token_path, api_key)
except FileNotFoundError:
    from selenium import webdriver

    with webdriver.Chrome() as driver:
        td = auth.client_from_login_flow(
            driver, api_key, redirect_uri, token_path)



"""
r = td.get_price_history('AAPL',
                         period_type=client.Client.PriceHistory.PeriodType.YEAR,
                         period=client.Client.PriceHistory.Period.TWENTY_YEARS,
                         frequency_type=client.Client.PriceHistory.FrequencyType.DAILY,
                         frequency=client.Client.PriceHistory.Frequency.DAILY)
assert r.status_code == 200, r.raise_for_status()
print('# AAPL')
print(json.dumps(r.json(), indent=4))
"""

"""
response = td.get_quote("BA")
print('# BA')
print(response.json())
"""

"""
symbols = ['AAPL', 'BTC', 'MSFT']
response = td.search_instruments(symbols, td.Instrument.Projection.FUNDAMENTAL)
print(f'# {symbols}')
print(json.dumps(response.json(), indent=4))
"""

"""
response = td.get_option_chain('AAPL')
print('AAPL options')
print(json.dumps(response.json(), indent=4))
"""

"""
response = td.get_option_chain('AAPL', contract_type=td.Options.ContractType.CALL, strike=300)
print('AAPL options')
print(json.dumps(response.json(), indent=4))
"""

"""
expiration = datetime.datetime.strptime('2021-12-31', '%Y-%m-%d').date()
response = td.get_option_chain('AAPL',
                               contract_type=td.Options.ContractType.CALL,
                               strike=300,
                               days_to_expiration=expiration,
                               )
print('AAPL options')
print(json.dumps(response.json(), indent=4))
"""
