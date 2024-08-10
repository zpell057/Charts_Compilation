import pandas as pd
import os
from pytube import YouTube

pathSource = "..."
path = "..."
pathOutput = "..."

for an in range(1970,1980):
    dataFrame = pd.read_excel(os.path.join(pathSource,str(an)+'.xlsx'),header=0, engine='openpyxl')
    dataFrame["Téléchargement"] = "Non-tenté"
    for index, row in dataFrame.iterrows():
        print("An: "+ str(an)+" row: "+ str(index))
        if((index !=0) and (dataFrame.at[index-1, 'Song'] == dataFrame.at[index,'Song'])):    
            dataFrame.at[index,"Téléchargement"] =  dataFrame.at[index-1,"Téléchargement"]
        else:    
            lien = "https://www.youtube.com/watch?v=" + dataFrame.at[index, 'VidId']
            #print(lien)
            try:
                
                yt=YouTube(lien)
                yt=yt.streams.get_highest_resolution()
                nomFichier = dataFrame.at[index, 'Song'].strip('"')+".mp4"
                print(nomFichier)
                yt.download(output_path = pathOutput, filename = nomFichier)
                dataFrame.at[index,"Téléchargement"] = "Réussi"
                print("Réussi")
            except:
                dataFrame.at[index,"Téléchargement"] = "Échec"
                print("Échec")
    dataFrame.to_excel(os.path.join(path,str(an)+'.xlsx'),index=False,engine='openpyxl')
