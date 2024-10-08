from h2w_aztools.azmonitor import AzMonitorRunQuery


class SentinelRunQuery(AzMonitorRunQuery):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)