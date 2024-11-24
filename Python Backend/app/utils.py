import base64
import os
# from pydub import AudioSegment
import subprocess

def save_audio(audio_data):
    # Decode the base64 audio data
    audio_bytes = base64.b64decode(audio_data.split(",")[1])
    
    # Save the audio to a temporary file
    temp_file = "temp_audio.webm"
    with open(temp_file, "wb") as f:
        f.write(audio_bytes)
    
    # Convert WebM to WAV
    # audio = AudioSegment.from_file(temp_file, format="webm")
    wav_file = "temp_audio.wav"
    if os.path.exists(wav_file): # Remove the file if it exists 
        os.remove(wav_file)

    # audio.export(wav_file, format="wav")

    try:
        # Run ffmpeg command to convert WebM to WAV
        subprocess.run(
            ["ffmpeg", "-i", temp_file, wav_file],
            check=True,
            capture_output=True
        )
        print(f"Conversion successful: {wav_file}")
        os.remove(temp_file)
        return wav_file
    except subprocess.CalledProcessError as e:
        # Print any errors from ffmpeg
        print(f"Error during conversion: {e.stderr.decode()}")
        return None

def text_to_speech(text):
    # Implement text-to-speech functionality if needed
    pass
