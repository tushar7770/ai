# travelling sales person problem
# implement using any heuristic approach
# cs20b1098 tushar panjeta
import numpy as np
import heapq

def fisible(x,y,path):
        if x==y or (path[x]==True and path[y]==True) or (path[x]==False and path[y]==False):
                return False
        return True
def msp(g):
        l=n-1
        visited=[False]*l
        visited[0]=True
        count=0
        heuristic=0
        while(count<(l-1)):
                min=99999
                n1,n2=-1,-1
                for i in range(l):
                        for j in range(l):
                                if min>g[i][j] and  fisible(i,j,visited):
                                       n1,n2=i,j
                                       min=g[i][j]
                if n1!=-1:
                        count+=1
                        heuristic+=min
                        visited[n1],visited[n2]=True,True
        
        return heuristic

def aStar_tsp(heuristic):
    start = 0
    visited = [False] * n
    path = []
    cost = 0
    f = heuristic[start]

    data = [(f, start, visited[:], path[:], cost)]

    while data:
        f, curr, visited, path, cost = heapq.heappop(data)

        if all(visited) and curr == start:
            
            path.append(start)
            cost += ad_mat[curr][start]
            return path, cost

        for i in range(n):
            if not visited[i] and i != curr:
                g = cost + ad_mat[curr][i]#f(n) = g(n) + h(n)
                h = heuristic[i]
                f = g + h

                visited[i] = True
                new_path = path + [curr]
                heapq.heappush(data, (f, i, visited[:], new_path[:], g))
                visited[i] = False  

n=5
ad_mat=[[ 0, 12, 10, 19, 8],
        [ 12, 0 , 3 ,7, 6],
        [ 10, 3 , 0 , 2, 20],
        [ 19, 7 , 2  ,0, 4],
        [ 8, 6, 20, 4, 0]]
print("Adjacency Matrix :\n",np.array(ad_mat))
h=[]
for i in range(n):
        g=np.delete(ad_mat,i,0)
        g=np.delete(g,i,1)

        x=msp(g)
        h.append(x)
print(h)
map,min_dist = aStar_tsp(h)
print("\nMin distance sales man has to travel =",min_dist)
print("Map he need to follow : ",map)

