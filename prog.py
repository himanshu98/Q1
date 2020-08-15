# author: Himanshu Tomar
n,k=map(int,input().split(' '))
ans=[]
arr=[[0 for col in range(n)] for row in range(n)]
while(k!=0):
    k=k-1
    s=input()
    ans.append(s)
for i in range(0,n):
	for j in range(0,n):
		arr[i][j]=''
for k in range(0,len(ans)):
	i,j=map(int,ans[k].split(' '))
	arr[i][j]='X'
	for val in range(0,n):
		arr[i][val]='X'
	for val in range(0,n):
		arr[val][j]='X'
	count=0
	for row in range(0,n):
		for col in range(0,n):
			if(arr[row][col]==''):
				count=count+1
	print(count,end=' ')
		


