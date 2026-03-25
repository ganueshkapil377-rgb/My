import asyncio
import edge_tts
import subprocess

async def create_video():
    print("Making Audio...")
    txt = "Psychology kehti hai ki akele rehne waale log zyada creative hote hain. Wo bheed se nahi, apne khayalon se baatein karte hain."
    
    communicate = edge_tts.Communicate(txt, "hi-IN-MadhurNeural")
    await communicate.save("voice.mp3")

    print("Making Video with FFmpeg...")
    # Seedha command jo black screen aur yellow text banayega
    cmd = [
        "ffmpeg", "-y",
        "-f", "lavfi", "-i", "color=c=0x0F0F0F:s=1080x1920:d=10",
        "-i", "voice.mp3",
        "-vf", "drawtext=text='Psychology says\\: Loners are Creative':fontcolor=yellow:fontsize=60:x=(w-text_w)/2:y=(h-text_h)/2",
        "-c:v", "libx264", "-c:a", "aac", "-shortest", "output_video.mp4"
    ]
    
    subprocess.run(cmd)
    print("SUCCESS: Pilot, video ready!")

if __name__ == "__main__":
    asyncio.run(create_video())
    
