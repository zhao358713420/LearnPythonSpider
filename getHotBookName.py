#-*- coding: utf-8 -*-
import re
import urllib
import requests
# import chardet

#下载网页
def getHtml(url):
    html1 = urllib.urlopen(url)
    html = html1.read()
    # html = requests.get(url)
    return html


#获取书名
def getName(html):
    bookName = re.findall('<div class="title"><a href="/ebook/.*? &#39;tag&#39;}, true, \'read.douban.com\'\)\">(.*?)</a><',html,re.S)
    return bookName


#获取作者
def getAuthor(html):
    bookAuthor = re.findall('>作者</span><span class="labeled-text"><a class="author-item" href=".*?">(.*?)</a></span></span>',html,re.S)
    return bookAuthor


#获取图书类别
def getClass(html):
    classes = re.findall('类别</span><span class="labeled-text"><span itemprop="genre">(.*?)</span>',html,re.S)
    return classes


#获取简介
def getIntroduction(html):
    introduction = re.findall('</span></div><div class="article-desc-brief">(.*?)<a href=',html,re.S)
    return introduction


#获取封面
def getCover(html,bookName,j = 0):
    urlOfPic = re.findall('<img width="110px" height="164px" src="(.*?)" alt="" itemprop="image"></a></div>',html,re.S)
    for name in bookName:
        name = "、"+name + ".jpg"
        img = requests.get(urlOfPic[i],stream=True).content
        print 'downloading..' + name.decode('utf8')
        with open("c:\\douban_download\\"+str(j)+name.decode('utf8'),'wb') as jpg:
            jpg.write(img)
            j = j + 1
    return



url = "http://read.douban.com/ebooks/category/all/?sort=top&dcs=book-hot&dcm=douban&dct=read-more"
html = getHtml(url)

numOfBook = 0
for name in getName(html):
    numOfBook = numOfBook + 1
    print name.decode('utf8'),numOfBook

numOfAuthor = 0
for author in getAuthor(html):
    numOfAuthor = numOfAuthor + 1
    print author.decode('utf8'),numOfAuthor

getCover(html,getName(html))

numOfClass = 0
for BookClass in getClass(html):
        numOfClass = numOfClass + 1
        print BookClass.decode('utf8'),numOfClass

numOfIntro = 0
for BookIntroduction in getIntroduction(html):
    numOfIntro = numOfIntro + 1
    print BookIntroduction.decode('utf8'),numOfIntro

