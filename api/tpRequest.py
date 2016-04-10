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
