# # WHILE CIKLUSSAL:
def pozitiv(n):
        li=[]
        i = 1
        while i * i <= n:
            j = 1
            while (j * j <= n):
                if (i * i + j * j == n):
                    li.append(i**2)
                    li.append(j**2)
                    return li
                j = j + 1
            i = i + 1
        return False
# WHILE MAIN:
n=5
print(pozitiv(n))

# # FOR CIKLUSSAL:
# def pozitiv(n):
#     li=[]
#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             if (i*i+j*j==n):
#                 li.insert(i**2,j**2)
#                 li.sort()
#     return li
# # FOR MAIN:
# n=5
# print(pozitiv(n))
