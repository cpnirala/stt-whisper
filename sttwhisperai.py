import whisper

audio_file = "C:\Users\HP\Desktop\portfolio\vcard-personal-portfolio-master\whisperai\harvard.wav"

model = whisper.load_model("base")
result = model.transcribe(audio_file)
print("Trancribed Text:\n", result["text"])
with open("transcription.txt", "w", encoding="utf_8") as f:
    f.write(result["text"])