from aztools.azmonitor import AzMonitorRunQuery
import requests
import datetime


class SentinelRunQuery(AzMonitorRunQuery):


    def __init__(self, oauth_token, query_text, workspace_id):
        super().__init__(oauth_token, query_text, workspace_id)


class SentinelListRules:


    def __init__(self, subscription_id, resource_group, workspace, auth_token, api_version='2024-09-01'):

        # parameter
        self.subscription_id = subscription_id
        self.resource_group = resource_group
        self.workspace = workspace
        self.api_version = api_version
        self.auth_token = auth_token

        # attributes
        self.request_url = f'https://management.azure.com/subscriptions/{self.subscription_id}/resourceGroups/{self.resource_group}/providers/Microsoft.OperationalInsights/workspaces/{self.workspace}/providers/Microsoft.SecurityInsights/alertRules?api-version={self.api_version}'
        self.request_headers = {
            'Authorization': f'Bearer {self.auth_token}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        self.response_json = requests.request('GET',
                                              self.request_url,
                                              headers=self.request_headers).json()
        self.pull_date = datetime.datetime.now()

