import sys

def rendezo(c):
    li=[]
    kicsi=[]
    nagy=[]
    paros=[]
    paratlan=[]
    null=[]
    egyeb=[]
    for i in c:
        li.append(i)
    for j in li:
            if "a"<=j<="z":
                kicsi.append(j)
            elif "A"<=j<="Z":
                nagy.append(j)
            elif int(j)%2==0 and int(j)!=0:
                paros.append(j)
            elif int(j)%2!=0:
                paratlan.append(j)
            elif int(j)==0:
                null.append(j)
            else:
                egyeb.append(j)
    kicsi.sort()
    nagy.sort()
    paros.sort()
    paratlan.sort()
    null.sort()
    egyeb.sort()
    x=kicsi+nagy+paros+paratlan+egyeb+null
    y=''.join(x)
    return y

print(rendezo(sys.argv[1]))