from moviepy import VideoFileClip

# Load your video file
clip1 = VideoFileClip("media/videos/main/480p15/tCircle.mp4")
clip2 = VideoFileClip("media/videos/main/480p15/LatticeTranslation.mp4")

# Optional: Resize, trim, or set duration
# clip = clip.subclip(0, 5)  # first 5 seconds only
# clip = clip.resize(0.5)    # 50% size

# Export to GIF
#clip.write_gif("media/.gif", fps=15)
clip1.write_gif("media/gifs/tCircle.gif")
clip2.write_gif("media/gifs/LatticeTranslation.gif")