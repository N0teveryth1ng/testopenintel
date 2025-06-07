# A project for gotham by palantir [0penIntel]
from http.client import responses
from idlelib.colorizer import prog_group_name_to_tag


#                                              -------- MAIN API CODE  --------

#  load libs
import pandas as pd
import numpy as np
import requests


class APIFetcher:
    def __init__(self):
        self.api_keys = {
            'cyber': 'b7aceffb1657bfac01d8cc7563d5e91c91ee239bfe2c99e30ab1e0030ee9e4b4'
        }

        self.urls = {
            'conflict': 'https://services8.arcgis.com/xu983xJB6fIDCjpX/arcgis/rest/services/ACLED/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson',
            'cyber': 'https://otx.alienvault.com/api/v1/pulses/subscribed'
        }

    def fetch(self, name):
        headers = {}
        if name == 'cyber':
            headers['X-OTX-API-KEY'] = self.api_keys['cyber']

        try:
            response = requests.get(self.urls[name], headers=headers, timeout=10)
            response.raise_for_status()
            print(f"[INFO] Successfully fetched {name} data")
            return response.json()
        except requests.RequestException as e:
            print(f"[ERROR] Failed to fetch '{name}': {e}")
            return None

# Example Usage
fetcher = APIFetcher()
conflict_data = fetcher.fetch('conflict')
cyber_data = fetcher.fetch('cyber')



print(conflict_data.keys(), cyber_data.keys())
print()

