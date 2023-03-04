l1=[1, 2, 3, 5, "hello", 5 ,3, 11, 11, "hello"]
l2=[]

for i in range(0, len(l1)):
    if l1[i] in l1[i+1:len(l1)]:
        l2.append(l1[i])
print(l2)