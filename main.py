import asyncio
import edge_tts
import os
from moviepy.video.VideoClip import ColorClip, TextClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip

SCRIPT = "Psychology kehti hai ki jo log akele rehna pasand karte hain, unka dimaag baki logon se zyada creative hota hai. Wo bheed se nahi, balki apne khayalon se baatein karte hain."

async def generate_video():
    print("Mision Day 1: Final Push...")
    
    # 1. Voice
    communicate = edge_tts.Communicate(SCRIPT, "hi-IN-MadhurNeural")
    await communicate.save("voice.mp3")
    
    audio = AudioFileClip("voice.mp3")
    audio_duration = audio.duration

    # 2. Background (Fixed: Using duration parameter directly)
    bg = ColorClip(size=(1080, 1920), color=(15, 15, 15), duration=audio_duration)

    # 3. Text (Fixed: Using duration parameter directly)
    txt = TextClip(
        text=SCRIPT,
        font_size=70,
        color='yellow',
        method='caption',
        size=(900, None),
        duration=audio_duration
    ).with_position('center')

    # 4. Final Assemble
    final_video = CompositeVideoClip([bg, txt])
    final_video.audio = audio
    
    # 5. Export
    final_video.write_videofile("output_video.mp4", fps=24, codec="libx264", audio_codec="aac")
    print("MISSION ACCOMPLISHED: output_video.mp4 is ready!")

if __name__ == "__main__":
    asyncio.run(generate_video())
    
