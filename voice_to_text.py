import whisper

model = whisper.load_model("large")
result = model.transcribe("kayit_ses.m4a")
print(result["text"])
