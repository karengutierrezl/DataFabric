#python3 app01.py

import json

def run_app() :
    # STEP 1
    with open('DD.json', 'r') as file:
        dd_data = json.load(file)

    with open('roles.json', 'r') as file:
        roles_data = json.load(file)

    with open('users.json', 'r') as file:
        users_data = json.load(file)


    print(dd_data)
    print(roles_data)
    print(users_data)


if True:
    run_app()