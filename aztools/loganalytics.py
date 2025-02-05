from aztools.azmonitor import AzMonitorRunQuery


class LogAnalyticsRunQuery(AzMonitorRunQuery):


    def __init__(self, la_oauth_token, query_text, workspace_id):
        super().__init__(la_oauth_token, query_text, workspace_id)