# [CamPay](https://www.campay.net/) Python SDK

Python SDK for CamPay Payment Gateway

CamPay is a Fintech service of the company TAKWID
GROUP which launched its financial services in Cameroon
from January 2021.

We provide businesses and institutions with solutions for
collecting and transferring money online, via primarily
Mobile Money(MTN and Orange).

With CamPay, simplify the purchasing experience for
your customers thanks to our mobile money
payment solutions, accessible via your website
and/or mobile application.


## Summary

  - [Getting Started](#getting-started)
  - [Running the samples](#running-the-samples)
  - [Deployment](#deployment)

## Getting Started

These instructions will get you started with the CamPay SDK for development and testing purposes. See deployment
for notes on how to deploy the project on a live system.

### Prerequisites

 - Create an account on [CamPay](https://www.campay.net/) platform
 - Register an application under your account.
 - Expand your registered application to get access to your API keys

### Installing

   ```python
        pip install campay
   ```

## Running the samples

  - Initialize the library with credentials. 
    ```python
        from campay.sdk import Client as CamPayClient

        campay = CamPayClient({
            "app_username" : "PASTE YOUR APP_USERNAME HERE",
            "app_password" : "PASTE YOUR APP_PASSWORD HERE",
            "environment" : "DEV" #use "DEV" for demo mode or "PROD" for live mode
        })
    ```

### To collect payments from your client - DIRECTLY

   **OPTION 1**: This option initiates a transaction and waits( or block the running code) for the transaction to complete before returning a response. 

   ```python
         collect = campay.collect({
            "amount": "5", #The amount you want to collect
            "currency": "XAF",
            "from": "2376xxxxxxxx", #Phone number to request amount from. Must include country code
            "description": "some description",
            "external_reference": "", #Reference from the system initiating the transaction.
         })

         print(collect)
         #{"reference": "bcedde9b-62a7-4421-96ac-2e6179552a1a", "external_reference":"12345678", "status": "SUCCESSFUL", "amount": 5, "currency": "XAF", "operator": "MTN", "code": "CP201027T00005", "operator_reference":  "1880106956" }
         
   ```
   > status can be SUCCESSFUL or FAILED

   **OPTION 2**: This option initiates a transaction and immediately returns the initiated transaction reference for you to use to check the status of the transaction.

   ```python
         collect = campay.initCollect({
            "amount": "5", #The amount you want to collect
            "currency": "XAF",
            "from": "2376xxxxxxxx", #Phone number to request amount from. Must include country code
            "description": "some description",
            "external_reference": "", #Reference from the system initiating the transaction.
         })

         print(collect)
         #{"reference": "bcedde9b-62a7-4421-96ac-2e6179552a1a", "ussd_code": "*126# for MTN or #150*50# for ORANGE", "operator": "mtn or orange" }
         
   ```
   > The default status for initiated transactions is PENDING
   

### To collect payments from your client - using PAYMENT LINKS

   ```python
         payment_link = campay.get_payment_link({
            "amount": "5",
            "currency": "XAF",
            "description": "some description",
            "external_reference": "12345678",
            "redirect_url": "https://mysite.com/"
         })

         print(payment_link)
         #{"status": "SUCCESSFUL", "link": "https://www.campay.com/pay/with/link/" }
         '''
         Redirect your customer to the returned payment link 
         '''
         
   ```
   > status can be SUCCESSFUL or FAILED


### To check a transaction status.

   You need the initiated transaction **reference** to use this function.

   ```python
         campay_status = campay.get_transaction_status({
            "reference": "bcedde9b-62a7-1234-96ac-2e6179552a1a", #The amount you want to collect
         })

         print(campay_status)
         #{"reference": "bcedde9b-62a7-4421-96ac-2e6179552a1a", "external_reference":"12345678", "status": "SUCCESSFUL", "amount": 5, "currency": "XAF", "operator": "MTN", "code": "CP201027T00005", "operator_reference":  "1880106956" }
         
   ```
   > status can be PENDING, SUCCESSFUL or FAILED


### To disburse
   > Please enable API withdrawal under app settings before trying this request
   
   ```python
        disburse = campay.disburse({
            "amount": "5", #The amount you want to disburse
            "currency": "XAF",
            "to": "2376xxxxxxxx", #Phone number to disburse amount to. Must include country code
            "description": "some description",
            "external_reference": "", #Reference from the system initiating the transaction.
        })

        print(disburse)
        #{"reference": "bcedde9b-62a7-4421-96ac-2e6179552a1a", "external_reference":"12345678", "status": "SUCCESSFUL", "amount": 5, "currency": "XAF", "operator": "MTN", "code": "CP201027T00005", "operator_reference":  "1880106956" }

   ```
   > status can be SUCCESSFUL or FAILED

### To Get application balance.

   ```python
        balance = campay.get_balance()

        print(balance)
        #{"total_balance": 0, "mtn_balance": 0, "orange_balance": 0, "currency": "XAF"}
   ```

### Transfer Airtime
   > Please enable API withdrawal under app settings before trying this request
   
   ```python
        airtime = campay.transfer_airtime({
            "amount": "100", #The amount you want to transfer
            "to": "2376xxxxxxxx", #Phone number to receive airtime. Must include country code
            "external_reference": "", #Reference from the system initiating the transaction.
        })

        print(airtime)
        #{"reference": "bcedde9b-62a7-4421-96ac-2e6179552a1a", "external_reference":"12345678", "status": "SUCCESSFUL", "amount": 5, "currency": "XAF", "operator": "MTN", "code": "CP201027U00005", "operator_reference":  "1880106956" }

   ```
   > status can be SUCCESSFUL or FAILED

## Deployment

Change the environment of the library introduction to PROD

  ```python
        from campay.sdk import Client
        campay = Client({
            "app_username" : "PASTE YOUR APP_USERNAME HERE",
            "app_password" : "PASTE YOUR APP_PASSWORD HERE",
            "environment" : "PROD" #use "DEV" for demo mode or "PROD" for live mode
        })
  ```