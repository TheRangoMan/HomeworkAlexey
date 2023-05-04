import requests

class ApiHandler:
    def __init__(self, base_url):
        self.base_url = base_url
    
    def get_data(self, endpoint=''):
        response = requests.get(self.base_url + endpoint)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to get data from endpoint {endpoint}. Error: {response.text}")
    
    def add_data(self, endpoint='', data={}):
        response = requests.post(self.base_url + endpoint, json=data)
        if response.status_code == 201:
            return response.json()
        else:
            raise Exception(f"Failed to add data to endpoint {endpoint}. Error: {response.text}")
    
    def delete_data(self, endpoint=''):
        response = requests.delete(self.base_url + endpoint)
        if response.status_code == 204:
            return "Data deleted successfully"
        else:
            raise Exception(f"Failed to delete data from endpoint {endpoint}. Error: {response.text}")
    
    def update_data(self, endpoint='', data={}):
        response = requests.put(self.base_url + endpoint, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to update data at endpoint {endpoint}. Error: {response.text}")
