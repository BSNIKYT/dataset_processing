import ssl
import urllib.request

url_ = ''
while 'https://' not in url_:
    url_ = input('Enter your link >>> ')

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)
ssl._create_default_https_context = ssl._create_unverified_context

try:
    urllib.request.urlretrieve(url = url_, filename=url_.split('/')[-1])
    print('Done!')
except Exception as err:
    print(err)
    input()
