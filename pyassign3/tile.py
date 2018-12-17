m=int(input())
n=int(input())
a=int(input())
b=int(input())
if (m*n)%(a*b)!=0:
    print("no answer")
else:
    matrix=[([0] * m) for i in range(n)]
    print(bricks(matrix))
    
    
def conflict(matrix):#matrix 表示二维数组；status表示是零还是1
#如果砖有重合是冲突      
#可以给每个位置一个状态数值，所有铺上的都是1，没有铺上的都是零
  #只要确保每一个位置都是1（铺上后加一，可以用2表示重叠，即为矛盾）
    conflict=True
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==2:
                conflict=False
                break
        break
    return conflict
    
  #第三次大作业
#感觉上和八皇后有点相似
def bricks(matrix):#如何递归？
   #不能和之前砖重叠
   #结束时所有都铺满
    answer=[]
    answer_sum=[]
    if matrix==[([1] * m) for i in range(n)]:
        answer_sum.append(answer.copy())
    else:
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    if judge_heng(matrix,i,j)==True:
                        matrix=hengxiang(matrix,i,j)[1]
                        answer.append(hengxiang(matrix,i,j)[0])
                        bricks(matrix)
                    if judge_zong(matrix,i,j)==True:
                        matrix=zongxiang(matrix,i,j)[1]
                        answer.append(zongxiang(matrix,i,j)[0])
                        bricks(matrix)
                        
    return answer_sum
    
    
    
    
def judge_heng(matrix,i,j):
    ju=True
    if j+a>m or i+b>n:
        ju=False
        return ju
    else:
        matrix2=hengxiang(matrix,i,j)[1]
        return conflict(matrix2)
        
        
def judge_zong(matrix,i,j):
    ju=True
    if j+b>m or i+a>n:
        ju=False
        return ju
    else:
        matrix2=zongxiang(matrix,i,j)[1]
        return conflict(matrix2)
        
        
def judge_zong(matrix,i,j):
    ju=True
    if j+b>m or i+a>n:
        ju=False
        return ju
    else:
        matrix2=zongxiang(matrix,i,j)[1]
        return conflict(matrix2)
        
        
def zongxiang(matrix,i,j):
    brick=[]
    matrix1=matrix
    for x in range(i,i+a):
        for y in range(j,j+b):
            matrix1[x][y]=matrix1[x][y]+1
            k=x*m+y
            brick.append(k)
    return brick,matrix1
