#cs20b1098 tushar panjeta
#tower of hanoi
import numpy as np
def toh_recursive(n,from_tower,to_tower,via_tower):
    if n==0:
        return

    toh_recursive(n-1,from_tower,via_tower,to_tower)
    print("\nMove disk-",n," from ",from_tower," to ",to_tower)
    toh_recursive(n-1,via_tower,to_tower,from_tower)

def toh_iterative(n,from_,to_,via_):
    if n%2==0:
        temp=to_
        to_=via_
        via_=temp

    l=np.arange(1,n+1,1)
    l=list(l)
    from_tower=l
    to_tower=[]
    via_tower=[]
    for i in range(1,pow(2,n)):
        if i%3==1:
            if to_tower==[] and from_tower!=[]:
                a=from_tower.pop(0)
                to_tower=[a]+to_tower
                print("\nMove disk-",a," from ",from_," to ",to_)
                i=i-1

            elif to_tower!=[] and from_tower!=[]:
                a=to_tower[0]
                b=from_tower[0]
                if a<b:
                    to_tower.pop(0)
                    from_tower=[a]+from_tower
                    print("\nMove disk-",a," from ",to_," to ",from_)
                
                else:
                    from_tower.pop(0)
                    to_tower=[b]+to_tower
                    print("\nMove disk-",b," from ",from_," to ",to_)
                    

            elif to_tower!=[] and from_tower==[]:
                a=to_tower.pop(0)
                from_tower=[a]+from_tower
                print("\nMove disk-",a," from ",to_," to ",from_)
        
        elif i%3==2:
            if via_tower==[] and from_tower!=[]:
                a=from_tower.pop(0)
                via_tower=[a]+via_tower
                print("\nMove disk-",a," from ",from_," to ",via_)

            elif via_tower!=[] and from_tower!=[]:
                a=via_tower[0]
                b=from_tower[0]
                if a<b:
                    via_tower.pop(0)
                    from_tower=[a]+from_tower
                    print("\nMove disk-",a," from ",via_," to ",from_)
                else:
                    from_tower.pop(0)
                    via_tower=[b]+via_tower
                    print("\nMove disk-",b," from ",from_," to ",via_)

            elif via_tower!=[] and from_tower==[]:
                a=via_tower.pop(0)
                from_tower=[a]+from_tower
                print("\nMove disk-",a," from ",via_," to ",from_)

        elif i%3==0:
            if via_tower==[] and to_tower!=[]:
                a=to_tower.pop(0)
                via_tower=[a]+via_tower
                print("\nMove disk-",a," from ",to_," to ",via_)

            elif via_tower!=[] and to_tower!=[]:
                a=via_tower[0]
                b=to_tower[0]
                if a<b:
                    via_tower.pop(0)
                    to_tower=[a]+to_tower
                    print("\nMove disk-",a," from ",via_," to ",to_)
                else:
                    to_tower.pop(0)
                    via_tower=[b]+via_tower
                    print("\nMove disk-",b," from ",to_," to ",via_)

            elif via_tower!=[] and to_tower==[]:
                a=via_tower.pop(0)
                to_tower=[a]+to_tower
                print("\nMove disk-",a," from ",via_," to ",to_)

n=3 #change n here
print("\n=====RECURSIVE APPROACH=====\n")
toh_recursive(n,'A','C','B')
print("\n=====NON RECURSIVE APPROACH=====\n")
toh_iterative(n,'A','C','B')
