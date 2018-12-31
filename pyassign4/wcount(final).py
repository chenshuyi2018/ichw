"""wcount.py: count words from an Internet file.

__author__ = "chenshuyi"
__pkuid__  = "1800011799"
__email__  = "1800011799@pku.edu.cn"
"""
import sys
from urllib.request import urlopen


def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """
    dic={}
    list1=lines.split()
    list2=list(set(list1))
    for i in list2:
        a=list1.count(i)
        dic[i]=a #建立字典
    list3=sorted(dic.items(),key = lambda x:x[1],reverse = True) #排序
    del list3[topn:len(list3)]
    for x,y in list3:
        print(x,y)
       
    
    pass

if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    else:
        req =Request(sys.argv[1])
        try:
            response = urlopen(req)
        except URLError as e:
            if hasattr(e,"code"):
                print (e.code)
            if hasattr(e,"reason"):
                print (e.reason)#如果出问题的解决方法
        else:
            doc.net=sys.argv[1]
            doc = urlopen(doc.net)
            docstr = doc.read()#打开文件
            lines = docstr.decode('utf-8')#转换为str
