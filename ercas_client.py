# ercaspay_client.py
import requests
import json

class ErcasPayClient:
    def __init__(self, api_key, base_url, sandbox=True):
        self.api_key = api_key
        if sandbox:
            self.base_url = "https://api.merchant.staging.ercaspay.com/api/v1"
        else:
           self.base_url =  "https://api.ercaspay.com/api/v1"
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        self.timeout = 10 

    def _request(self, method, url, data=None):
      try:
          response = requests.request(
              method,
              url,
              headers=self.headers,
              json=data,
              timeout=self.timeout
          )
          response.raise_for_status()  
          return response.json()
      except requests.exceptions.RequestException as e:
          raise Exception(f"API Request Error: {e}")

    def initiate_payment(self, amount, payment_reference, payment_methods,
                         customer_name, currency, customer_email, customer_phone_number,
                         redirect_url, description, metadata):
         
         payload = {
              "amount": amount,
              "paymentReference": payment_reference,
              "paymentMethods": payment_methods,
              "customerName": customer_name,
              "currency": currency,
              "customerEmail": customer_email,
              "customerPhoneNumber": customer_phone_number,
              "redirectUrl": redirect_url,
              "description": description,
              "metadata": metadata
          }

         return self._request("POST", f"{self.base_url}/payment/initiate", data=payload)