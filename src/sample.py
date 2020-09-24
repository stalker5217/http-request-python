import requests
import json

url = 'https://nghttp2.org/httpbin'
token = 'temp'

def get():
	uri = url + '/get'
	return requests.get(uri, headers={'X-Auth-Token': token}).json()

def post():
	uri = url + '/post'
	return requests.post(uri, headers={'X-Auth-Token': token}, json={'temp' : 'temp'}).json()

def delete():
	uri = url + '/delete'
	return requests.delete(uri, headers={'X-Auth-Token': token}).json()

def put():
	uri = url + '/put'
	return requests.put(uri, headers={'X-Auth-Token': token}).json()

def patch():
	uri = url + '/patch'
	return requests.patch(uri, headers={'X-Auth-Token': token}).json()

if __name__ == '__main__':
	print(get()['url'])
	print(post()['url'])
	print(delete()['url'])
	print(put()['url'])
	print(patch()['url'])