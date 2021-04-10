import os
import sys
import time
import pathlib
import requests
import threading


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def rate_limit():
    try:
        os.system('cls')
        URL = f'https://api.github.com/rate_limit'
        f = open(resource_path('token.txt'), "r")
        token = f.read()
        headers = {'Authorization': 'token ' + str(token)}
        r = requests.get(url=URL, headers=headers)
        r_limit = r.json()
        x_limit = r_limit['rate']
        limit = x_limit['limit']
        remaining = x_limit['remaining']
        green = '\033[32m'
        endcolor = '\033[0m'
        print(
            f'TOKEN CHECK: {green}VALID{endcolor}\nRequests limit: {limit}\nRequests remains: {remaining}')
        time.sleep(3)
        main()
    except (KeyError, ValueError):
        try:
            os.system('cls')
            red = '\033[91m'
            yellow = '\033[93m'
            endcolor = '\033[0m'
            print(f'{red}INVALID TOKEN:{endcolor} {yellow}Your token is not valid{endcolor}')
            time.sleep(1)
            question = input(
                f'\nDo you still want to continue with an {red}invalid token{endcolor} ? [y/n/show token]: ').lower().strip(' ')
            if question == 'y':
                main()
            elif question == 'n':
                os.system('cls')
                auth()
            elif question == 'show token':
                print(token)
                time.sleep(5)
                rate_limit()
            else:
                rate_limit()
        except KeyboardInterrupt:
            keyboardinterrupt()

    except FileNotFoundError:
        try:
            os.system('cls')
            red = '\033[91m'
            yellow = '\033[93m'
            endcolor = '\033[0m'
            print(f'{red}AUTHENTICATION REQUIRED:{endcolor} {yellow}Please, tell me who you are{endcolor}')
            time.sleep(3)
            auth()
        except KeyboardInterrupt:
            keyboardinterrupt()
    except(requests.exceptions.ConnectionError):
        try:
            red = '\033[91m'
            endcolor = '\033[0m'
            print(f'{red}NO INTERNET CONNECTION{endcolor}')
            time.sleep(2)
            os.system('cls')
            main()
        except KeyboardInterrupt:
            keyboardinterrupt()
    except KeyboardInterrupt:
        keyboardinterrupt()


def auth():
    os.system('cls')
    yellow = '\033[93m'
    endcolor = '\033[0m'
    print(f'    {yellow}AUTHENTICATION PROCEDURE INITIATED{endcolor}')
    print('#----------------------------------------#')
    print('            [../] to main menu')
    print('             [help] for help')
    print('              [:q] for exit\n')
    token = input('Please, enter your GitHub token: ').lower().replace(' ', '')
    if token == ':q':
        os.system('cls')
        sys.exit()
    elif token == '../':
        rate_limit()
    elif token == 'help':
        os.system('cls')
        print('#-----------HELP----------#\n')
        print('IF YOU DONT KNOW WHAT IT IS:\n')
        print('1. Sign in or sign up on GitHub.com \n')
        print('2. Follow this link:\n')
        print('https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line#creating-a-token \n')
        print('3. Copy your token and paste it here\n')
        print('#-------------------------#')
        time.sleep(10)
        auth()
    else:
        # print(pathlib.Path(__file__).parent.absolute())
        os.system('cls')
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        print('Current program directory is:', base_path)
        path_choice = input(
            '\nShould I generate path myself or you will insert it manualy ? [man/auto]: ')
        if path_choice == 'man':
            try:
                os.system('cls')
                file_path = input('Insert the correct path to the program directory: ').strip(' ')
                f = open(f'{file_path}/token.txt', 'w')
                f.write(token)
                f.close()
                rate_limit()
            except FileNotFoundError:
                print('\nERROR: I see no such directory')
                time.sleep(2)
                os.system('cls')
                auth()
            except PermissionError:
                print(
                    '\nERROR: Due to OS settings, I have no permisson to write the file in the following directory')
                time.sleep(4)
                os.system('cls')
                auth()
        elif path_choice == 'auto':
            os.system('cls')
            f = open(resource_path('token.txt'), "w")
            f.write(token)
            f.close()
            print('File saved at', os.path.realpath(f.name))
            print('\nNew authentication try in 5 sec ')
            time.sleep(1)
            os.system('cls')
            print('File saved at', os.path.realpath(f.name))
            print('\nNew authentication try in 4 sec. ')
            time.sleep(1)
            os.system('cls')
            print('File saved at', os.path.realpath(f.name))
            print('\nNew authentication try in 3 sec.. ')
            time.sleep(1)
            os.system('cls')
            print('File saved at', os.path.realpath(f.name))
            print('\nNew authentication try in 2 sec... ')
            time.sleep(1)
            os.system('cls')
            print('File saved at', os.path.realpath(f.name))
            print('\nNew authentication try in 1 sec.... ')
            time.sleep(1)
            rate_limit()
        else:
            auth()


def main_menu():
    os.system('cls')
    red = '\033[91m'
    yellow = '\033[93m'
    endcolor = '\033[0m'
    print(f'''{yellow}
      //     ___ _ _   _  _      _       ___ _           _
      //    / __(_) |_| || |_  _| |__   / __| |_  ___ __| |_____ _ _
      //   | (_ | |  _| __ | || | '_ \ | (__| ' \/ -_) _| / / -_) '_|
      //    \___|_|\__|_||_|\_,_|_.__/  \___|_||_\___\__|_\_\___|_|
      //
                              #------------------#{endcolor}
                                 {red}[:q] for exit{endcolor}
                            {red}[:l] for current limits{endcolor}
                           {red}[:auth] for token settings{endcolor}\n''')
    name = input(f'{yellow}Enter user name:{endcolor} ').lower().strip(' ')
    if name == ':q':
        os.system('cls')
        sys.exit()
    elif name == ':l':
        rate_limit()
    elif name == ':auth':
        os.system('cls')
        print(f'{red}\nWARNING:{endcolor} {yellow}This is a system function{endcolor}')
        print(f'{yellow}You may loose your current token settings if you`ll mess up with input here{endcolor}')
        time.sleep(4)
        auth()
    else:
        return name


