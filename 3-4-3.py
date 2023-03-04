import json
import sys

login = input("Логин: ")
passwd = input ("Пароль: ")

reg = {}

def login_function(login, passwd):
    with open('reg.json', 'r') as f:
        reg=json.load(f)
    if login in reg.keys():
        if passwd==reg.get(login):
            print("Успех!")
        else: print("Неверный пароль")
    else: print("Неверный логин")

login_function(login, passwd)

