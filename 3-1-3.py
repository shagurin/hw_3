n=int(input("Введите число: ")) 
n_str = str(n)
n_list=[]
x=1
for i in range (0, len(n_str), x):
  n_list.append(int(n_str[i:i+x]))
print("Сумма", sum(n_list))
