from decouple import config

EMAIL = config('userEMAIL',default='')
PASS = config('password',default='')

URL = 'https://apps.google.com/meet/?authuser=0'
CODE = 'ofz-vuhm-uwa'
print(EMAIL,PASS)