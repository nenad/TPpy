from config import config
import requests
from requests.auth import HTTPBasicAuth


class TPRequest:
    def __init__(self):
        self.project_id = ""
        self.username = config.get('username')
        self.password = config.get('password')
        self.basicUrl = ""
        self.includedProperties = ['Name']

    def setBasicUrl(self, url):
        self.basicUrl = url

    def setIncludedProperties(self, properties):
        self.includedProperties = properties

    def setId(self, project_id):
        self.project_id = "/" + project_id

    def get(self, url="", return_format='json'):
        return_format = "?format=" + return_format
        properties = "&include=[" + ",".join(self.includedProperties) + "]"
        if url == "":
            url = self.basicUrl
        return requests.get(url + self.project_id + return_format + properties,
                            auth=HTTPBasicAuth(self.username, self.password))
