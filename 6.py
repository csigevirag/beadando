# LEFUT,DE NEM CSAK AZOK A SZÁMOK VANNAK BENNE
def kisebb(n):
    n=int(input("Adjon meg egy 1000-nél kisebb számot:"))
    s=0
    t=[0,4,7]
    d=[1,2,3,5,6,8,9]
    if int(n)<=1000:
        for num in range(0,n+1):
            nu=map(int,str(num))
            for m in nu:
                if (m in t) and (m not in d):
                    s+=1
        return s
    else:
        "1000-nél nagyobb számot adott meg!"
n=3
print(kisebb(n))
