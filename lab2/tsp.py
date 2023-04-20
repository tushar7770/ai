# travelling sales person problem
# cs20b1098 tushar panjeta

import numpy as np
# n=int(input("Enter the no of cities :"))
# print("Enter the matrix : ")
# ad_mat=[]
# for i in range(n):
#     l=[]
#     for j in range(n):
#         a=int(input())
#         l.append(a)
#     ad_mat.append(l)
n=4
ad_mat=[[ 0, 10, 15, 20],
        [ 5 , 0 , 9 ,10],
        [ 6 ,13 , 0 ,12],
        [ 8 , 8  ,9 , 0]]

print("Adjacency Matrix :\n",np.array(ad_mat))
visited=(1<<n)-1
dp=[[-1]*n]*pow(2,n)

def tsp(visit,loc):
    if(visit==visited):
        return(ad_mat[loc][0])#change here according to starting poistion

    if(dp[visit][loc]!=-1):#if already calculated no need to find again
        return dp[visit][loc]
    
    min_dist=99999
    for i in range(n):
        if((visit & 1<<i) == 0):
            dist=ad_mat[loc][i]+tsp((visit | 1<<i), i)
            min_dist=min(min_dist,dist)
    dp[visit][loc]=min_dist

    return dp[visit][loc]

#starting from postion 0 and visit=0001
print("\nMin distance sales man has to travel =",tsp(1,0))




