#python3 app_01_05_completed.py
# install pandas = pip3 install pandas

import json
import pandas as pd
from pandas import ExcelFile


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
            print("El usuario tiene acceso.")
            user_info = user
            break

    if user_info is None:
        print("El usuario", user_name, "no tiene acceso.")
    # STEP 3
    else:
        # users.json data
        role_user = user_info.get("role") # se obtiene el role asignado al usario ("gral_user")
        dds = user_info.get("DDs") # Nombre de data dictionary que tiene acceso ("DD1","DD2")

        tag_role = None
        for role in roles_data["roles"]: # roles.json data
            if role.get('role') == role_user: # role_user = "gral_user" obtenido de user.json user "Alex" role
                tag_role = role.get("tag") # se obtiene solo el tag de roles.json tag = "Gral"
                break

        access_streaming_platforms = {} # Diccionario de datos para guardar el contenido que tiene el usuario
        for dd in dds: # iteramos la lista de los "Data Dictionaries" keys que tiene acceso "Alex"
            for access in dd_data[dd]: # Obtenemos de la fuente de datos dd.json con los accesos de "Alex"
                if access == tag_role:  # verificamos que se encuentre el  tag = "Gral" de "Alex"
                    """
                        obtenemos apartir del 'dd' que estamos iterando su list de objetos "Gral"
                        y es almacenado en un nuevo diccionario de datos solo con los accessos que tiene el usuario
                    """
                    access_streaming_platforms[dd] = dd_data[dd][access]

        # STEP 4
        col_access_netflix = []
        col_access_imdb = []
        for key in access_streaming_platforms:
            if key == 'DD1': # contenido de netflix
                netflix_data = access_streaming_platforms[key]
                for netflix in netflix_data:
                    col_access_netflix.append(netflix.get('golden_name'))
            if key == 'DD2':  # contenido de IMDb Top TV Series
                imdb_data = access_streaming_platforms[key]
                for imdb in imdb_data:
                    col_access_imdb.append(imdb.get('golden_name'))


        # STEP 5 (use pandas python library)
        # se obtiene dataframe con la lista de columnas de acceso de netflix y IMDb Top TV Series
        df_netflix = pd.read_csv("netflix.csv")
        df_access_netflix = df_netflix[col_access_netflix]
        print(df_access_netflix)

        df_imdb = pd.read_csv("IMDb Top TV Series.csv")
        df_imdb = df_imdb[col_access_imdb]
        print(df_imdb)



if True:
    run_app()