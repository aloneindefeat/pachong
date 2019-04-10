# 网络爬虫爬取起点中文网完本榜小说500部
# 四步，分步操作，不易出错
#  所需要获取的数据：书名 、作者、网址、类型、主要介绍、作品信息

from urllib.request import *  #导入所有的request，urllib相当于一个文件夹，用到它里面的方法request
from lxml.etree import *  #调用包
import pickle #
import time
import pickle,fake_useragent
# 第一步，将25页起点完本榜的每部小说的名字和相对应的链接写入txt文件中

# arr=[]
# url0='https://www.qidian.com/rank/fin?page='
# urls=[ url0+str(i) for i in range(1,26)]
#
#
# def aa(link):
#     time.sleep(1)
#     print("正在爬取:%s"%link)   #提示信息可以实时看到爬取信息
#     with urlopen(link) as html:  # 在html中打开爬取的数据
#         text = html.read().decode("utf-8")# 读取并且解码数据
#         doc =HTML(text)       #解析html  etree这是lxml中的方法
#     url=doc.xpath("//div[@class='book-img-text']/ul/li/div[@class='book-mid-info']/h4/a/@href")
#     name=doc.xpath("//div[@class='book-img-text']/ul/li/div[@class='book-mid-info']/h4/a/text()")
#
#     arr.append(list(zip(name,url))) #用append方法将爬取数据添加到数组arr
# for link in urls:
#     aa(link)
# print(arr)
# with open("完本榜.txt",'wb') as f: #打开本地文件“完本榜.txt”以写的方式，二进制
#     pickle.dump(arr,f)     #pickle包


# 第二步，将每部小说链接内的作者、类型、主要介绍、作品信息分别获取到并写入txt1文件中

# with open('完本榜.txt','rb') as f:
#     arr1 = pickle.load(f)
# lists = []
# for arr2 in arr1:
#     for name,url in arr2:
#         url='https:'+url
#         lists.append(url)
#
# print(lists)
# #获取代理开始（让网站不认为你在爬取数据）
# ua = fake_useragent.UserAgent()
# header = {
#     'User-Agent':ua.random
# }
# list2 = []
# def spider(url):
#     time.sleep(1)
#     # print("正在爬取:%s"%url)   #提示信息可以实时看到爬取信息
#     req = Request(url,headers=header)
#     with urlopen(req) as html:
#         text = html.read().decode()
#     doc =HTML(text)
#     # 作者
#     pl1 = doc.xpath("//span/a[@class='writer']/text()")
#     # 类型
#     # print(pl1)
#
#     pl2 = doc.xpath("//p/a[@class='red']/text()")
#     # 主要介绍
#     # print(pl2)
#     #
#     pl3 = doc.xpath("//p[@class='intro']/text()")
#     # 作品信息
#     # print(pl3)
#     #
#     pl4 = doc.xpath("//div[@class='book-info-detail']/div[@class='book-intro']/p/text()")
#     # print(pl4)
#
#     list2.append(list(zip(pl1, pl2,pl3,pl4)))  # 用append方法将爬取数据添加到数组lists
#     print(list2)
# for url in lists:
#     mm=spider(url)
# with open("完本榜1.txt",'wb') as f: #打开本地文件“完本榜.txt”以写的方式，二进制
#     pickle.dump(list2,f)     #pickle包


# 第三步，将txt文件写入表格xls中

# import xlwt#（写入）
# wb=xlwt.Workbook()  #创建表格对象
# ws=wb.add_sheet("完本榜")
# with open("完本榜.txt",'rb') as f:
#     arr6=pickle.load(f)
# index=0
# for arr7 in arr6:
#     for name,url in arr7:
#         #序号
#         ws.write(index,0,index+1)
#         # title
#         ws.write(index,1,name)
#         ws.write(index,2,url)
#         index+=1
# wb.save("完本榜.xls")


# 第四步  将txt文件写入xls1中
import xlwt#（写入）
wb=xlwt.Workbook()  #创建表格对象
ws=wb.add_sheet("完本榜1")
with open("完本榜1.txt",'rb') as f:
    arr6=pickle.load(f)
index=0
for arr7 in arr6:
    for pl1,pl2,pl3,pl4 in arr7:
        #序号
        # ws.write(index,0,index+1)
        # title
        ws.write(index,3,pl1)
        ws.write(index,4,pl2)
        ws.write(index,5,pl3)
        ws.write(index,6,pl4)
        index+=1
wb.save("完本榜1.xls")