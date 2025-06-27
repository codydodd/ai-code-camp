import whisper

# Load the base Whisper model
model = whisper.load_model("base")

# Transcribe an audio file (e.g., test.mp3)
result = model.transcribe("simple_convo.mp3")

# Print the transcribed text
print(f"The transcribed text: {result['text']}")