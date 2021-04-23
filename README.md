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
        from campay.tools import Client

        campay = Client({
            "app_username" : "PASTE YOUR APP_USERNAME HERE",
            "app_password" : "PASTE YOUR APP_PASSWORD HERE",
            "environment" : "DEV" #use "DEV" for demo mode or "PROD" for live mode
        })
    ```

### To collect payments from your client 

    ```python
        collect = campay.collect({
            "amount": "5", #The amount you want to collect
            "currency": "XAF",
            "from": "2376xxxxxxxx", #Phone number to request amount from. Must include country code
            "description": "some description"
        })
    ```

### To disburse
    > Please enable API withdrawal under app settings before trying this request

    ```python
        disburse = campay.disburse({
            "amount": "5", #The amount you want to disburse
            "currency": "XAF",
            "to": "237679587525", #Phone number to disburse amount to. Must include country code
            "description": "some description"
        })
    ```

### To Get application balance. 

    ```python
        balance = campay.get_balance()
    ```


## Deployment

Add additional notes about how to deploy this on a live system
Change the environment of the library introduction to PROD

  ```python
        from campay.tools import Client
        campay = Client({
            "app_username" : "PASTE YOUR APP_USERNAME HERE",
            "app_password" : "PASTE YOUR APP_PASSWORD HERE",
            "environment" : "PROD" #use "DEV" for demo mode or "PROD" for live mode
        })
  ```