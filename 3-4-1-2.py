import json
import sys

login = input("Логин: ")
passwd = input ("Пароль: ")

reg = {}

def register (login, passwd):
   
   with open('reg.json', 'r') as f:
    reg=json.load(f)
   if login in reg.keys():
    print("Такой пользователь уже есть")
    sys.exit()
   
   with open ('reg.json', 'w') as f: # блок для задания 1
    reg[login] = passwd
    json.dump(reg, f)
   print("Вы успешно зарегистрированы") 

register(login, passwd)