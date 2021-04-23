
from src.campay.tools import Client


campay = Client({
    "app_username" : "QHZKLTECJPnt_wLgGy9v8teM28As6e5lz06u5DuH-AF5naz3HA_EuXJz16ADtuoCUgJiMX_QpjUId9o6nRp3vw",
    "app_password" : "JU-bFtjhcKkfPjx53vudPAgaYZiajj--L1AwsUrBppsNpjKkHJZF7HnkWSvSeFHvkMq6gr4azCdy5mNMuFz2Jg",
    "environment" : "DEV" #"DEV" = demo mode, "PROD" = live mode
})


# collect = campay.collect({
#     "amount": "5",
#     "currency": "XAF",
#     "from": "237679587525",
#     "description": "some description"
# })


# disburse = campay.disburse({
#     "amount": "5",
#     "currency": "XAF",
#     "to": "237679587525",
#     "description": "some description"
# })


balance = campay.get_balance()