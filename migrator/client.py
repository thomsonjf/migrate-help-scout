
import json
import requests

class HelpScoutClient:

    def __init__(self, config):
        self.config = config
        self.auth = (self.config.get('api', 'key'), self.config.get('api', 'password'))

    def fetch_sites_list(self):
        url = self.config.get('api', 'baseurl') + '/sites'
        response = requests.get(url, auth=self.auth)

        if response.status_code == 200:
            return json.loads(response.content.decode('utf-8'))['sites']
        else:
            return None

    def fetch_site_collections(self, siteId):
        url = self.config.get('api', 'baseurl') + '/collections?siteId=' + str(siteId)
        print(url)
        response = requests.get(url, auth=self.auth)

        if response.status_code == 200:
            return json.loads(response.content.decode('utf-8'))['collections']
        else:
            return None



