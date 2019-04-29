from lxml import etree


html = etree.parse('./test.html', etree.HTMLParse())
result = html.xpath('//ul//a')
print(result)