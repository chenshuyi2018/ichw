currency_from=input()
currency_to=input()
amount_from=input()
def exchange(currency_from, currency_to, amount_from):#原货币，新货币，原货币的数目
    from urllib.request import urlopen
    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='+currency_from+'&to='+currency_to+'&amt='+amount_from)#从网站获取数据
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    j_str=jstr.split(':')
    if j_str[-2]==' false, "error" ':
        moneynumber="invalid"
    else:
        w=j_str[2].split('"')#我在这里想方设法地切割，试图取出数字，应该没有出错，虽然蠢得要死
        print(w)
        a_str=w[1].split()
        print(a_str)
        moneynumber=float(a_str[0])#必须是浮点数
        return moneynumber
print( exchange(currency_from, currency_to, amount_from))

#测试函数
def test_exchange():
    assert(exchange(USD, EUR, 2.5) == 2.1589225)  
if  exchange(USD, EUR, 2.5) == 2.1589225:
    print("Test Pass")
else:
    print("You fail")
