import asyncio
import edge_tts
import os
import requests
from moviepy import ColorClip, TextClip, AudioFileClip, CompositeVideoClip

# 1. Pilot's Viral Script
SCRIPT = "Psychology kehti hai ki jo log akele rehna pasand karte hain, unka dimaag baki logon se zyada creative hota hai. Wo bheed se nahi, balki apne khayalon se baatein karte hain."

async def generate_video():
    # Audio Generation
    print("Generating Audio...")
    communicate = edge_tts.Communicate(SCRIPT, "hi-IN-MadhurNeural")
    await communicate.save("voice.mp3")
    
    # Audio Load karein duration janne ke liye
    audio = AudioFileClip("voice.mp3")
    duration = audio.duration

    # 2. Background (Black Color Clip - Taaki error na aaye footage ka)
    # Baad mein hum Pexels API se real footage link karenge
    bg = ColorClip(size=(1080, 1920), color=(20, 20, 20)).with_duration(duration)

    # 3. Text Overlay (Captions)
    txt = TextClip(
        text=SCRIPT,
        font_size=70,
        color='yellow',
        method='caption',
        size=(900, None)
    ).with_duration(duration).with_position('center')

    # 4. Final Assembly
    final_video = CompositeVideoClip([bg, txt])
    final_video.audio = audio
    
    print("Exporting Video...")
    final_video.write_videofile("output_video.mp4", fps=24, codec="libx264", audio_codec="aac")

if __name__ == "__main__":
    asyncio.run(generate_video())
    
