import urllib.request

url = 'http://www.whatismip.com.tw'

proxy_support = urllib.request.ProxyHandler({'http':'116.22.184.203:9999'})

opener = urllib.request.build_opener(proxy_support)

opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36')]


urllib.request.install_opener(opener)

reponse = urllib.request.urlopen(url)
html = response.read().decode('utf-8')

print(html)
