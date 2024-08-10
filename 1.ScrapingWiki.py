
#https://www.youtube.com/watch?v=0FKOugdhExw&ab_channel=DatawithDylan
import pandas as pd
import ssl
import pywhatkit as pwk
import os

path = "..."
ssl._create_default_https_context = ssl._create_unverified_context
for an in range(1970,1980):
    anSTR = str(an)
    lien = 'https://en.wikipedia.org/wiki/List_of_number-one_singles_of_' + anSTR+'_(Canada)'
    tables = pd.read_html(lien)
    dataFrame=pd.DataFrame(tables[0])
    nomFichier= anSTR + ".xlsx"
    dataFrame.to_excel(os.path.join(path,nomFichier),index=False,engine='openpyxl')

#next: faire la recherche youtube et mettre le lien du premier résultat dans la table .xlsx, vas devoir lire le .xlsx déjà là et ajouter.