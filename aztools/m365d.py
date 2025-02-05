import requests
import pandas as pd
import datetime


class XdrRunAhtQuery:


    def __init__(self, graph_oauth_token, query_text):

        # parameters
        self.oath_token = graph_oauth_token
        self.query_text = query_text

        # attributes
        self.query_json = {"Query": self.query_text}
        self.request_url = 'https://graph.microsoft.com/v1.0/security/runHuntingQuery'
        self.request_headers = {
            'Authorization': f'Bearer {self.oath_token}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        self.response_json = requests.request('POST',
                                              self.request_url,
                                              headers=self.request_headers,
                                              json=self.query_json).json()
        self.pull_date = datetime.datetime.now()
        self.response_df = self._to_df()


    def _to_df(self):
        if 'results' in self.response_json:
            adh_df = pd.DataFrame.from_dict(self.response_json['results'])
        else:
            adh_df = pd.DataFrame.from_dict(self.response_json['error'])

        return adh_df


class XdrListCustomRules:


    def __init__(self, graph_oauth_token):

        # parameter
        self.oath_token = graph_oauth_token

        # attributes
        self.request_url = 'https://graph.microsoft.com/beta/security/rules/detectionRules'
        self.request_headers = {
            'Authorization': f'Bearer {self.oath_token}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        self.response_json = requests.request('GET',
                                              self.request_url,
                                              headers=self.request_headers).json()
        self.pull_date = datetime.datetime.now()
        self.flat_retained = self._flat_retained()
        self.flat_renamed = self._flat_renamed()


    def _flat_retained(self):
        df1 = pd.DataFrame(self.response_json)
        df1 = pd.concat([df1, df1['value'].apply(pd.Series)], axis=1)
        df1 = pd.concat([df1, df1['queryCondition'].apply(pd.Series)], axis=1)
        df1 = pd.concat([df1, df1['schedule'].apply(pd.Series)], axis=1)
        df1 = pd.concat([df1, df1['lastRunDetails'].apply(pd.Series)], axis=1)
        df1 = pd.concat([df1, df1['detectionAction'].apply(pd.Series)], axis=1)
        df1 = pd.concat([df1, df1['alertTemplate'].apply(pd.Series)], axis=1)


        return df1


    def _flat_renamed(self):
        df1 = pd.DataFrame(self.response_json)
        df1['rule_dump_date'] = datetime.datetime.now(datetime.timezone.utc)
        df1 = pd.concat([df1, df1['value'].apply(pd.Series)], axis=1)
        df1.rename(columns={'detectorId': 'rule_uuid',
                            'id': 'rule_id',
                            'displayName': 'rule_name',
                            'isEnabled': 'enabled',
                            'createdBy': 'created_by',
                            'createdDateTime': 'created_date',
                            'lastModifiedDateTime': 'last_modified_date',
                            'lastModifiedBy': 'last_modified_by',
                            }, inplace=True)
        df1 = df1.drop('value', axis=1)
        df1 = pd.concat([df1, df1['queryCondition'].apply(pd.Series)], axis=1)
        df1.rename(columns={'queryText': 'query',
                            'lastModifiedDateTime': 'query_last_modified_date'
                            }, inplace=True)
        df1 = df1.drop('queryCondition', axis=1)
        df1 = pd.concat([df1, df1['schedule'].apply(pd.Series)], axis=1)
        df1.rename(columns={'period': 'run_every',
                           'nextRunDateTime': 'next_run'
                           }, inplace=True)
        df1 = df1.drop('schedule', axis=1)
        df1 = pd.concat([df1, df1['lastRunDetails'].apply(pd.Series)], axis=1)
        df1.rename(columns={'lastRunDateTime': 'last_run',
                            'status': 'last_run_status',
                            'failureReason': 'failure_reason',
                            'errorCode': 'failure_code'
                            }, inplace=True)
        df1 = df1.drop('lastRunDetails', axis=1)
        df1 = pd.concat([df1, df1['detectionAction'].apply(pd.Series)], axis=1)
        df1.rename(columns={'organizationalScope': 'deployed_to',
                            'responseActions': 'alert_action'
                            }, inplace=True)
        df1 = df1.drop('detectionAction', axis=1)
        df1 = pd.concat([df1, df1['alertTemplate'].apply(pd.Series)], axis=1)
        df1.rename(columns={'title': 'alert_name',
                            'recommendedActions': 'recommendations',
                            'mitreTechniques': 'mitre_technique'
                            }, inplace=True)
        df1 = df1.drop('alertTemplate', axis=1)
        df1.rename(columns={'impactedAssets': 'entity_map',
                            '@odata.context': 'odata_context'
                            }, inplace=True)

        return df1


