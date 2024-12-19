from aztools.azmonitor import AzMonitorRunQuery


class SentinelRunQuery(AzMonitorRunQuery):
    """A class to store and instance of data from an API call to run a query against sentinel data
    class inherited from AzMonitorRunQuery
    Sentinel sits on top of Azure Monitor

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

    def __init__(self, oauth_token, query_text, workspace_id):
        """
        sets attributes for instance of object

        :param oauth_token: (str) graph api bearer token
        :param query_text: (str) advanced hunting query text
        :param workspace_id: (str) azure monitor workspace id
        """
        super().__init__(oauth_token, query_text, workspace_id)