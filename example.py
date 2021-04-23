
from campay.tools import Client


campay = Client({
    "app_username" : "",
    "app_password" : "",
    "environment" : "DEV" #"DEV" = demo mode, "PROD" = live mode
})


collect = campay.collect({
    "amount": "5",
    "currency": "XAF",
    "from": "237xxxxxxxx",
    "description": "some description"
})


disburse = campay.disburse({
    "amount": "5",
    "currency": "XAF",
    "to": "237xxxxxxxx",
    "description": "some description"
})


balance = campay.get_balance()