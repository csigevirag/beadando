import itertools

def kisebb(n):
    if int(n)<=1000:
        k=0
        for i in itertools.product([0,4,7],repeat=len(n)):
            s=''
            for j in i:
                s+=str(j)
            if int(s)<int(n):
                k+=1
        return k
    else:
        return 'Adjon meg 1000 vagy annál kisebb számot!'


print(kisebb(str(100)))

# LEFUT,DE NEM CSAK AZOK A SZÁMOK VANNAK BENNE
# def kisebb(n):
#     n=int(input("Adjon meg egy 1000-nél kisebb számot:"))
#     s=0
#     t=[0,4,7]
#     if int(n)<=1000:
#         for num in range(0,n+1):
#             nu=map(int,str(num))
#             for m in nu:
#                 if m in t:
#                     s+=1
#         return s
#
# n=3
# print(kisebb(n))