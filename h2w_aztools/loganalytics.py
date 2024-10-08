from h2w_aztools.azmonitor import AzMonitorRunQuery


class LogAnalyticsRunQuery(AzMonitorRunQuery):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)