import os
import json
FICHER = 'tache.json'
def stockage(nombre_tache):
    with open(FICHER,'w') as f :
        json.dump(nombre_tache,f)

def charger_tache():
    if os.path.exists(FICHER) == True:
        with open(FICHER,'r') as f :
            return json.load(f)
    else:
        return []