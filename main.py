import asyncio
import edge_tts
import subprocess

SCRIPT = "Psychology kehti hai ki jo log akele rehna pasand karte hain, unka dimaag baki logon se zyada creative hota hai."

async def make_video():
    print("Step 1: Making Audio...")
    communicate = edge_tts.Communicate(SCRIPT, "hi-IN-MadhurNeural")
    await communicate.save("voice.mp3")

    print("Step 2: Making Video with FFmpeg (The Jugad)...")
    # Ye command seedha black background aur text overlay banayega
    cmd = (
        f"ffmpeg -f colorspace -f lavfi -i color=c=black:s=1080x1920:d=10 "
        f"-i voice.mp3 "
        f"-vf \"drawtext=text='{SCRIPT}':fontcolor=yellow:fontsize=50:x=(w-text_w)/2:y=(h-text_h)/2:fix_bounds=1\" "
        f"-c:v libx264 -c:a aac -shortest output_video.mp4 -y"
    )
    
    subprocess.run(cmd, shell=True)
    print("DONE! output_video.mp4 is ready.")

if __name__ == "__main__":
    asyncio.run(make_video())
    
