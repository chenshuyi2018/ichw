#第二项作业
##为什么证明停机问题，证明方法及数学原理
停机问题是第三次数学危机的解决方案
证明方法：假设有一个图灵机C，它的作用是copy自身，即对输入m，得到(m,m)。又构造另一个图灵机D，对于D，如果带子上1的个数大于1就停机，否则不停机。构造一个函数h，h(x,y)=1 如果图灵机Mx在y上停机，否则h(x,y)=2。第一步我们将C和h联合起来得到图灵机G(G的作用可以看成对于输入m，得到h(m,m)，即Mm在m上停机时输出1，否则输出2);第二步将G和D联合起来得到M，编号为m。根据上面的构造可知，Mm在m上停机，当且仅当Mm在m上不停机，矛盾，所以得证。

##二进制补码原理
最初使用的是二进制反，第一位表示正负，后面是原码逐一取反
因为二进制反码的与负数有关的计算会面临两个零的问题，为了解决这个问题，引入补码运算
######补码运算
如何表示负数：假设一个八位的二进制补码（-128~127）
0000 0000表示唯一的零
1000 0000表示-128（其实是加一后溢出的）
要使一个正数取其负数，只需要将其所有数字取反后加一（简单一些可以是留下最后一个1，剩下的全部取反）

######浮点
±0：0 0000000 00000000
1： 0 0111111 11111111
-1: 1 0111111 11111111
正无穷：0 1111111 00000000
负无穷：1 1111111 00000000
最小非规范化数：* 0000000 00000001
最大非规范化数：* 1111110 11111111
最大规范化数浮点数：0 1111110 11111111
最小规范化数浮点数：1 1111110 11111111
NaN：0 1111111 11111111
     1 1111111 11111111
