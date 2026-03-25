import asyncio
import edge_tts
import os
# Fix: Corrected import path for MoviePy v2
from moviepy.video.VideoClip import ColorClip, TextClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip

SCRIPT = "Psychology kehti hai ki jo log akele rehna pasand karte hain, unka dimaag baki logon se zyada creative hota hai."

async def generate_video():
    print("Mision Day 1: Generating Content...")
    communicate = edge_tts.Communicate(SCRIPT, "hi-IN-MadhurNeural")
    await communicate.save("voice.mp3")
    
    audio = AudioFileClip("voice.mp3")
    duration = audio.duration

    # Background
    bg = ColorClip(size=(1080, 1920), color=(15, 15, 15)).with_duration(duration)

    # Text Overlay
    txt = TextClip(
        text=SCRIPT,
        font_size=70,
        color='yellow',
        method='caption',
        size=(900, None)
    ).with_duration(duration).with_position('center')

    # Assembly
    final_video = CompositeVideoClip([bg, txt])
    final_video.audio = audio
    
    final_video.write_videofile("output_video.mp4", fps=24, codec="libx264", audio_codec="aac")
    print("SUCCESS: Video is ready!")

if __name__ == "__main__":
    asyncio.run(generate_video())
    
