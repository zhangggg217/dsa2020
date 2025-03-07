#8211 0190
#这个题明显是错的，25.133*2>pi*4**2
'''from math import pi

def V(r):
	a=pi*r**2
	return a
N,F=map(int,input().split())
pies=[]
radium=list(map(int,input().split()))
for r in radium:
	size=V(r)
	pies.append(int(size*1000))
print(pies)
right=max(pies)+1
left=0
def f(x):
	s=0
	for i in range(N):
		size=pies[i]
		s+=(size//x)
	return s
while left<right:
	mid=(left+right+1)//2
	if f(mid)<F+1:
		right=mid-1
	else:
		left=mid
print(left/1000,f(left))'''



'''#8210 0200

L,N,M=map(int,input().split())
distance=[]
for _ in range(N):
	distance.append(int(input()))

def possibe_distance(d,min_stones):
	count=0
	curr_distance=0

	i=0
	while i <=N-1:

		if distance[i]>=curr_distance+d and L-distance[i]>=d:
			count+=1
			curr_distance=distance[i]
			
			i+=1
		else:
			i+=1
			
	if count>=min_stones:
		return True
left=1
right=L
min_stones=N-M
while left<right:
	mid=(left+right+1)//2

	if not possibe_distance(mid,min_stones):
		right=mid-1
	else:
		left=mid
print(left)'''


#66 0120
#非常奇怪的二分查找。下面代码不对
'''N,K=map(int,input().split())
cable=[]
for _ in range(N):
	x=float(input())
	cable.append(int(x*100))
def can_divied(x):
	s=0
	for length in cable:
		s+=length//x
	return s
if sum(cable)<K:
	print(0.00)
else:
	left=1
	right=max(cable)+1
	while left<=right:
		mid=left+(right-left)//2
		s=can_divied(mid)
		
		if s>=K:
			left=mid+1
			ans=mid
		else:
			right=mid-1
	print(f'{ans/100:.2f}')'''

# 0210 2442 memory limit excess
'''n=int(input())
A,B,C,D=[],[],[],[]
for _ in range(n):
	a,b,c,d=map(int,input().split())
	A.append(a)
	B.append(b)
	C.append(c)
	D.append(d)
dict={}
for i in range(n):
	for j in range(n):
		s=A[i]+B[j]
		lst=dict.get(s,[0,0])
		lst[0]+=1
		dict[s]=lst
for i in range(n):
	for j in range(n):
		s=-(C[i]+D[j])
		if s in dict:
			lst=dict[s]
			lst[1]+=1
			dict[s]=lst
ans=0
for key in dict:
	ans+=dict[key][0]*dict[key][1]
print(ans)'''
# 0220 12067 不会做
'''statistics={}
while True:
	n,k=map(int,input().split())
	if n==0 and k==0:
		break
	else:
		scores=[]
		
		
		correct=list(map(int,input().split()))
		total=list(map(int,input().split()))
		scores.append(correct)
		scores.append(total)
		statistics[(n,k)]=scores

for (n,k),scores in statistics.items():
	proportion=[(scores[0][i]/scores[1][i],i) for i in range(n)]
	proportion=sorted(proportion,key=lambda x:x[0])
	a=0
	b=0
	for i in range(k,n):
		ind=proportion[i][1]
		a+=scores[0][ind]
		b+=scores[1][ind]
	print(int(100*a/b))'''

#0230 22007 N皇后 accepted
'''def is_safe(board, row, col):
	# 检查当前位置是否安全
	# 检查同一列是否有皇后
	for i in range(row):
		if board[i] == col:
			return False
	# 检查左上方是否有皇后
	i = row - 1
	j = col - 1
	while i >= 0 and j >= 0:
		if board[i] == j:
			return False
		i -= 1
		j -= 1
	# 检查右上方是否有皇后
	i = row - 1
	j = col + 1
	while i >= 0 and j < N:
		if board[i] == j:
			return False
		i -= 1
		j += 1
	return True

def queen_dfs(board, row):
	if row == N:
		# 找到第b个解，将解存储到result列表中
		ans.append(''.join([str(x) for x in board]))
		return
	for col in range(N):
		if is_safe(board, row, col):
			# 当前位置安全，放置皇后
			board[row] = col
			# 继续递归放置下一行的皇后
			queen_dfs(board, row + 1)
			# 回溯，撤销当前位置的皇后,可有可无
			board[row]=0
N=int(input())
ans=[]
queen_dfs([0]*N,0)
if ans !=[]:
	for nums in ans:
		print(' '.join(nums))
else:
	 print("NO ANSWER")'''

#0240 1750 accepted 注意用递归的方法自己实现
'''def permutation(arr):
	if len(arr)==1:
		return [arr]
	else:
		result=[]
		n=len(arr)
		for i in range(n):
			curr=arr[i]
			rema=arr[:i]+arr[i+1:]
			for s in permutation(rema):
				result.append(curr+''.join(s))
		return result
s=input()
arr=list(s)
arr.sort()
result=permutation(arr)
for x in result:
	print(''.join(x))'''

