import json
import requests
import pandas as pd


class RunHuntingQuery:

    def __init__(self, **kwargs):
        self.oath_token = kwargs.get('oath_token', 'error')
        self.query_text = kwargs.get('query_text', 'error')
        self.request_url = 'https://graph.microsoft.com/v1.0/security/runHuntingQuery'
        self.request_headers = {
            'Authorization': f'Bearer {self.oath_token}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        self.response_json = requests.request('POST',
                                              self.request_url,
                                              headers=self.request_headers,
                                              json=self.query_text).json()
        self.response_df = self._to_df()

    def _to_df(self):
        adh_df = pd.DataFrame.from_dict(self.response_json['results'])

        return adh_df

