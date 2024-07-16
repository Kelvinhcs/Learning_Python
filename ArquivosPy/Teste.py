from urllib.request import urlopen, Request
url = 'https://www.blaze.com/pt/'
req = Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})
resposta1 = urlopen(req)
resposta2 = urlopen('https://www.google.com')
status_code = resposta1.getcode()
status_code2 = resposta2.getcode()
print(f'Status Code blaze: {status_code}')
print(f'Status Code google: {status_code2}')
