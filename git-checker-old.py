#!/usr/bin/env python

import requests
import sys

#---------------------EXIT OPTION & LOOP-------------------------#
while True:

    name = input("Enter user name: ")
    if name == str("exit()"):
        sys.exit()
        
    else:
#-----------------GITHUB CHECKER & LIST APPENDER-----------------#
        print("Checking if user exists on GitHub ...")

        headers = {"Authorization": "token " + "d12a3a996bf3edae61ac53499efac8f22c989433"}      # and add: headers = {"Authorization": "Token " +  "yourabcdefgh0123token"}
        URL = "https://api.github.com/users/" + name
        r = requests.get(url = URL, headers = headers)
        user_data = r.json()
        keys = list(user_data.keys())
    
        if keys[0] != "message":       
            URL = "https://api.github.com/users/" + name + "/repos"
            r = requests.get(url = URL, headers = headers)
            user_repos = r.json()
            languages = [i["language"] for i in user_repos if i["language"] != None if i["language"] != "Makefile"] # add more langs != if needed
            languages_counted = {i: f"{round(languages.count(i)/len(languages)*100, 2)}%" for i in set(languages)}
            
#------------------GET EMAIL FROM COMMITS------------------------#
            URL = "https://functions.yandexcloud.net/d4ebb29c98cblsp0lgem"

            PARAMS = {"name":name}
            r = requests.post(url = URL, params = PARAMS)
            user_email = r.json()
            
#--------------------------FORM OUTPUT---------------------------#
            output = {'Username': user_data['login'], 'Full Name': user_data['name'], 'Email': user_data['email'], 'Additional Email': user_email['message'],
                        'Location': user_data['location'], 'Company': user_data['company'], 'Hireable Status': user_data['hireable'],
                        'Languages': languages_counted, 'Profile Summary': 'https://profile-summary-for-github.com/user/' + user_data['login']}
            print(output)
        
        else:
            print("There is no such user on GitHub")
