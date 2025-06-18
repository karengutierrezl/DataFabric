#python3 app03.py

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
    user_name = input("Ingresa nombre de usuario: ") # Input ejemplo: Alex

    user_info = None
    for user in users_data['users']:
        if user.get('username').lower() == user_name.lower():
            print("El usuario tiene acceso!")
            user_info = user
            break
    #print(user_info)

    # STEP 3
    if user_info:
        # users.json data
        role_user = user_info.get("role") # se obtiene el role asignado al usario ("gral_user")
        dds = user_info.get("DDs") # Nombre de data dictionary que tiene acceso ("DD1","DD2")

        tag_role = None
        for role in roles_data["roles"]: # roles.json data
            if role.get('role') == role_user: # role_user = "gral_user" obtenido de user.json user "Alex" role
                tag_role = role.get("tag") # se obtiene solo el tag de roles.json tag = "Gral"
                break

        tag_role_dd1 = None
        if "DD1" in dds: # DD.json
            for access in dd_data['DD1']:
                if access == tag_role: # "Gral"
                    tag_role_dd1 = access # acceso json nodo objetos catalogo de series
                    break

        data_dd1_role = dd_data["DD1"][tag_role_dd1] # se obtiene nodo con el acceso permitido "Gral"

        print(data_dd1_role)

if True:
    run_app()