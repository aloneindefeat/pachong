from urllib.request import *  #导入所有的request，urllib相当于一个文件夹，用到它里面的方法request
# from lxml import etree  #调用包
# import pickle #
# import time
# arr = []       #定义一个空数组，用来添加爬出的数据
# url = "https://movie.douban.com/top250?start="   #豆瓣top250网址
# urls = [ url+str(i) for i in range(0,250,25)] #每次步进值25，总共250个，爬取十次
# def aa(link):    #定义一个函数aa
#     time.sleep(1)  #间隔一秒
#     print("正在爬取:%s"%link)   #提示信息可以实时看到爬取信息
#     with urlopen(link) as html:  #在html中打开爬取的数据
#         text = html.read().decode("utf-8")# 读取并且解码数据
#     doc = etree.HTML(text)       #解析html  etree这是lxml中的方法
#     #分别爬取电影名字titles、详细信息news、评分grade、最佳评论comment、网址links
#     titles = doc.xpath("//ol[@class='grid_view']/li/div[@class='item']/div[@class='info']/div[@class='hd']/a/span[1]/text()")
# #     # news= doc.xpath("//ol[@class='grid_view']/li/div[@class='item']/div[@class='info']/div[@class='bd']/p/text()")
# #     # grade= doc.xpath("//ol[@class='grid_view']/li/div[@class='item']/div[@class='info']/div[@class='bd']/div[@class='star']/span[@class='rating_num']/text()")
# #     # comment= doc.xpath("//ol[@class='grid_view']/li/div[@class='item']/div[@class='info']/div[@class='bd']/p[@class='quote']/span[@class='inq']/text()")
#     links = doc.xpath("//ol[@class='grid_view']/li/div[@class='item']/div[@class='info']/div[@class='hd']/a/@href")
#     arr.append(list(zip(titles,links))) #用append方法将爬取数据添加到数组arr
# for link in urls: #遍历十页urls
#     aa(link)   #调用
# with open("豆瓣电影完整版.txt",'wb') as f: #打开本地文件“豆瓣电影.txt”以写的方式，二进制
#     pickle.dump(arr,f)     #pickle包
# with open("豆瓣电影完整版.txt",'rb') as f:
#     obj = pickle.load(f)    #加载
# for item in obj:
#     print(item)
# import xlwt#（写入）
# wb=xlwt.Workbook()  #创建表格对象
# ws=wb.add_sheet("豆瓣电影完整版")
# with open("豆瓣电影完整版.txt",'rb') as f:
#     arr6=pickle.load(f)
# index=0
# for arr7 in arr6:
#     for title,links in arr7:
#         #序号
#         ws.write(index,0,index+1)
#         # title
#         ws.write(index,1,title)
#         ws.write(index,2,links)
#         index+=1
# wb.save("豆瓣电影完整版.xls")
#爬取里面的详细信息
# from urllib.request import *
from fake_useragent import UserAgent #代理
import pickle
from lxml.etree import *
import pickle,fake_useragent
with open('豆瓣电影完整版.txt','rb') as f:
    arr = pickle.load(f)
lists = []
for arr1 in arr:
    for title,url in arr1:
        lists.append(url)
ua =fake_useragent.UserAgent()
header = {
    'User-Agent':ua.random
}
def spider(url):
    req = Request(url,headers=header)
    with urlopen(req) as html:
        text = html.read().decode()
    doc =HTML(text)
    # 导演
    pl1 = doc.xpath("//div[@id='info']/span[1]/span[@class='attrs']/a[1]/text()")
    # 编剧
    pl2 = doc.xpath("//div[@id='info']/span[2]/span[@class='attrs']/a/text()")
    # 主演
    pl3 = doc.xpath("//div[@id='info']/span[3]/span[@class='attrs']/a/text()")
    # 类型
    pl4 = doc.xpath("//div[@id='info']/span[@property='v:genre']/text()")
    # 剧情简介
    # pl5 = doc.xpath("//span[@property='v:summary']/text()")[0].strip()
    lists.append(list(zip(pl1, pl2,pl3,pl4)))  # 用append方法将爬取数据添加到数组arr
    print(lists)
for url in lists:
    mm=spider(url)
    print(mm)

with open("电影详细信息.txt",'wb') as f: #打开本地文件“豆瓣电影.txt”以写的方式，二进制
    pickle.dump(lists,f)     #pickle包
with open("电影详细信息.txt",'rb') as f:
    obj = pickle.load(f)    #加载
for item in obj:
    print(item)
import xlwt#（写入）
wb=xlwt.Workbook()  #创建表格对象
ws=wb.add_sheet("豆瓣电影完整版详细信息")
with open("豆瓣电影完整版.txt",'rb') as f:
    arr6=pickle.load(f)
index=0
for arr7 in arr6:
    for pl1,pl2,pl3,pl4 in arr7:
        #序号
        ws.write(index,0,index+1)
        # title
        ws.write(index,1,pl1)
        ws.write(index,2,pl2)
        ws.write(index,3,pl3)
        ws.write(index,4,pl4)
        index+=1

wb.save("豆瓣电影完整版详细信息.xls")