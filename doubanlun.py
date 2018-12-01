import urllib.request
from bs4 import BeautifulSoup
from urllib import request
import re
import time
from urllib.error import HTTPError
from wordcloud import WordCloud
import requests
import sys
f=False
userll=[]
head = {}
number=0
page=0
'''
headll=['Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11','Opera/9.25 (Windows NT 5.1; U; en)','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)','Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12','Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',"Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7","Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 ",]
head['User-Agent'] = random.choice(headll)
'''
header = {
        'user-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language':'en-US,en;q=0.5',
        'Accept-Encoding':'gzip,deflate,br',
        'Connetion':'keep-alive'
        }
def openurl(ol):
    data = {}
    data['source'] = None
    data['form_email']='15976346512'
    data['from_password']='20102asd'
    data['redir']='https://www.douban.com'
    s = requests.Session()
    html =s.post(ol,data).text
    #print(html)
    return html

def user(url):
    global page
    htmlread=openurl(url)
    bshtml=BeautifulSoup(htmlread,'lxml')
    if page==0:
        myfind=bshtml.findAll('div',{'id':'hot-comments'})
        myfind2=myfind[0].findAll('span',{'class':"short"})
        #print(myfind2)
        for kk in myfind2:
                print(kk.string)
                userll.append(kk.string)
    else:
        myfind3=bshtml.findAll('div',{'class':'mod-bd'})
        myfind4=myfind3[0].findAll('span',{'class':"short"})
        #print(myfind4)
        #print('.................................................'*4)
        for y in myfind4:
                print(y.string)
                userll.append(y.string)
def getmore():
    #打开更多短评
    global page
    global number
    while page<10:
        if page==0:
            user(url1)
        else:
            urlmore=url1+'comments?start='+str(number)+'&limit=20&sort=new_score&status=P'
            user(urlmore)
            print(urlmore)
            number +=20
        page+=1
def short(li):
    li2=set(li)
    li3=list(li2)
    return li3
def savetxt(name,lis):
    name2=name+'.txt'
    with open(name2,'w',encoding='utf-8') as g:
            for i in lis:
                g.write(i)
def word(name):
    name2=name+'.txt'
    with open(name2 ,'r',encoding='utf-8')as file:
        #1.读取文本内容
        text=file.read()
        #2.设置词云的背景颜色、宽高、字数
        wordcloud=WordCloud(font_path="C:/Windows/Fonts/simhei.ttf",
        background_color="black",width=600,
        height=300,max_words=50).generate(text)
        #3.生成图片
        image=wordcloud.to_image()
        #4.显示图片
        wordcloud.to_file(name+'.jpg')

url1=input('111')
openurl(url1)
getmore()
user(url1)
name1 = input('222')
savetxt(name1,userll)
word(name1)




