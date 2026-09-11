def compter_tache(nombre_tache,titre):
    nouvelle_tache = {"id" : len(nombre_tache)+1, "titre" : (titre), "fait": False}
    nombre_tache.append(nouvelle_tache)
    return nombre_tache
def valider_tache(nombre_tache,id_cible):
    for tache in nombre_tache :
        if tache['id'] == id_cible :
            tache['fait'] = True
def marque_tache(liste_tache,id_tache):
    trouve = False
    for tache in liste_tache:
        if id_tache == tache['id']:
            tache['fait'] = True
            trouve = True
    if trouve == False:
        return False
    else:
     return liste_tache

def supprimer_tache(liste_tache,id_tache):
    trouve = False
    for tache in liste_tache:
        if id_tache == tache['id']:
            liste_tache.remove(tache)
            trouve = True
            break
    if trouve == False:
        return False
    else:
     return liste_tache
    
