from random import randint
n=5
m=[[randint(0, 100) for i in range(n)] for j in range(n)]
max_list=[]
for i in range(0, len(m)):
    max_list.append(max(m[i]))
print(m)
print(max(max_list))



# print (m)
# print(max(m[1]))