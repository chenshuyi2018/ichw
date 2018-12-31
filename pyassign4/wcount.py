#草稿版
import sys
from urllib.request import urlopen

doc = urlopen('http://www.gutenberg.org/cache/epub/19033/pg19033.txt')
docstr = doc.read()
lines = docstr.decode('utf-8')
topn=10
list1=lines.split()
list2=list(set(list1))
dic={}
for i in list2:
    a=list1.count(i)
    dic[i]=a
list3=sorted(dic.items(),key = lambda x:x[1],reverse = True) 
del list3[topn:len(list3)]
for x,y in list3:
    print(x,y)
