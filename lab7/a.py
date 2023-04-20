#tushar panjeta cs20b1098
'''
ASSUMPTIONS: Doing for Player "X"
INPUT: as inital state of tic tac toe (same as in sirs ppt-> oox,_x_,ox_)
ALGO: 1.)finding the space state and storing in tree
      2.)alpha beta pruning
OUTPUT: atleast score that "X" player can achieve  if opponent "O" plays best moves 
'''
import numpy as np
class Node:
    def __init__(self, state,t,l):
        self.config = state
        self.turn=t
        self.leaf=l
        self.win=0
        self.path=9
        self.child = []
        
    def update_path(self,bt):
        self.path=bt   
	

def newNode(key,t,l):   
    temp = Node(key,t,l)
    return temp

def alpha_beta_pruning(node, alpha, beta, node_type):
	
	# base case: leaf node
    if(len(node.child)==0):
        node.path=node.win
        return node.win
    
	# if this node is a max-node
    if (node_type=='x'):
        bestScore = -999
        for child in node.child:            
            childScore = alpha_beta_pruning(child,alpha,beta, 'o')
            bestScore = max(bestScore, childScore)
            alpha=max(alpha, bestScore)
            node.path=alpha
            if beta <= alpha:
                break
        return bestScore

	# if this node is a min-node
    else:
        bestScore = 999
        for child in node.child:
            childScore = alpha_beta_pruning(child, alpha,beta, 'x')
            bestScore = min(bestScore, childScore)
            beta = min(beta, bestScore)
            node.path=beta
            if beta <= alpha:
                break
        return bestScore

def display_path(root,score):
      print(root.config)
      x=len(root.child) 
      while(x):
        x-=1
        if root.child[x].path==score:
            print(root.child[x].config)
            root=root.child[x]
            x=len(root.child)
            # if(len(root.child)==0):
            #      print(root.config)

initail_state=np.array([["o","o","x"],[None,"x",None],["o","x",None]])
# print(initail_state)
win_condition=[[(0,0),(0,1),(0,2)],[(1,0),(1,1),(1,2)],[(2,0),(2,1),(2,2)],[(0,0),(1,0),(2,0)],[(0,1),(1,1),(2,1)],[(0,2),(1,2),(2,2)],[(0,0),(1,1),(2,2)],[(0,2),(1,1),(2,0)]]
l=[]
turn='x'
l.append(initail_state)
root=newNode(initail_state,turn,0)
tree=[]
tree.append(root)
while(l):
    
    p=list(zip(*np.where(l[0]==None)))
    curr_state=l.pop(0)
    curr_node=tree.pop(0)
    turn=curr_node.turn
    if curr_node.leaf==1:
        continue

    for i in range(len(p)):
        a=curr_state.copy()
        a[p[i][0]][p[i][1]]=turn
        check=set(zip(*np.where(a==turn)))
        flag=0
        for j in range(len(win_condition)):
            s=set(win_condition[j])
            if len(s-check)==0:
                flag=1
                break

        if(turn=='x'):
            curr_node.child.append(newNode(a,'o',flag))
            if(flag):
                curr_node.child[i].win=1

        else:
            curr_node.child.append(newNode(a,'x',flag))
            if(flag):
                curr_node.child[i].win=-1
              
        tree.append(curr_node.child[i])
        l=l+[a]
    
score=alpha_beta_pruning(root,-999,999,'x')
print("OPTIMAL SCORE :",score)
display_path(root,score)

