import requests
from requests.auth import HTTPBasicAuth


class SlsQuery:
    def __init__(self, url, auth_user='user', auth_password='password'):
        self.base_url = url
        self.api_query = '/api/v1/query'
        self.api_query_range = '/api/v1/query_range'
        self.auth = HTTPBasicAuth(auth_user, auth_password)

    def sls_query(self, query_str, start_ms, end_ms, timeout=3000):
        url = self.base_url + self.api_query
        data = {'query': query_str, 'time': end_ms / 1000, 'timeout': timeout}
        return requests.post(url, data=data, auth=self.auth).json()

    def sls_query_range(self, query_str, start_ms, end_ms, step_ms, timeout=3000):
        url = self.base_url + self.api_query_range
        step_ms = 1000 if step_ms == 0 else step_ms
        data = {'query': query_str, 'start': start_ms / 1000, 'end': end_ms / 1000, 'step': step_ms / 1000, 'timeout': timeout}
        return requests.post(url, data=data, auth=self.auth).json()

    def set_auth(self, auth_user, auth_password):
        self.auth = HTTPBasicAuth(auth_user, auth_password)


def to_number(s):
    if s.find('.') != -1:
        return float(s)
    return int(s)


def parse_data(data, read_response):
    query_result = read_response.results.add()
    for item in data['result']:
        timeseries = query_result.timeseries.add()
        for metric in item['metric']:
            timeseries.labels.add(name=metric, value=item['metric'][metric])
        if data['resultType'] != "vector":
            for ts in item['values']:
                timeseries.samples.add(value=int(ts[1]), timestamp=int(str(ts[0]).replace('.', '')))
        else:
            timeseries.samples.add(value=to_number(item['value'][1]), timestamp=to_number(str(item['value'][0]).replace('.', '')))

