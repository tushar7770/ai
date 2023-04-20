#cs20b1098 tushar panjeta
#2 jug problem

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)


def two_jug(jug1,jug2,w):
    l=[]
    t=[0,0]
    l.append(t)
    if(w==0):
        return l

    jug1_f=jug1
    jug2_f=0
   
    t=[jug1_f,jug2_f]
    l.append(t)

    if(jug1!=w):
        while 1:
            tranfer=min(jug1_f,jug2-jug2_f)
            jug2_f=jug2_f+tranfer
            jug1_f=jug1_f-tranfer

            t=[jug1_f,jug2_f]
            l.append(t)

            if(jug1_f==w or jug2_f==w):
                break

            if jug2_f==jug2:
                jug2_f=0

                t=[jug1_f,jug2_f]
                l.append(t)

            if jug1_f==0:
                jug1_f=jug1

                t=[jug1_f,jug2_f]
                l.append(t)
    
    if(jug1_f==w and jug2_f!=0):
        t=[w,0]
        l.append(t)

    return l
   

if __name__ == '__main__':
    n=3
    m=5
    w=1

    if (w%(gcd(m,n) if m>n else gcd(n,m))) != 0 or (w>n and w>m):
        print("Not Possible")

    else:
        l1=two_jug(n,m,w)
        l2=two_jug(m,n,w)

        if len(l1)>len(l2):
            print("Jug1 capacity :",m,"\njug2 capacity :",n,"\nMinimum no of steps :",len(l2),"\nPath Followed :",l2)
        else:
            print("Jug1 capacity :",n,"\njug2 capacity :",m,"\nMinimum no of steps :",len(l1),"\nPath Followed :",l1)

