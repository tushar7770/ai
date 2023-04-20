# travelling sales person problem
# implement using dfs,bfs,ids
# cs20b1098 tushar panjeta

import numpy as np
from collections import deque

def dfs_tsp(visit,loc,temp):
    if(visit==visited):
        return(ad_mat[loc][temp])
    
    min_dist=99999
    for i in range(n):
        if((visit & 1<<i) == 0):
            dist=ad_mat[loc][i]+dfs_tsp((visit | 1<<i), i,temp)
            min_dist=min(min_dist,dist)

    return min_dist

def bfs_tsp(start):
    min_dist=9999
    q=deque([(start,[start],0)])
    while(q):
        cur_loc,path,cost=q.popleft()
        if(len(path)==n):
            if (cost+ad_mat[cur_loc][start])<min_dist:
                min_dist=cost+ad_mat[cur_loc][start]

        for i in range(n):
            if i not in path:
                q.append((i,path+[i],(cost+ad_mat[cur_loc][i])))

    return min_dist

def ids_tsp(start):
    min_dist=99999

    def ids_dfs(visit,loc,home,curr_depth,max_depth):
        if(visit==visited and max_depth==n):
            return(ad_mat[loc][home])
        
        if(max_depth==curr_depth):
            return 0
        
        min_dist=99999
        for i in range(n):
            if((visit & 1<<i) == 0):
                dist=ad_mat[loc][i]+ids_dfs((visit | 1<<i), i,home,curr_depth+1,max_depth)
                min_dist=min(min_dist,dist)

        return min_dist

    for d in range(1,n+1):
        min_dist=ids_dfs(pow(2,start),start,start,0,d)

    return min_dist
        


n=5
visited=(1<<n)-1
ad_mat=[[ 0, 12, 10, 19, 8],
        [ 12, 0 , 3 ,7, 6],
        [ 10, 3 , 0 , 2, 20],
        [ 19, 7 , 2  ,0, 4],
        [ 8, 6, 20, 4, 0]]

print("Adjacency Matrix :\n",np.array(ad_mat))

#starting from postion 0 and visit=00001
start=0
vst=pow(2,start)
print("\nMin distance sales man has to travel using dfs =",dfs_tsp(vst,start,start))
print("\nMin distance sales man has to travel using bfs =",bfs_tsp(start))
print("\nMin distance sales man has to travel using ids =",ids_tsp(start))





