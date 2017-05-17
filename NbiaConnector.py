class NbiaConnector:
    json = __import__('json')
    requests = __import__('requests')
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.url = 'https://dcm.bmia.nl/'
        self.token = ''
    def __connect(self):
        urlAuth = str(self.url + 'nbia-api/oauth/token')
        authData = {
            'username': self.username,
            'password': self.password,
            'client_id': 'nbiaRestAPIClient',
            'client_secret': 'ItsBetweenUAndMe',
            'grant_type': 'password'
        }
        # execute HTTP POST to try and authenticate
        resp = self.requests.post(urlAuth, data=authData)
        # parse JSON string into python dictionary
        respObj = self.json.loads(resp.text)
        self.token = respObj.get('access_token', '')
    def getSeries(self, project):
        # get series for PETRA_PETAL
        getData = {
            'Collection': project,
            'format': 'json'
        }
        if not self.token:
            self.__connect()
        headerData = {
            'Authorization': str('Bearer ' + self.token)
        }
        # perform the actual GET request
        respSeries = self.requests.get(str(self.url + 'nbia-api/services/v2/getSeries'), headers=headerData, params=getData)
        return self.json.loads(respSeries.text.encode('utf-8'))
    def getSeriesCsv(self, project):
        # get series for PETRA_PETAL
        getData = {
            'Collection': project,
            'format': 'csv'
        }
        if not self.token:
            self.__connect()
        headerData = {
            'Authorization': str('Bearer ' + self.token)
        }
        # perform the actual GET request
        respSeries = self.requests.get(str(self.url + 'nbia-api/services/v2/getSeries'), headers=headerData, params=getData)
        return respSeries.text.encode('utf-8')
    def logout(self):
        headerData = {
            'Authorization': str('Bearer ' + self.token)
        }
        # Perform logout
        self.requests.get(str(self.url + 'nbia-api/logout'), headers=headerData)
