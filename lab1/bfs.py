#Breadth First Search
#cs20b1098 tushar panjeta

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph=defaultdict(list)

    def addedge(self,u,v):
        self.graph[u].append(v)

    def bfs_ite(self,startingNode):
        queue=[]
        visited=[]

        queue.append(startingNode)
        visited.append(startingNode)

        while(queue):
            node=queue.pop(0)
            print(node,end=" ")
            for i in self.graph[node]:
                if i not in visited:
                    queue.append(i)
                    visited.append(i)

    def bfs_rec(self,startingNode,visited=[],queue=[]):
        visited+=[startingNode]
        for neigbhour in self.graph[startingNode]:
            if neigbhour not in visited:
                queue.append(neigbhour)
        
        if(queue):
            visited = self.bfs_rec(queue.pop(0),visited,queue)

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
print("BFS NonRecursive => ")
g.bfs_ite(start)
print("\nBFS Recursive ==> ",g.bfs_rec(start))
# print(dict(g.graph.items()))
