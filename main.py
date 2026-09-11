import tasks
import affichage
import stockage
from fastapi import FastAPI,HTTPException
app = FastAPI(
    title='to-do-liste',
    description= 'API de gestion de donne de Mehdi',
    version='0.0.9'
    )


@app.get('/tache')
def obtenir_tache():
    return stockage.charger_tache()
@app.post('/tache')
def ajoute_tache(titre : str):
    mes_tasks = stockage.charger_tache()
    tasks.compter_tache(mes_tasks,titre)
    stockage.stockage(mes_tasks)
    return mes_tasks

@app.put('/tache/{id_tache}')
def terminer_tache(id_tache : int):
    mes_tasks = stockage.charger_tache()
    resultat = tasks.marque_tache(mes_tasks,id_tache)
    if resultat == False :
        raise HTTPException(status_code= 404 , detail= 'tache pas presente')
    else:
        stockage.stockage(resultat)
        return resultat

@app.delete('/tache/{id_tache}')
def efface_tache(id_tache : int):
    mes_tasks = stockage.charger_tache()
    resultat = tasks.supprimer_tache(mes_tasks,id_tache)
    if resultat == False :
        raise HTTPException(status_code= 404 , detail= 'tache pas presente')
    else:
        stockage.stockage(resultat)
        return resultat