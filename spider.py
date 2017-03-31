import requests
import re
from bs4 import BeautifulSoup
headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, compress',
           'Accept-Language': 'en-us;q=0.5,en;q=0.3',
           'Cache-Control': 'max-age=0',
           'Connection': 'keep-alive',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
url='https://www.gn00.com/'
login_url='"https://www.gn00.com/connect.php?mod=login&op=init&referer=index.php&statfrom=login_simple'
login_post_data ={
    'user.account':'username',
    'user.pwd':'password'
}
s=requests.session()
pattern="<.+>签到<.+>"
try:
    r=requests.get(url,headers)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    login_r = s.post(login_url, login_post_data)
    homepage=s.get(url)
    soup=BeautifulSoup(homepage)
    target=soup.find_all(string=re.compile(pattern))
    script=target.a['href']
    s.post(script,'today moods')
except:
    print('签到失败')