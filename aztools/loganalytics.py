from aztools.azmonitor import AzMonitorRunQuery


class LogAnalyticsRunQuery(AzMonitorRunQuery):


    def __init__(self, oauth_token, query_text, workspace_id):
        super().__init__(oauth_token, query_text, workspace_id)