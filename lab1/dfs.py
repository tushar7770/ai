#Depth First Search
#cs20b1098 tushar panjeta

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph=defaultdict(list)

    def addedge(self,u,v):
        self.graph[u].append(v)

    def dfs_rec(self,startingNode,visited=[]):
        visited+=[startingNode]
        for neigbhour in self.graph[startingNode]:
            if neigbhour not in visited:
                visited = self.dfs_rec(neigbhour,visited)

        return visited

    def dfs_ite(self,startingNode):
        stack=[startingNode]
        visited=[]
        
        while(stack):
            vertex=stack.pop()
            if vertex in visited:
                continue
            visited.append(vertex)
            for neigbhour in self.graph[vertex]:
                stack.append(neigbhour)

        return visited




g=Graph()
n=int(input("Enter no of edges : "))
c=0
while(n):
    print("\n==Edge",c+1,"==")
    x=int(input("\nnode1 : "))
    y=int(input("\nnode2 : "))
    g.addedge(x,y)
    g.addedge(y,x)
    n=n-1
    c=c+1
start=int(input("\nEnter the starting node :"))
print("DFS_Recursive=> ")
print(g.dfs_rec(start))

print("\nDFS_NonRecursive==> ")
print(g.dfs_ite(start))

queue=[]
queue.append(start)
for i in range(len(dict(g.graph.items()))):
    g.dfs_rec(start)
# print(dict(g.graph.items()))
