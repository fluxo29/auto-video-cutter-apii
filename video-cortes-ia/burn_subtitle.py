import subprocess

def aplicar_legendas_animadas(video_in, blocos, video_out):
    filtros = []

    for b in blocos:
        filtros.append(
            f"drawtext=text='{b['texto'].upper()}':"
            "fontcolor=white:"
            "fontsize=64:"
            "box=1:"
            "boxcolor=black@0.6:"
            "boxborderw=20:"
            "x=(w-text_w)/2:"
            "y=h*0.75:"
            f"enable='between(t,{b['inicio']},{b['fim']})'"
        )

    filtro_final = ",".join(filtros)

    comando = [
        "ffmpeg",
        "-i", video_in,
        "-vf", filtro_final,
        "-codec:a", "copy",
        video_out
    ]

    subprocess.run(comando)
