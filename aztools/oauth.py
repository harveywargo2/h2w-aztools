import requests


class AzureOathGraph:
    """
    Class Object for calls to azure graph api
    ```
    Attributes
    ----------
        graph_auth (str) : azure graph url for tenant
        graph_resource_url (str) : azure oath token grant for graph api
        request_header (dict) : hardcoded request headers
        request_body (dict) : hardcoded request body
        response_json (dict) : json api response
        token_typ (str or dict) : token type issued from azure
        access_token (str or dict) : access token granted

    """

    def __init__(self, tenant_id='null', client_id='null', client_secret='null'):
        """
        sets attributes for instance of object

        :param tenant_id: (str) azure tenant id
        :param client_id: (str) client identifier from aad-app/service principal
        :param client_secret: (str) client secret from aad-app/service principal
        """

        # parameters
        self.tenant_id = tenant_id
        self.client_id = client_id
        self.client_secret = client_secret

        # attributes
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

        self.token_type = self._token_type()
        self.access_token = self._access_token()


    def _token_type(self):
        if 'token_type' in self.response_json:
            output = self.response_json['token_type']
        else:
            output = self.response_json['error']

        return output

    def _access_token(self):
        if 'access_token' in self.response_json:
            output = self.response_json['access_token']
        else:
            output = self.response_json['error']

        return output


class AzureOathMde:
    """
    Class Object for calls to MSFT XDR Defender Endpoint api
    ```
    Attributes
    ----------
        graph_auth (str) : azure graph url for tenant
        graph_resource_url (str) : azure oath token grant for MDE api
        request_header (dict) : hardcoded request headers
        request_body (dict) : hardcoded request body
        response_json (dict) : json api response
        token_typ (str or dict) : token type issued from azure
        access_token (str or dict) : access token granted

    """

    def __init__(self, tenant_id='null', client_id='null', client_secret='null'):
        """
        sets attributes for instance of object

        :param tenant_id: (str) azure tenant id
        :param client_id: (str) client identifier from aad-app/service principal
        :param client_secret: (str) client secret from aad-app/service principal
        """

        # parameters
        self.tenant_id = tenant_id
        self.client_id = client_id
        self.client_secret = client_secret

        # attributes
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

        self.token_type = self._token_type()
        self.access_token = self._access_token()

    def _token_type(self):
        if 'token_type' in self.response_json:
            output = self.response_json['token_type']
        else:
            output = self.response_json['error']

        return output

    def _access_token(self):
        if 'access_token' in self.response_json:
            output = self.response_json['access_token']
        else:
            output = self.response_json['error']

        return output


class AzureOathLogAnalytics:
    """
    Class Object for calls to azure log analytics/azuremonitor api
    ```
    Attributes
    ----------
        graph_auth (str) : azure graph url for tenant
        graph_resource_url (str) : azure oath token grant for Log Analytics/Azure Monitor api
        request_header (dict) : hardcoded request headers
        request_body (dict) : hardcoded request body
        response_json (dict) : json api response
        token_typ (str or dict) : token type issued from azure
        access_token (str or dict) : access token granted

    """

    def __init__(self, tenant_id='null', client_id='null', client_secret='null'):
        """
        sets attributes for instance of object

        :param tenant_id: (str) azure tenant id
        :param client_id: (str) client identifier from aad-app/service principal
        :param client_secret: (str) client secret from aad-app/service principal
        """

        # parameters
        self.tenant_id = tenant_id
        self.client_id = client_id
        self.client_secret = client_secret

        # attributes
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

        self.token_type = self._token_type()
        self.access_token = self._access_token()

    def _token_type(self):
        if 'token_type' in self.response_json:
            output = self.response_json['token_type']
        else:
            output = self.response_json['error']

        return output

    def _access_token(self):
        if 'access_token' in self.response_json:
            output = self.response_json['access_token']
        else:
            output = self.response_json['error']

        return output


class AzureOathArm:
    """
    Class Object for calls to azure resource manager api
    ```
    Attributes
    ----------
        graph_auth (str) : azure graph url for tenant
        graph_resource_url (str) : azure oath token grant for arm api
        request_header (dict) : hardcoded request headers
        request_body (dict) : hardcoded request body
        response_json (dict) : json api response
        token_typ (str or dict) : token type issued from azure
        access_token (str or dict) : access token granted

    """

    def __init__(self, tenant_id='null', client_id='null', client_secret='null'):
        """
        sets attributes for instance of object

        :param tenant_id: (str) azure tenant id
        :param client_id: (str) client identifier from aad-app/service principal
        :param client_secret: (str) client secret from aad-app/service principal
        """

        # parameters
        self.tenant_id = tenant_id
        self.client_id = client_id
        self.client_secret = client_secret

        # attributes
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

        self.token_type = self._token_type()
        self.access_token = self._access_token()

    def _token_type(self):
        if 'token_type' in self.response_json:
            output = self.response_json['token_type']
        else:
            output = self.response_json['error']

        return output

    def _access_token(self):
        if 'access_token' in self.response_json:
            output = self.response_json['access_token']
        else:
            output = self.response_json['error']

        return output
