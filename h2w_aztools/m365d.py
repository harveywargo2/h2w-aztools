import requests
import pandas as pd
import datetime


class XdrRunAhtQuery:
    """A class to store and instance of data from an API call to run a query against MSFT XDR advanced
    hunting table

    ```
    kwargs:
        oauth_token= (str) : bearer token from Graph api
        query_text= (str) : kql query in string to run

    attributes
    ----------
        query_json (dict) : api query formatting
        request_url (str) : hardcoded request api url
        request_headers (str) : hardcoded request headers
        response_json (dict) : response from api call
        pull_date (datetime) : timestamp of api call
        response_df (dataframe) : convert to pandas dataframe object

    """

    def __init__(self, **kwargs):
        # kwargs
        self.oath_token = kwargs.get('oath_token', 'error')
        self.query_text = kwargs.get('query_text', 'error')

        # attributes
        self.query_json = {'query': self.query_text}
        self.request_url = 'https://graph.microsoft.com/v1.0/security/runHuntingQuery'
        self.request_headers = {
            'Authorization': f'Bearer {self.oath_token}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        self.response_json = requests.request('POST',
                                              self.request_url,
                                              headers=self.request_headers,
                                              json=self.query_json).json()
        self.pull_date = datetime.datetime.now()
        self.response_df = self._to_df()

    def _to_df(self):
        if 'results' in self.response_json:
            adh_df = pd.DataFrame.from_dict(self.response_json['results'])
        else:
            adh_df = pd.DataFrame.from_dict(self.response_json['error'])

        return adh_df


class XdrListCustomRules:
    """A class to store and instance of data from an API call to retrieve custom detection from MSFT XDR

    ```
    kwargs:
        oauth_token= (str) : bearer token from MTP api

    attributes
    ----------
        request_url (str) : hardcoded request api url
        request_headers (str) : hardcoded request headers
        response_json (dict) : response from api call
        pull_date (datetime) : timestamp of api call

    """
    def __init__(self, **kwargs):
        # kwargs
        self.oath_token = kwargs.get('oath_token', 'error')

        # attributes
        self.request_url = 'https://api.security.microsoft.com/api/CustomDetections'
        self.request_headers = {
            'Authorization': f'Bearer {self.oath_token}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        self.response_json = requests.request('GET',
                                              self.request_url,
                                              headers=self.request_headers).json()
        self.pull_date = datetime.datetime.now()

