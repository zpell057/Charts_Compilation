from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, concatenate_videoclips, ColorClip
path = "..."
Output = ColorClip((1920,1080),(0,0,0),duration = 0.1)
for an in range(1972,1980):
    video = VideoFileClip(path + str(an)+".mp4")
    Output = concatenate_videoclips([Output, video])
Output.write_videofile(path+"charts 1970s"+".mp4", codec="libx264")