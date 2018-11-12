import pdfkit
import os
from urllib.request import urlopen
from bs4 import BeautifulSoup


# 获取标题列表
def get_title_list():
    soup = urlopen('http://www.yinwang.org')
    content = BeautifulSoup(soup.read(), 'html.parser')
    title_list = []
    content_list = content.find_all('li', 'list-group-item')
    for text in content_list:
        title_list.append(text.get_text().strip())
    return title_list


# 获取所有页面url
def get_url_list():
    soup = urlopen('http://www.yinwang.org')
    content = BeautifulSoup(soup.read(), 'html.parser')
    menu_tag = content.find_all(class_='list-group-item')
    urls = []
    for li in menu_tag:
        url = "http://www.yinwang.org" + li.a.get('href')
        urls.append(url)
    return urls

# 将html页面保存到本地
def saveHtml(file_name, file_content):
    fp = open(file_name, "w+b")
    fp.write(file_content)
    fp.close()

# 将博客转化为pdf文件
def savePDF(url, file_name):
    options = {
        'page-size': 'A4',
        'zoom':'2.5'
    }
    pdfkit.from_url(url, file_name, options = options)

# 将当前所有文章url保存到文件里
def saveCurrUrList(urls, filename, mode = 'a'):
    file = open(filename,mode)
    for i in range(len(urls)):
        file.write(str(urls[i] + '\n'))
    file.close()

if __name__ == '__main__':
    urls = get_title_list()
    for i in range(73, 77):
        urls = get_url_list()
        title_list = get_title_list()
        print(title_list[i])
        soup = urlopen(urls[i])
        content = BeautifulSoup(soup.read(), 'html.parser')
        saveHtml(os.getcwd() + '/html/' + title_list[i] + '.html', content.encode())
        savePDF(urls[i], os.getcwd() + '/pdf/' + title_list[i] + ".pdf")




