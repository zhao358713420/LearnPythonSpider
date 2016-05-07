#-*- coding: utf-8 -*-

import re
import requests

下载网页
def getHtml(url):
    html = requests.get(url)
    html = html.text()
    return html

#获取书名
def getName(html):
    bookName = re.findall('<div class="title"><a href="/ebook/.*? &#39;tag&#39;}, true, \'read.douban.com\'\)\">(.*?)</a><',html,re.S)
    return bookName

#获取作者
def getAuthor(html):
    bookAuthor = re.findall('>作者</span><span class="labeled-text"><a class="author-item" href=".*?">(.*?)</a></span></span>',html,re.S)
    return bookAuthor

#获取译者
def getTranslator(html):
    extent = re.findall('作者.*?</a></span>(.*?)类别',html,re.S)
    translatorList = []
    for matchExist in extent:
        if re.search("译者",matchExist):
            translator = re.findall('<span class="labeled-text"><a class="author-item" href=".*?">(.*?)</a>',matchExist,re.S)
        else:
            translator = '无译者'
        translatorList.append(translator)
        continue
    return translatorList


#将作者替换，方便获取译者
def replaceAuthor(html):
    replace = re.sub('>作者</span><span class="labeled-text"><a class="author-item" href=".*?</a></span></span>','123',html)
    return replace


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
    i = 0
    urlOfPic = re.findall('<img width="110px" height="164px" src="(.*?)" alt="" itemprop="image"></a></div>',html,re.S)
    for name in bookName:
        name = "、".decode('utf-8')+name + ".jpg".decode('utf-8')
        img = requests.get(urlOfPic[i],stream=True).content
        print 'downloading..' + name
        with open("c:\\douban_download\\"+str(j)+name,'wb') as jpg:
            jpg.write(img)
            i = i + 1
            j = j + 1
    return



url = "http://read.douban.com/ebooks/category/all/?sort=top&dcs=book-hot&dcm=douban&dct=read-more"
html = getHtml(url)

numOfBook = 0
for name in getName(html):
    numOfBook = numOfBook + 1
    print name,numOfBook

numOfAuthor = 0
for author in getAuthor(html):
    numOfAuthor = numOfAuthor + 1
    print author,numOfAuthor


numOfTranslator = 0
for Translator in getTranslator(html):
    numOfTranslator = numOfTranslator + 1
    if type(Translator) == list:
        for j in Translator:
            print j
        print numOfTranslator
    else:
        print Translator,numOfTranslator


html = replaceAuthor(html)

getCover(html,getName(html))

numOfClass = 0
for BookClass in getClass(html):
        numOfClass = numOfClass + 1
        print BookClass,numOfClass

numOfIntro = 0
for BookIntroduction in getIntroduction(html):
    numOfIntro = numOfIntro + 1
    print BookIntroduction,numOfIntro
