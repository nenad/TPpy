import json

from configuration import config
from requests.auth import HTTPBasicAuth
import requests


class TPRequest:
    def __init__(self):
        self.entity_id = ""
        self.username = config.get('username')
        self.password = config.get('password')
        self.basicUrl = ""
        self.includedProperties = ['Name']
        if config.get_project_var('user_id') is None:
            self._set_user()

    def setBasicUrl(self, url):
        self.basicUrl = url

    def setIncludedProperties(self, properties):
        self.includedProperties = properties

    def setId(self, entity_id):
        self.entity_id = "/" + entity_id.__str__()

    def get(self, url="", return_format='json'):
        return_format = "?format=" + return_format
        properties = "&include=[" + ",".join(self.includedProperties) + "]"
        if url == "":
            url = self.basicUrl
        return requests.get(url + self.entity_id + return_format + properties,
                            auth=HTTPBasicAuth(self.username, self.password))

    def post(self, url="", data=""):
        if url == "":
            url = self.basicUrl
        if '?' in url:
            url += '&format=json'
        else:
            url += '?format=json'
        return requests.post(url, data, auth=HTTPBasicAuth(self.username, self.password))

    def _set_user(self):
        from api.tpApi import TPApi
        prev_id = self.entity_id
        prev_url = self.basicUrl
        prev_incl = self.includedProperties
        self.setId('loggeduser')
        self.setBasicUrl(TPApi().getEntityTypeURL('Users'))
        self.setIncludedProperties(['Id', 'FirstName', 'LastName'])
        response = self.get()
        data = json.loads(response.content)
        config.set_project_var('user_id', data['Id'])
        self.setBasicUrl(prev_url)
        self.entity_id = prev_id
        self.setIncludedProperties(prev_incl)
