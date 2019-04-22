#str = 'https://upload-images.jianshu.io/upload_images/68562-8cedc6f1791d0410.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/300'
#a = str.split("?")
from bs4 import BeautifulSoup
# import re

# def replaceAll(txt,old,new):
#     pattern = re.compile(old)
#     a = pattern.sub(new,txt)
#     return a

# # a = str.replace(pattern,'https')
# print(replaceAll('http://baidu.com abc http://baidu.com','http://baidu.com','https://baidu.com'))


htm = '<span href="https://www.yinwang.org/main.css" style="font-family: Arial, Helvetica, sans-serif; background-color: rgb(255, 255, 255);">怎么办嘛</span> '
content = BeautifulSoup(htm,"html5lib")
links = content.findAll('span')
for link in links:
    href = link.get('href')
    link['href'] = href.replace('https://www.yinwang.org/main.css','css/main.css')
    
print(links)