import asyncio
import edge_tts
import os
from moviepy import ColorClip, TextClip, AudioFileClip, CompositeVideoClip

# 1. Pilot's Viral Script (Day 1 - Retention Hack)
SCRIPT = "Psychology kehti hai ki jo log akele rehna pasand karte hain, unka dimaag baki logon se zyada creative hota hai. Wo bheed se nahi, balki apne khayalon se baatein karte hain."

async def generate_video():
    print("Mision Day 1: Generating Content...")
    
    # Audio Generation
    communicate = edge_tts.Communicate(SCRIPT, "hi-IN-MadhurNeural")
    await communicate.save("voice.mp3")
    
    # Audio Load duration ke liye
    audio = AudioFileClip("voice.mp3")
    duration = audio.duration
    print(f"Audio Duration: {duration} seconds")

    # 2. Background (Black Color Clip with correct size)
    bg = ColorClip(size=(1080, 1920), color=(15, 15, 15)).with_duration(duration)

    # 3. Text Overlay (Captions)
    # Humein size aur position specifically batana padega v2 mein
    txt = TextClip(
        text=SCRIPT,
        font_size=80,
        color='yellow',
        method='caption',
        size=(900, None)
    ).with_duration(duration).with_position('center')

    # 4. Final Video Assembly
    print("Assembling Video Layers...")
    final_video = CompositeVideoClip([bg, txt])
    final_video.audio = audio
    
    # 5. Export
    print("Pilot, exporting the video to output_video.mp4...")
    final_video.write_videofile("output_video.mp4", fps=24, codec="libx264", audio_codec="aac")
    print("SUCCESS: Video file is ready for upload!")

if __name__ == "__main__":
    asyncio.run(generate_video())
    
