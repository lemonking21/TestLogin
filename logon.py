import json
import re

accounts = []
password =''
username =''


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
    check_user()

def set_username(name):
    global username
    username = name

def get_password():
    passw = input("Password must contain at least eight characterswith at least one Uppercase, one Lower case and one Number\nEnter Password")
    accept_pas =condition(passw,'[a-zA-Z0-9]')
    if accept_pas == '1':
        set_password(passw)
        print('pass has been accepted')

def set_password(passw):
    global password
    password = passw

def record_setup():
    global username, password
    account = { 'username': username, 'password': password, 'accountid' : len(accounts)}
    return account

def write_write_to_file():
    account = record_setup()
    with open('jsontest.json', 'a') as outf:
        json.dump(account,outf)
        outf.write('\n')
    print('New account created!!')
    opeing_menu()


def readfromFile():
    global accounts
    with open('jsontest.json','r') as data_file:
        for x in data_file:
            accounts.append(json.loads(x))

def loggedin():
    readfromFile()
    usernameL =input("Enter your username")
    passwordL =input("Enter your password")
    check_username(usernameL, passwordL)

def check_password(i, passwordL):
    if accounts[i]['password']==passwordL:
        return 'Good'

def check_username(usernameL,passwordL):
    x = len(accounts)
    for i in range(0, x):
        if accounts[i]['username'] == usernameL:
            chckpass = check_password(i, passwordL)
            if chckpass == 'Good':
                print('Logged in')
                opeing_menu()
            else:
                print('Not the correct log in info!!!')

def check_user():
    if 'jsontest.json':
        readfromFile()
        account = record_setup()
        print(account)
        print(len(accounts))
        for record in range(0,len(accounts)):
            if account['username'] == accounts[record]['username']:
                print(account['username'])
                print(accounts[record]['username'])
                if account['password'] == accounts[record]['password']:
                    print('\n***************************************\nThis user already exists in the system\n***************************************\n')
                    get_username()
        write_write_to_file()           
    else:
        print('New Record')

def opeing_menu():
    i = 0
    while i != 3:
        print("###########################################")
        print("######Welcome to my first Sign in program!!")
        print("##We store your username and password here!")
        print("See the below options to navigate the Menu!")
        print("###Enter the number of what you wish to do!")
        print("1 -New user setup")
        print("2 -Log in to your account")
        print("3 -Close the program")
        print("###########################################")
        i =int(input("Type here >>"))
        if i == 1:
            get_username()
        if i == 2:
            loggedin()
        if i == 3:
            print("Good Bye")
def main():
    opeing_menu()

main()