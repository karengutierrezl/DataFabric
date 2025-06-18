#python3 app02.py

import json

def run_app() :
    # STEP 1
    with open('DD.json', 'r') as file:
        dd_data = json.load(file)

    with open('roles.json', 'r') as file:
        roles_data = json.load(file)

    with open('users.json', 'r') as file:
        users_data = json.load(file)


    # STEP 2
    user_name = input("Ingresa nombre de usuario: ")

    user_info = None
    for user in users_data['users']:
        if user.get('username').lower() == user_name.lower():
            print("El usuario tiene acceso!")
            user_info = user
            break
    print(user_info)


if True:
    run_app()