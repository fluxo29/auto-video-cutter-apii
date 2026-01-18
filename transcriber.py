import whisper

def transcrever(video_path):
    model = whisper.load_model("base")
    result = model.transcribe(video_path)

    segmentos = []
    for seg in result["segments"]:
        segmentos.append({
            "inicio": seg["start"],
            "fim": seg["end"],
            "texto": seg["text"]
        })

    return segmentos
[
  {"inicio": 10.2, "fim": 14.8, "texto": "essa frase é importante"},
  ...
]
