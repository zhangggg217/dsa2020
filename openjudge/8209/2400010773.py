#平凡的建树思路，空间超了
N,M=map(int,input().split())
nums=[int(input()) for _ in range(N)]
class TreeNode():
    def __init__(self,divided,index):
        self.divided=divided
        self.index=index

from collections import deque
queue=deque([TreeNode([nums[0]],0)])
minimum=10000
while queue:

    node=queue.popleft()
 

    if node.index<N-1:
        new_num=nums[node.index+1]
        tmp_divided=node.divided[:]
        tmp_divided.append(new_num)

        leftnode=TreeNode(tmp_divided,node.index+1)
        
        queue.append(leftnode)
        tmp_divided=node.divided[:]
        tmp_divided[-1]+=new_num
        rightnode=TreeNode(tmp_divided,node.index+1)
        queue.append(rightnode)
    if len(node.divided)==M and node.index==N-1:
        tmp=max(node.divided)
        minimum=min(minimum,tmp)
print(minimum)


#二分查找，注意到M小N大，我们对M二分枚举（类似于aggressive cows）

def min_max_expense(N, M, expenses):
    # 前缀和数组
    prefix_sum = [0] * (N + 1)
    for i in range(N):
        prefix_sum[i + 1] = prefix_sum[i] + expenses[i]

    # 二分查找的范围
    left, right = max(expenses), prefix_sum[-1]

    def can_split(max_expense):
        count = 1  # 当前财政周期数
        current_sum = 0  # 当前财政周期的开销
        for i in range(1, N + 1):
            current_sum += expenses[i - 1]
            if current_sum > max_expense:
                count += 1
                current_sum = expenses[i - 1]
                if count > M:
                    return False
            if i == N:
                return True
        

    # 二分查找
    while left < right:
        mid = (left + right) // 2
        if can_split(mid):
            right = mid
        else:
            left = mid + 1

    return left

# 读取输入
N, M = map(int, input().split())
expenses = [int(input()) for _ in range(N)]

# 输出结果
print(min_max_expense(N, M, expenses))