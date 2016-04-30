class LNDynamic:
	LNDYNAMIC_URL = 'https://dynamic.lunanode.com/api/{CATEGORY}/{ACTION}/'

	def __init__(self, api_id, api_key):
		if len(api_id) != 16:
			raise LNDAPIException('supplied api_id incorrect length, must be 16')
		if len(api_key) != 128:
			raise LNDAPIException('supplied api_key incorrect length, must be 128')

		self.api_id = api_id
		self.api_key = bytes(api_key, 'utf-8')
		self.partial_api_key = api_key[:64]

	def request(self, category, action, params = {}):
		import json
		import time
		import hmac
		import hashlib
		import requests

		url = self.LNDYNAMIC_URL.format(CATEGORY=category, ACTION=action)
		request_array = dict(params)
		request_array['api_id'] = self.api_id
		request_array['api_partialkey'] = self.partial_api_key
		request_raw = json.dumps(request_array)
		nonce = str(int(time.time()))
		handler = '{CATEGORY}/{ACTION}/'.format(CATEGORY=category, ACTION=action)
		hasher = hmac.new(self.api_key, bytes('{handler}|{raw}|{nonce}'.format(handler=handler, raw=request_raw, nonce=nonce), 'utf-8'), hashlib.sha512)
		signature = hasher.hexdigest()

		data = {'req': request_raw, 'signature': signature, 'nonce': nonce}
		content = requests.post(url, data=data).json()
		# content is now a dictionary, NOT a string
		return content

class LNDAPIException(Exception):
	pass
