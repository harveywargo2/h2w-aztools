import requests
import pandas as pd


class AzMonitorRunQuery:

    def __init__(self, **kwargs):
        self.oath_token = kwargs.get('oath_token', 'error')
        self.query_text = kwargs.get('query_text', 'error')
        self.workspace_id = kwargs.get('workspace_id', 'error')
        self.request_url = f'https://api.loganalytics.azure.com/v1/workspaces/{self.workspace_id}/query'
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
        col_names_df = []

        if 'tables' in self.response_json:
            column_name_list = self.response_json['tables'][0]['columns']
            row_list = self.response_json['tables'][0]['rows']

            for item in column_name_list:
                col_names_df.append(item['name'])
            out_df = pd.DataFrame(row_list, columns=col_names_df)

        else:
            out_df = pd.DataFrame.from_dict(self.response_json)

        return out_df
