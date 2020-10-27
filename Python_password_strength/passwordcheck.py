import requests
import hashlib
def check(query):
	url=requests.get('https://api.pwnedpasswords.com/range/' + query)
	return url

def check_hack(res,last):
	count=0
	hashes=(line.split(':') for line in res.text.splitlines())
	for hashed,count in hashes:
		if hashed==last:
			return count

def sha1(data):
	password=hashlib.sha1(data.encode('UTF-8')).hexdigest().upper()
	first,last=password[:5],password[5:]
	res=check(first)
	count=check_hack(res,last)
	print(count)
	if count==0:
		print('all fine')
	else:
		print(f'your password has been hacked {count} times')
sha1('hello')