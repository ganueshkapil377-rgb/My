import asyncio
import edge_tts
from moviepy.video.VideoClip import ColorClip, TextClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip

SCRIPT = "Psychology kehti hai ki jo log akele rehna pasand karte hain, unka dimaag baki logon se zyada creative hota hai."

async def generate_video():
    print("Mission Day 1: Bulletproof Version...")
    
    # 1. Audio Generation
    communicate = edge_tts.Communicate(SCRIPT, "hi-IN-MadhurNeural")
    await communicate.save("voice.mp3")
    audio = AudioFileClip("voice.mp3")
    dur = audio.duration

    # 2. Background
    bg = ColorClip(size=(1080, 1920), color=(15, 15, 15)).with_duration(dur)

    # 3. Text (MoviePy v2.0 exact syntax: positional arguments only)
    # Humein 'text=' keyword nahi use karna hai v2 mein
    txt = TextClip(
        SCRIPT, 
        font_size=70, 
        color='yellow', 
        size=(900, None), 
        method='caption'
    ).with_duration(dur).with_position('center')

    # 4. Assembly
    final_video = CompositeVideoClip([bg, txt])
    final_video.audio = audio
    
    # Export
    final_video.write_videofile("output_video.mp4", fps=24, codec="libx264", audio_codec="aac")
    print("SUCCESS: Pilot, video is 100% ready!")

if __name__ == "__main__":
    asyncio.run(generate_video())
    
