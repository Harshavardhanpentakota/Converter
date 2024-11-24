from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import speech_recognition as sr
import google.generativeai as genai
import os
import urllib.parse
import time
import requests
from .utils import save_audio

from dotenv import load_dotenv
load_dotenv()


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Initialize Groq client with the API key
genai.configure(api_key=os.environ["API_KEY"])
gemini_model = genai.GenerativeModel('gemini-1.5-pro')

class AudioData(BaseModel):
    audio_data: str

class ImagePrompt(BaseModel):
    prompt: str

class PromptRequest(BaseModel):
    text: str

# Add this new model
class FreeImagePrompt(BaseModel):
    prompt: str
    image_path: str

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/transcribe")
async def transcribe_audio(audio_data: AudioData):
    try:
        # Save the audio data to a file
        audio_file = save_audio(audio_data.audio_data)

        # Transcribe the audio
        recognizer = sr.Recognizer()
        with sr.AudioFile(audio_file) as source:
            audio = recognizer.record(source)
        text = recognizer.recognize_google(audio)

        return JSONResponse(content={"text": text})
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/generate_prompt")
async def generate_prompt(prompt_request: PromptRequest):
    try:
        text = prompt_request.text
        chat = gemini_model.start_chat()
        prompttext = f'''This is a programmatically generated input. Perform the following tasks for the given input.
                        Generate a detailed prompt for an instruction which is : "{text}".
                        keep it short and precise.
                        Image generated from the prompt should clearly describe the instruction visually.
                        Response should only be the image prompt and nothing else'''
        response2 = chat.send_message(prompttext)
        final_subtitles = "".join(part.text for candidate in response2.candidates for part in candidate.content.parts)

        return JSONResponse(content={"prompt": final_subtitles})
    except Exception as e:
        print(f"Error generating prompt: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    
def download_image(image_url, image_name):
    try:
        response = requests.get(image_url, stream=True)
        if response.status_code == 200:
            with open(image_name, 'wb') as out_file:
                out_file.write(response.content)
        else:
            print("Error:", response.status_code)
    except Exception as e:
        print(f"Error downloading image: {str(e)}")

@app.post("/generate_image")
async def generate_image(image_prompt: ImagePrompt):
    try:
        prompt = image_prompt.prompt
        print(f"Received prompt: {prompt}")

        # Encode the prompt for URL safety
        encoded_prompt = urllib.parse.quote(prompt)
        # Generate the image URL for Pollinations AI
        image_url = f"https://pollinations.ai/p/{encoded_prompt}?width=1280&height=1280&seed=-1&model=flux-realism&nologo='true'"
        
        # Generate and download the image
        image_name = f"generated_image_{int(time.time())}.jpg"
        download_image(image_url, image_name)

        return JSONResponse(content={"image_url": image_url, "filename": image_name})
    except Exception as e:
        print(f"Error generating image: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)