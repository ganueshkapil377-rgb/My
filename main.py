import asyncio
import edge_tts
import os
from moviepy.video.VideoClip import ColorClip, TextClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip

SCRIPT = "Psychology kehti hai ki jo log akele rehna pasand karte hain, unka dimaag baki logon se zyada creative hota hai."

async def generate_video():
    print("Mission Day 1: Final Attempt...")
    
    # Audio Generation
    communicate = edge_tts.Communicate(SCRIPT, "hi-IN-MadhurNeural")
    await communicate.save("voice.mp3")
    
    audio = AudioFileClip("voice.mp3")
    audio_duration = audio.duration

    # Background - Fix: v2 uses duration= instead of with_duration()
    bg = ColorClip(size=(1080, 1920), color=(15, 15, 15), duration=audio_duration)

    # Text Overlay - Fix: same here
    txt = TextClip(
        text=SCRIPT,
        font_size=80,
        color='yellow',
        method='caption',
        size=(900, None),
        duration=audio_duration
    ).with_position('center')

    # Assembly
    final_video = CompositeVideoClip([bg, txt])
    final_video.audio = audio
    
    final_video.write_videofile("output_video.mp4", fps=24, codec="libx264", audio_codec="aac")
    print("SUCCESS: Video is ready!")

if __name__ == "__main__":
    asyncio.run(generate_video())
    
