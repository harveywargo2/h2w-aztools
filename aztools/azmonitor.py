import requests
import pandas as pd


class AzMonitorRunQuery:
    """A class to store and instance of data from an API call to run a query against azure monitor data

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

    def __init__(self, oauth_token='null', query_text='null', workspace_id='null'):
        """
        sets attributes for instance of object

        :param oauth_token: (str) graph api bearer token
        :param query_text: (str) advanced hunting query text
        :param workspace_id: (str) azure monitor workspace id
        """

        # parameters
        self.oauth_token = oauth_token
        self.query_text = query_text
        self.workspace_id = workspace_id

        # attributes
        self.query_json = {'query': self.query_text}
        self.request_url = f'https://api.loganalytics.azure.com/v1/workspaces/{self.workspace_id}/query'
        self.request_headers = {
            'Authorization': f'Bearer {self.oauth_token}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        self.response_json = requests.request('POST',
                                              self.request_url,
                                              headers=self.request_headers,
                                              json=self.query_json).json()
        self.response_df = self._to_df()

    def _to_df(self):
        """
        converts dict/json to pandas dataframe

        :return: dataframe stored in attribute
        """
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