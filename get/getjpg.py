import urllib.request
import re

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.*?\.jpg)"'
    imgre = re.compile(reg)
    html = html.decode('utf-8')
    imglist = re.findall(imgre,html)
    #print(imglist)
    x = 0
    for imgurl in imglist:
        if(imgurl.find('https') == 0):
            urllib.request.urlretrieve(imgurl, '%s.jpg'%x)
            x += 1

html = getHtml("https://tieba.baidu.com/p/3379040099#!/l/p1")

print(getImg(html))