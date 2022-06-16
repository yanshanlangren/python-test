import urllib3

response = urllib3.open('http://www.baidu.com')
html = response.read()
print(html)
