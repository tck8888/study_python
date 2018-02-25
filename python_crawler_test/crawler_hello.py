from urllib import request
# 判断网页的编码
import chardet

'''
1. 简单爬取网页的html源代码
2. 获取网页源码
'''
url = 'http://fanyi.baidu.com'


def getHtml(url):
    page = request.urlopen(url)
    html = page.read()
    page.close()
    return html


if __name__ == '__main__':
    html = getHtml(url)
    # 获取网页的编码
    charset = chardet.detect(html)
    print(charset)
