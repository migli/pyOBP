import settings as sett
import requests as req

class pyOBP:

	def __init__(self):
		pass

	def _url(self, path):
		return sett.OAUTH_API + sett.OAUTH_API_BASE_PATH + path

	def _getRequest(self, path):
		resp = req.get(self._url(path))
		if(resp.status_code != 200):
			raise ApiError('GET {} {}'.format(path, resp.status_code))
		return resp

	def _postRequest(self, path):
		pass

	def getApiRoot(self):
		resp = self._getRequest("/root")
		print('{} version {}'.format(resp.json()["hosted_by"]["organisation"] ,resp.json()["version"]))
		return resp.json()

	def getAllAccounts(self):
		resp = self._getRequest("/accounts")
		print('Number of accounts: {}'.format(len(resp.json())))
		return resp.json()


