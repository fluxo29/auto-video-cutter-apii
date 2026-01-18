import subprocess
import os

from subtitle import gerar_blocos_com_tempo
from burn_subtitle import aplicar_legendas_animadas

def cortar_video(video_path, cortes, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    for i, corte in enumerate(cortes):
        corte_path = f"{output_dir}/corte_{i}.mp4"
        final_path = f"{output_dir}/final_{i}.mp4"

        subprocess.run([
            "ffmpeg",
            "-i", video_path,
            "-ss", str(corte["inicio"]),
            "-to", str(corte["fim"]),
            "-vf", "scale=1080:1920",
            "-c:a", "copy",
            corte_path
        ])

        blocos = gerar_blocos_com_tempo(
            corte["inicio"],
            corte["fim"],
            corte["texto"]
        )

        aplicar_legendas_animadas(
            video_in=corte_path,
            blocos=blocos,
            video_out=final_path
        )
