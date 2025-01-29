import requests
import pandas as pd
import datetime


class XdrRunAhtQuery:


    def __init__(self, oauth_token, query_text):

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
        if 'results' in self.response_json:
            adh_df = pd.DataFrame.from_dict(self.response_json['results'])
        else:
            adh_df = pd.DataFrame.from_dict(self.response_json['error'])

        return adh_df


class XdrListCustomRules:


    def __init__(self, oauth_token):

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