#0250 1696 波兰表达式 没有给出答案应该取多少位，学习算法就好
'''def evaluate_polish(expression):
	stack = []
	operators = {'+', '-', '*', '/'}

	# 将表达式按空格分割并反转，方便从右向左处理
	tokens = expression.split()[::-1]

	for token in tokens:
		if token not in operators:
			# 如果是操作数，直接入栈
			stack.append(float(token))
		else:
			# 如果是运算符，弹出栈顶的两个操作数
			operand1 = stack.pop()
			operand2 = stack.pop()
			# 根据运算符进行计算，并将结果压入栈
			if token == '+':
				stack.append(operand1 + operand2)
			elif token == '-':
				stack.append(operand1 - operand2)
			elif token == '*':
				stack.append(operand1 * operand2)
			elif token == '/':
				stack.append(operand1 / operand2)

	# 最终栈中只剩下一个元素，即为表达式的值
	return stack[0]

# 测试用例
expression = input()
result = evaluate_polish(expression)
print(result)'''


#0260 22799 accepted 略
'''def f(n):
	if n==1:
		return 1
	if n==2:
		return 2
	else:
		return f(n-1)+f(n-2)
n=int(input())
print(f(n))'''
			
#0280 666 注意这个递归，比较巧妙，没做出来
# 递归思想 accepted
'''def put_apple(m, n):
	if m < 0 or n < 0:
		return -1
	if n == 1 or m == 0:
		return 1
	# 如果 苹果数量m 小于 盘子数量n,相当于 把m个苹果放到 m个盘子里
	elif m < n:
		return put_apple(m, m)
	# 如果 m >= n, 递归思想，等于有一个空盘子的放法，加上没有空盘的放法
	# 即 p(m,n) = p(m,n-1) + p(m-n,n)
	elif m >= n:
		return put_apple(m, n - 1) + put_apple(m - n, n)
t=int(input())
for _ in range(t):
	m,n=map(int,input().split())
	print(put_apple(m, n))#m个苹果 n个盘子'''

#0290 23660
#itertools的应用
'''from itertools import combinations


t=int(input())

for _ in range(t):
	count=0
	dict={i:0 for i in range(7)}
	l,nums=input().split(' ',maxsplit=1)
	lst=list(map(int,nums.split()))
	for i in range(int(l)+1):
		gen=combinations(lst,i)
		for tup in gen:
			if sum(tup)%7==0:
				count+=1
	print(count)'''

#0300 7622
#注意归并排序算法 nlogn accepted
'''def merge_sort_and_count(arr):
	if len(arr) <= 1:
		return arr, 0
	mid = len(arr) // 2
	left, left_inv = merge_sort_and_count(arr[:mid])
	right, right_inv = merge_sort_and_count(arr[mid:])
	merged, split_inv = merge_and_count(left, right)
	return merged, left_inv + right_inv + split_inv

def merge_and_count(left, right):
	result = []
	inv_count = 0
	i = j = 0
	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
			inv_count += len(left) - i  # 因为left[i:]的所有元素都比right[j]大
	result.extend(left[i:])
	result.extend(right[j:])
	return result, inv_count

# 测试代码
n=int(input())
arr = list(map(int,input().split()))
sorted_arr, total_inv_count = merge_sort_and_count(arr)

print(total_inv_count)'''

#0310 22006 accepted
'''dic={0:'A',1:'B',2:'C'}
def operations(n,i,j):
	if n==1:
		print(dic[i]+'->'+dic[j])
		return
	else:
		k=3-i-j
		operations(n-1,i,k)
		print(dic[i]+'->'+dic[j])
		operations(n-1,k,j)
n=int(input())
operations(n,0,2)'''

#0320 24681 accepted 水题略
'''def f(n):
	if n<0:
		return 0
	elif n==0:
		return 1
	else:
		return f(n-1)+f(n-3)+f(n-5)
n=int(input())
print(f(n))'''

#0330 23937
#BFS做法
'''from collections import deque
N=int(input())
map=[list(map(int,input().split())) for _ in range(N)]
movement=[(1,0),(0,1)]
visited=set()
def legal(step):
	i,j=step
	if 0<=i<=N-1 and 0<=j<=N-1 and map[i][j]!=1 and step not in visited:
		return True
	else:
		return False
def bfs(map):
	queue=deque()
	start=(0,0)
	queue.append(start)
	visited.add(start)
	while queue:
		position=queue.popleft()
		if position==(N-1,N-1):
			return "Yes"
		for move in movement:
			dx,dy=move
			x,y=position
			next_step=(x+dx,y+dy)
			if legal(next_step):
				queue.append(next_step)
				visited.add(next_step)
			
	else:
		return "No"
result=bfs(map)
print(result)'''
#DFS方法
'''N=int(input())
map=[list(map(int,input().split())) for _ in range(N)]
movement=[(1,0),(0,1)]
visited=[[0]*N for _ in range(N)]
def legal(step):
	i,j=step
	if 0<=i<=N-1 and 0<=j<=N-1 and map[i][j]!=1 and not visited[i][j]:
		return True
	else:
		return False
def dfs(map,x,y):
	for move in movement:
		dx,dy=move
		next_step=(x+dx,y+dy)
		if next_step==(N-1,N-1):
			return 'Yes'
		else:
			if legal(next_step):
				visited[x][y]=1
				result=dfs(map,x+dx,y+dy)
				if result=="Yes":
					return "Yes"
				visited[x][y]=0
result=dfs(map,0,0)
if result:
	print(result)
else:
	print('No')'''

