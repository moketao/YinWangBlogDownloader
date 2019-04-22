# import pdfkit
import os
from urllib.request import urlopen
import urllib
from bs4 import BeautifulSoup
import re

# 获取标题列表
def get_title_list():
    soup = urlopen('https://www.yinwang.org')
    content = BeautifulSoup(soup.read(), 'html.parser')
    title_list = []
    content_list = content.find_all('li', 'list-group-item')
    for text in content_list:
        title_list.append(text.get_text().strip())
    return title_list


# 获取所有页面url
def get_url_list():
    soup = urlopen('https://www.yinwang.org')
    content = BeautifulSoup(soup.read(), 'html.parser')
    menu_tag = content.find_all(class_='list-group-item')
    urls = []
    for li in menu_tag:
        url = "https://www.yinwang.org" + li.a.get('href')
        urls.append(url)
    return urls

# 将html页面保存到本地
def saveHtml(file_name, file_content):
    fp = open(file_name, "w+b")
    fp.write(file_content)
    fp.close()

# 将img保存到本地
def saveImg(img_url,imgDirName):
    path = os.getcwd()
    new_path = os.path.join(path, imgDirName)
    # print(path)
    # print(new_path)
    img_url_arr = img_url.split('?')
    img_url = img_url_arr[0]
    print('(',img_url,')')
    filename = os.path.basename(img_url)
    filePath = new_path +'\\' + filename
    if os.path.exists(filePath):
        print(' 文件已存在，跳过保存')
        return filename
    try:
        urllib.request.urlretrieve(img_url, filePath)
    except Exception as e:
        print(' 保存文件出错: '+img_url)
        print(e)
        return 'err'
    else:
        print('文件已保存.')
    return filename

# 替换
def replaceAll(txt,old,new):
    pattern = re.compile(old)
    a = pattern.sub(new,txt)
    return a

# 将博客转化为pdf文件
# def savePDF(url, file_name):
#     options = {
#         'page-size': 'A4',
#         'zoom':'2.5'
#     }
#     pdfkit.from_url(url, file_name, options = options)

# 将当前所有文章url保存到文件里
def saveCurrUrList(urls, filename, mode = 'a'):
    file = open(filename,mode)
    for i in range(len(urls)):
        file.write(str(urls[i] + '\n'))
    file.close()

if __name__ == '__main__':
    urls = get_title_list()
    
    start = 0
    end = len(urls)
    
    # 修改 start 和 end 的值，可局部更新。
    # start = 0
    # end = 100


    print(end)
    for i in range(start, end):
        urls = get_url_list()
        title_list = get_title_list()
        print(title_list[i])
        soup = urlopen(urls[i])
        content = BeautifulSoup(soup.read(), 'html.parser')
        menu_tag = content.find_all(class_='list-group-item')

        imgs = content.findAll('img')
        for img in imgs:
            imgurl = img.get('src')
            imgFileName = saveImg(imgurl,'html/images')
            if imgFileName!='err':
                img['src'] = 'images/'+imgFileName

        links = content.findAll('link')
        for link in links:
            href = link.get('href')
            link['href'] = href.replace('http://www.yinwang.org/main.css','css/main.css')
        
        saveHtml(os.getcwd() + '/html/' + title_list[i] + '.html', content.encode())

        # savePDF(urls[i], os.getcwd() + '/pdf/' + title_list[i] + ".pdf")




