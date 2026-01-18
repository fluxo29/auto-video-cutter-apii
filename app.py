from fastapi import FastAPI
from cutter import cortar_video

app = FastAPI()

@app.post("/cortar")
def cortar():
    cortes = [
        {
            "inicio": 2,
            "fim": 8,
            "texto": "isso aqui vai virar um corte viral"
        }
    ]

    cortar_video(
        video_path="video.mp4",
        cortes=cortes,
        output_dir="outputs"
    )

    return {"status": "ok"}
