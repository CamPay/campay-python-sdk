
from campay.sdk import Client as CamPayClient


campay = CamPayClient({
    "app_username" : "",
    "app_password" : "",
    "environment" : "DEV" #"DEV" = demo mode, "PROD" = live mode
})


collect = campay.collect({
    "amount": "5",
    "currency": "XAF",
    "from": "237xxxxxxxx",
    "description": "some description",
    "external_reference": "12345678"
})


collect = campay.initCollect({
    "amount": "5",
    "currency": "XAF",
    "from": "237xxxxxxxx",
    "description": "some description",
    "external_reference": "12345678"
})


collect = campay.get_payment_link({
    "amount": "5",
    "currency": "XAF",
    "description": "some description",
    "external_reference": "12345678",
    "redirect_url": "https://mysite.com/"
})


disburse = campay.disburse({
    "amount": "5",
    "currency": "XAF",
    "to": "237xxxxxxxx",
    "description": "some description",
    "external_reference": "12345678"
})


airtime = campay.transfer_airtime({
    "amount": "100",
    "to": "237xxxxxxxx",
    "external_reference": "12345678"
})


balance = campay.get_balance()


campay_status = campay.get_transaction_status({
    "reference": "bcedde9b-62a7-4421-96ac-2e6179552a1a"
})