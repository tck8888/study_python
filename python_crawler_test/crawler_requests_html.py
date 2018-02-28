from requests_html import HTMLSession

session = HTMLSession()
r = session.get('https://python.org/')

print(r.html.links)
print(r.html.absolute_links)
# 获取css选择器的值
about = r.html.find('#about', first=True)
print(about.text)
# 属性
print(about.attrs)

print(about.html)

print(about.find('a'))

print(about.absolute_links)
