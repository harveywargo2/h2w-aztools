import requests


class AzureOath:

    def __init__(self, **kwargs):
        self.tenant_id = kwargs.get('tenant_id', 'error')
        self.client_id = kwargs.get('client_id', 'error')
        self.client_secret = kwargs.get('client_secret', 'error')


class AzureOathGraph(AzureOath):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.graph_auth = f'https://login.windows.net/{self.tenant_id}/oauth2/token'
        self.graph_resource_url = 'https://graph.microsoft.com'
        self.request_header = {'Content-Type': 'application/x-www-form-urlencoded'}
        self.request_body = {
            'resource': self.graph_resource_url,
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'client_credentials'
        }
        self.response_json = requests.request('POST', self.graph_auth,
                                               headers=self.request_header,
                                               data=self.request_body).json()

        self.token_type = self.response_json['token_type']
        self.access_token = self.response_json['access_token']
        self.expires_in_seconds = self.response_json['expires_in']
        self.expires_on_epoch = self.response_json['expires_on']


class AzureOathMde(AzureOath):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mde_auth = f'https://login.windows.net/{self.tenant_id}/oauth2/token'
        self.mde_resource_url = 'https://api.securitycenter.windows.com'
        self.request_header = {'Content-Type': 'application/x-www-form-urlencoded'}
        self.request_body = {
            'resource': self.mde_resource_url,
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'client_credentials'
        }
        self.response_json = requests.request('POST', self.mde_auth,
                                               headers=self.request_header,
                                               data=self.request_body).json()

        self.token_type = self.response_json['token_type']
        self.access_token = self.response_json['access_token']
        self.expires_in_seconds = self.response_json['expires_in']
        self.expires_on_epoch = self.response_json['expires_on']


class AzureOathMdeMtp(AzureOath):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mtp_auth = f'https://login.windows.net/{self.tenant_id}/oauth2/token'
        self.mtp_resource_url = 'https://security.microsoft.com/mtp/'
        self.request_header = {'Content-Type': 'application/x-www-form-urlencoded'}
        self.request_body = {
            'resource': self.mtp_resource_url,
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'client_credentials'
        }
        self.response_json = requests.request('POST', self.mtp_auth,
                                               headers=self.request_header,
                                               data=self.request_body).json()

        self.token_type = self.response_json['token_type']
        self.access_token = self.response_json['access_token']
        self.expires_in_seconds = self.response_json['expires_in']
        self.expires_on_epoch = self.response_json['expires_on']


class AzureOathLogAnalytics(AzureOath):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.la_auth = f'https://login.windows.net/{self.tenant_id}/oauth2/token'
        self.la_resource_url = 'https://api.loganalytics.io'
        self.request_header = {'Content-Type': 'application/x-www-form-urlencoded'}
        self.request_body = {
            'resource': self.la_resource_url,
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'client_credentials'
        }
        self.response_json = requests.request('POST', self.la_auth,
                                               headers=self.request_header,
                                               data=self.request_body).json()

        self.token_type = self.response_json['token_type']
        self.access_token = self.response_json['access_token']
        self.expires_in_seconds = self.response_json['expires_in']
        self.expires_on_epoch = self.response_json['expires_on']


class AzureOathArm(AzureOath):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.arm_auth = f'https://login.windows.net/{self.tenant_id}/oauth2/token'
        self.arm_resource_url = 'https://management.azure.com'
        self.request_header = {'Content-Type': 'application/x-www-form-urlencoded'}
        self.request_body = {
            'resource': self.arm_resource_url,
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'client_credentials'
        }
        self.response_json = requests.request('POST', self.arm_auth,
                                               headers=self.request_header,
                                               data=self.request_body).json()

        self.token_type = self.response_json['token_type']
        self.access_token = self.response_json['access_token']
        self.expires_in_seconds = self.response_json['expires_in']
        self.expires_on_epoch = self.response_json['expires_on']