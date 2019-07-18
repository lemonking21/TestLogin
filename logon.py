import json
import re
import pprint as pprint

username =''
password = ''
accounts = []
usernameL=''
passwordL =''


def condition(x, match):
    if len(x) >= 8:
        if re.search(match, x):
                    print('Good')
                    return '1'

def get_username():
    name = input("Username must contain at least eight characters with at least one Uppercase,and one Lower case\nEnter username")
    accept = condition(name , '[a-zA-Z]')
    if accept == '1':
        set_username(name)
        print('username has been accepted')
        get_password()
    else:
        get_username()

def set_username(name):
    global username
    username = name
    print(username)

def get_password():
    
    passw = input("Password must contain at least eight characterswith at least one Uppercase, one Lower case and one Number\nEnter Password")
    accept_pas =condition(passw,'[a-zA-Z0-9]')
    if accept_pas == '1':
        set_password(passw)
        print('pass has been accepted')

def set_password(passw):
    global password
    password = passw
    print(password)

def write_write_to_file():
    global username, password

    account = { 'username': username , 'password': password , 'accountid' : '0'}

    with open('jsontest.json', 'a') as outf:
        json.dump(account,outf)
        outf.write('\n')
    print('done')

def readfromFile():
    global accounts
    with open('jsontest.json','r') as data_file:
        for x in data_file:
            accounts.append(json.loads(x))

def main():
    readfromFile()
    loggedin()

def loggedin():
    global usernameL, passwordL
    usernameL =input("Enter your username")
    passwordL =input("Enter your password") 
    check_username()


def check_password(i):
    if accounts[i]['password']==passwordL:
        return 'Good'

def check_username():
    for i in range(0,len(accounts)):
        if accounts[i]['username'] == usernameL:
            chckpass = check_password(i)
            if chckpass == 'Good':
                print('Logged in')
            else:
                print("No")

main()