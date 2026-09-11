def afficher_taches(liste_taches):
    for tache in liste_taches:
        print(f"tache {tache['id']}: {tache['titre']} : {'fait' if tache['fait'] else 'pas fait'}")