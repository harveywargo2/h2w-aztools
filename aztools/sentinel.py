from aztools.azmonitor import AzMonitorRunQuery
import requests
import datetime
import json
import pandas as pd


class SentinelRunQuery(AzMonitorRunQuery):


    def __init__(self, la_oauth_token, query_text, workspace_id):
        super().__init__(la_oauth_token, query_text, workspace_id)


class SentinelListRules:


    def __init__(self, subscription_id, resource_group, workspace, arm_auth_token, api_version='2024-09-01'):

        # parameter
        self.subscription_id = subscription_id
        self.resource_group = resource_group
        self.workspace = workspace
        self.api_version = api_version
        self.auth_token = arm_auth_token

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

        # wrangled attributes
        self.flat_retained_df = self._flat_retained()
        self.flat_renamed_df = self._flat_renamed()


    def _flat_retained(self):
        df1 = pd.DataFrame(self.response_json)
        df1 = pd.concat([df1, df1['value'].apply(pd.Series)], axis=1)
        df1 = pd.concat([df1, df1['properties'].apply(pd.Series)], axis=1)
        df1 = pd.concat([df1, df1['eventGroupingSettings'].apply(pd.Series)], axis=1)
        df1 = pd.concat([df1, df1['incidentConfiguration'].apply(pd.Series)], axis=1)
        df1 = pd.concat([df1, df1['groupingConfiguration'].apply(pd.Series)], axis=1)

        df1['rule_dump_date'] = datetime.datetime.now(datetime.timezone.utc)

        return df1


    def _flat_renamed(self):

        df1 = pd.DataFrame(self.response_json)
        df1['rule_dump_date'] = datetime.datetime.now(datetime.timezone.utc)
        df1 = pd.concat([df1, df1['value'].apply(pd.Series)], axis=1)
        df1 = df1.drop('value', axis=1)
        df1.rename(columns={'id': 'rule_path', 'name': 'rule_guid'}, inplace=True)
        df1 = pd.concat([df1, df1['properties'].apply(pd.Series)], axis=1)
        df1.rename(columns={'queryFrequency': 'run_every',
                            'queryPeriod': 'query_lookback',
                            'triggerOperator': 'trigger_operator',
                            'triggerThreshold': 'trigger_threshold'
                            }, inplace=True)
        df1 = df1.drop('properties', axis=1)
        df1.rename(columns={'customDetails': 'custom_details',
                            'entityMappings': 'entity_map',
                            'query': 'query',
                            'suppressionDuration': 'suppression_duration',
                            'suppressionEnabled': 'suppression_active',
                            'displayName': 'rule_name',
                            'enabled': 'enabled',
                            'description': 'description',
                            'alertRuleTemplateName': 'rule_template',
                            'lastModifiedUtc': 'last_modified_date',
                            'alertDetailsOverride': 'alert_details_override',
                            'eventGroupingSettings': 'event_grouping'
                            }, inplace=True)
        df1 = pd.concat([df1, df1['incidentConfiguration'].apply(pd.Series)], axis=1)
        df1.rename(columns={'createIncident': 'create_incident'
                            }, inplace=True)
        df1 = df1.drop('incidentConfiguration', axis=1)
        df1 = pd.concat([df1, df1['groupingConfiguration'].apply(pd.Series)], axis=1)
        df1.rename(columns={'enabled': 'incident_alert_groupby',
                            'reopenClosedIncident': 'incident_reopen',
                            'lookbackDuration': 'incident_groupby_time',
                            'matchingMethod': 'incident_groupby_method',
                            'groupByEntities': 'incident_groupby_entities',
                            'groupByAlertDetails': 'incident_groupby_alert_details',
                            'groupByCustomDetails': 'incident_groupby_custom_details',
                            }, inplace=True)
        df1 = df1.drop('groupingConfiguration', axis=1)

        return df1

