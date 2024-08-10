import pandas as pd
import os
from googleapiclient.discovery import build
youtube = build('youtube','v3',developerKey = '...')
pathSource = "..."
path = "..."
for an in range(1979,1980):
    dataFrame = pd.read_excel(os.path.join(pathSource,str(an)+'.xlsx'),header=1, engine='openpyxl')
    for index, row in dataFrame.iterrows():
        print("An: "+ str(an)+" row: "+ str(index))
        if((index !=0) and (dataFrame.at[index-1, 'Song'] == dataFrame.at[index,'Song'])):
            dataFrame.at[index,"VidId"] =  dataFrame.at[index-1,"VidId"]
        else:
            recherche = row['Song'] + " by "+row['Artist']+" Music video"
            request = youtube.search().list(
                q=recherche,
                part='id',
                maxResults=1,
                type='video'
                )
            response = request.execute()
            VidId = response['items'][0]['id']['videoId']
            dataFrame.at[index, "VidId"]=VidId
    
    dataFrame.to_excel(os.path.join(path,str(an)+'.xlsx'),index=False,engine='openpyxl')