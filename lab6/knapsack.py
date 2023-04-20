#knapsack using heuristic
#tushar panjeta

items =[[10,1000],
        [100,2000],
        [300,4000],
        [1,5000],
        [200,5000],]

max_weight=400

h=[] #taking heuristic valueas cost/weight
for i in range(len(items)):
    a=items[i][1]/items[i][0]
    h.append(a)

print("heuristics :",h)

sorted_items= [x for _,x in sorted(zip(h,items),reverse=True)]
# print(sorted_items)
max_cost=0

for w,c in sorted_items:
    if(w<=max_weight):
        max_cost+=c
        max_weight-=w

print("Maximum cost of material in bag :",max_cost)

