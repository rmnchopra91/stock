import pandas as pd
import json

def get_instrumet_token() :
    df = pd.read_csv('api-scrip-master.csv')
    data_dict = {}
    for index, row in df.iterrows():
        trading_symbol = row['SEM_TRADING_SYMBOL']
        exm_exch_id = row['SEM_EXM_EXCH_ID']
        if trading_symbol not in data_dict:
            data_dict[trading_symbol] = {}
        data_dict[trading_symbol][exm_exch_id] = row.to_dict()

    return data_dict

token_dict = get_instrumet_token()
# print(token_dict['TCS'])
print(json.dumps(token_dict['HDFCBANK'], indent=4))
print(token_dict['HDFCBANK']['BSE']['SEM_SMST_SECURITY_ID'])

def get_symbol_name(symbol, expiry, strike, strike_type):
    instrument = f'{symbol}-{expiry}-{str(strike)}-{strike_type}'
    return instrument


symbol = 'FINNIFTY'
expiry = 'Feb2024'
strike = 23750
strike_type = 'CE'
instrument = get_symbol_name(symbol, expiry, strike, strike_type)
# print(instrument)
# print(token_dict[instrument])
print("+++++++++++++++=======F&N======+++++++++++++++++++")
print(token_dict[instrument]['NSE']['SEM_LOT_UNITS'])
print(pd.DataFrame(token_dict[instrument]['NSE'], index=[0]))
print(token_dict[instrument]['NSE']['SEM_SMST_SECURITY_ID'])

# FINNIFTY-Feb2024-23750-CE

