from moviepy.editor import *  # * is used for importing everything
clip= VideoFileClip("video4.mp4")
duration=clip.duration
print("duration"+str(duration))
subclip=clip.subclip(0,duration/2)
subclip2=clip.subclip(duration/2,duration)
subclip.write_videofile("result.mp4")
subclip2.write_videofile("result2.mp4")