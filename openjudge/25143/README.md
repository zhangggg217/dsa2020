# P0610:求二叉树的高度和叶结点数目



------

总时间限制： 1000ms 内存限制： 65536kB

### 描述

给定一棵二叉树，求该二叉树的高度和叶子数目

二叉树高度定义：从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的结点数减1为树的高度。只有一个结点的二叉树，高度是0。

### 输入

第一行是一个整数n，表示二叉树的结点个数。二叉树结点编号从0到n-1。n <= 100
接下来有n行，依次对应二叉树的编号为0,1,2....n-1的节点。
每行有两个整数，分别表示该节点的左儿子和右儿子的编号。如果第一个（第二个）数为-1则表示没有左（右）儿子

### 输出

在一行中输出2个整数，分别表示二叉树的高度和叶子结点个数

### **样例输入**

```
3
-1 -1
0 2
-1 -1
```



### **样例输出**

```
1 2
```