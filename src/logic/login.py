from dhanhq import dhanhq

def login(client_id, access_token):
    print(f"client_id : {client_id}")
    print(f"access_token : {access_token}")
    dhan = dhanhq(client_id,access_token)
    print(dhan)