def github_checker(name):
    os.system('cls')
    URL = f'https://api.github.com/users/{name}'
    f = open(resource_path('token.txt'), "r")
    token = f.read()
    headers = {'Authorization': 'token ' + str(token)}
    r = requests.get(url=URL, headers=headers)
    user_data = r.json()
    status_code = r.status_code
    return(user_data, status_code)


def languages_checker(name):
    URL = f'https://api.github.com/users/{name}/repos'
    f = open(resource_path('token.txt'), "r")
    token = f.read()
    headers = {'Authorization': 'token ' + str(token)}
    r = requests.get(url=URL, headers=headers)
    user_repos = r.json()
    languages = [i['language']
                 for i in user_repos if i['language'] != None if i['language'] != 'Makefile']
    languages_counted = {
        i: f'{round(languages.count(i)/len(languages)*100, 2)}%' for i in set(languages)}
    return languages_counted


def email_in_commits(name):
    URL = 'https://functions.yandexcloud.net/d4ebb29c98cblsp0lgem'
    PARAMS = {'name': name}
    r = requests.post(url=URL, params=PARAMS)
    user_email = r.json()
    return user_email


def output(user_data, languages_counted, user_email):
    output = {'Username': user_data['login'],
              'Full Name': user_data['name'],
              'Email': user_data['email'],
              'Commit Email': user_email['message'],
              'Location': user_data['location'],
              'Company': user_data['company'],
              'Hireable Status': user_data['hireable'],
              'Languages': languages_counted,
              'Profile Summary': 'https://profile-summary-for-github.com/user/' + user_data['login'],
              'Profile Link': 'https://github.com/' + user_data['login']
              }
    red = '\033[91m'
    yellow = '\033[93m'
    endcolor = '\033[0m'
    print(f'{yellow}Username:{endcolor} ' + str(output['Username']))
    print(f'{yellow}Full Name:{endcolor} ' + str(output['Full Name']))
    print(f'#--------------------{yellow}CONTACTS{endcolor}----------------------------#')
    print(f'{red}Email:{endcolor} ' + str(output['Email']))
    print(f'{red}Commit Email:{endcolor} ' + str(output['Commit Email']))
    print(f'#---------------------{yellow}SKILS{endcolor}------------------------------#')
    print(f'{red}Languages:{endcolor} ' + str(output['Languages']))
    print(f'#---------------------{yellow}LINKS{endcolor}------------------------------#')
    print(f'{red}Profile Link:{endcolor} ' + str(output['Profile Link']))
    print(f'{red}Profile Summary:{endcolor} ' + str(output['Profile Summary']))
    print(f'#---------------------{yellow}OTHER{endcolor}------------------------------#')
    print(f'{red}Location:{endcolor} ' + str(output['Location']))
    print(f'{red}Company:{endcolor} ' + str(output['Company']))
    print(f'{red}Hireable Status:{endcolor} ' + str(output['Hireable Status']))


def animation(stop):
    red = '\033[91m'
    yellow = '\033[93m'
    endcolor = '\033[0m'
    while True:
        print(f'{yellow}Checking if user exists on GitHub{endcolor} {red}|{endcolor}')
        time.sleep(0.1)
        os.system('cls')
        print(f'{yellow}Checking if user exists on GitHub{endcolor} {red}/{endcolor}')
        time.sleep(0.1)
        os.system('cls')
        print(f'{yellow}Checking if user exists on GitHub{endcolor} {red}—{endcolor} ')
        time.sleep(0.1)
        os.system('cls')
        print(f'{yellow}Checking if user exists on GitHub{endcolor} {red}\\{endcolor}')
        time.sleep(0.1)
        os.system('cls')
        if stop():
            break


def backward():
    go_back = input('\nPress [any button]')
    if go_back:
        os.system('cls')
        main()
    else:
        os.system('cls')
        main()


def status(status_code):
    if status_code == 401:
        print('Invalid Token')
        time.sleep(2)
        os.system('cls')
        auth()
    elif status_code == 403:
        print('API rate limit exceeded')
        time.sleep(2)
        os.system('cls')
        main()
    elif status_code == 404:
        print("There is no such user on GitHub")
        time.sleep(2)
        os.system('cls')
        main()


def main():
    try:
        name = main_menu()
        user_data, status_code = github_checker(name)
        if status_code == 200:
            try:
                stop_threads = False
                t1 = threading.Thread(target=animation, args=(lambda: stop_threads, ))
                t1.start()
                languages_counted = languages_checker(name)
                user_email = email_in_commits(name)
                stop_threads = True
                t1.join()
                output(user_data, languages_counted, user_email)
                backward()
            except KeyboardInterrupt:
                stop_threads = True
                t1.join()
                keyboardinterrupt()
        else:
            status(status_code)
    except(requests.exceptions.ConnectionError):
        try:
            print('Please, check your internet connection ...')
            time.sleep(2)
            os.system('cls')
            main()
        except KeyboardInterrupt:
            keyboardinterrupt()
    except FileNotFoundError:
        auth()


def keyboardinterrupt():
    os.system('cls')
    print('Program killed by user')
    time.sleep(0.5)
    os.system('cls')
    sys.exit()


if __name__ == '__main__':
    rate_limit()
