d={"name1":"id1", "name2":"id2", "name3":"id3", "name4":"id4", "name5":"id5"}
lk=list(d.keys())
lv=list(d.values())
d1={}
for i in range(0, len(lv)):
    d1[lv[i]]=lk[i]
print(d1)