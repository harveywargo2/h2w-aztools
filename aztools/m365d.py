import requests
import pandas as pd
import datetime


class XdrRunAhtQuery:
    """A class to store and instance of data from an API call to run a query against MSFT XDR advanced
    hunting table

    ```
    attributes
    ----------
        query_json (dict) : api query formatting
        request_url (str) : hardcoded request api url
        request_headers (dict) : hardcoded request headers
        response_json (dict) : response from api call
        pull_date (datetime) : timestamp of api call
        response_df (dataframe) : convert to pandas dataframe object
    """

    def __init__(self, oauth_token='null', query_text='null'):
        """
        sets attributes for instance of object

        :param oauth_token: (str) graph api bearer token
        :param query_text: (str) advanced hunting query text
        """

        # parameters
        self.oath_token = oauth_token
        self.query_text = query_text

        # attributes
        self.query_json = {"Query": self.query_text}
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
        """
        converts dict/json to pandas dataframe

        :return: dataframe stored in attribute
        """
        if 'results' in self.response_json:
            adh_df = pd.DataFrame.from_dict(self.response_json['results'])
        else:
            adh_df = pd.DataFrame.from_dict(self.response_json['error'])

        return adh_df


class XdrListCustomRules:
    """A class to store and instance of data from an API call to retrieve custom detection from MSFT XDR

    ```
    attributes
    ----------
        request_url (str) : hardcoded request api url
        request_headers (dict) : hardcoded request headers
        response_json (dict) : response from api call
        pull_date (datetime) : timestamp of api call
    """

    def __init__(self, oauth_token='null'):
        """
        sets attributes for instance of object

        :param oauth_token: (str) graph api bearer token
        """

        # parameter
        self.oath_token = oauth_token

        # attributes
        self.request_url = 'https://graph.microsoft.com/beta/security/rules/detectionRules'
        self.request_headers = {
            'Authorization': f'Bearer {self.oath_token}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        self.response_json = requests.request('GET',
                                              self.request_url,
                                              headers=self.request_headers).json()
        self.pull_date = datetime.datetime.now()

