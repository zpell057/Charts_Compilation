import pandas as pd
import os
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, concatenate_videoclips, ColorClip
pathInput = "D:/2nd disk/code/python/vidéos/"
pathOutput = "D:/2nd disk/code/python/vidéos/output/"
pathSource = "D:/2nd disk/code/python/dataframes/top charts Canada 1970s downloads"

#Output = ColorClip((1920,1080),(0,0,0),duration = 0.1)

for an in range(1970,1980):
    Output = ColorClip((1920,1080),(0,0,0),duration = 0.1)
    dataFrame = pd.read_excel(os.path.join(pathSource,str(an)+'.xlsx'),header=0, engine='openpyxl')
    dataFrame["Téléchargement"] = "Non-tenté"
    DébutTop=""
    FinTop=""
    NouvelleToune=True
    for index, row in dataFrame.iterrows():
        print("An: "+ str(an)+" row: "+ str(index))
        if(NouvelleToune):
            DébutTop = dataFrame.at[index,"Issue Date(s)"]
            NouvelleToune=False
        if((index == len(dataFrame)-1) or (dataFrame.at[index,"Song"] !=dataFrame.at[index+1,"Song"])):#Regarder si c'est la fin
            NouvelleToune=True
            #Faire le clip et l'intégrer
            video = VideoFileClip(pathInput + dataFrame.at[index,"Song"].strip('"')+".mp4")
            subClip = video.subclip(video.duration/2,video.duration/2+10).resize(newsize=(1920,1080)).set_fps(20)
            #subClip = subClip.resize(1920,1080)
            text1 = TextClip((dataFrame.at[index,"Song"] + " by " + dataFrame.at[index, "Artist"]),fontsize=90,color='black',stroke_color = 'white',stroke_width = 3)
            text1 = text1.set_duration(10)
            text1 = text1.set_pos(("left","top"))
            text2 = TextClip(("#1 from "+DébutTop + " to " + dataFrame.at[index, "Issue Date(s)"] +" "+ str(an)),fontsize=60,color='black',stroke_color = 'white',stroke_width = 3)
            text2 = text2.set_duration(10)
            text2 = text2.set_pos(("left","bottom"))
            clip = CompositeVideoClip([subClip,text1,text2])
            Output = concatenate_videoclips([Output, clip])
        if((index !=0) and (dataFrame.at[index-1, 'Song'] == dataFrame.at[index,'Song'])):    
            dataFrame.at[index,"Téléchargement"] =  dataFrame.at[index-1,"Téléchargement"]
    Output.write_videofile(pathOutput+str(an)+".mp4", codec="libx264")