from urllib.request import urlopen, Request
try:
    url = 'https://www.blaze.com/pt/'
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})
    resposta = urlopen(req)
    status_code = resposta.getcode()
except:
    print(f'\033[0;31mNão deu de dar pra dar uma apostadinha😭😭😭\033[m')
else:
    if status_code == 200:
        print(f'\033[0;32mDeu Green!!! bora que o pai logou na 🔞💰🔥\033[4;32mBlaze\033[0;32m🔥💰🔞!!!\033[m')
