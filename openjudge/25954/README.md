002:运算符的实现  

总时间限制: 1000ms 内存限制: 65536kB  
描述  
程序填空  

 
####
    class A:
        def __init__(self,x):
            self.x = x
    // 在此处补充你的代码
    a,b,c = map(int,input().split())
    print(isinstance(A(2),A))
    print(A(a) < A(b))
    print(A(a) >= A(c))
    print(A(a) < c)
输入  
输入三个整数a,b,c  
输出  
先输出一行True  
然后  
依次输出 a < b， a >= c , a < c 三个表达式的值(True或False)  
样例输入  
####
    2 8 5
样例输出  
####
    True
    True
    False
    True
来源  
Guo Wei  