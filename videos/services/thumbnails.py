import os
import subprocess


def generate_thumbnail(

    video_path,

    thumbnail_path

):

    os.makedirs(

        os.path.dirname(
            thumbnail_path
        ),

        exist_ok=True
    )

    command = [

        'ffmpeg',

        '-i',

        video_path,

        '-ss',

        '00:00:03.000',

        '-vframes',

        '1',

        thumbnail_path

    ]

    subprocess.run(

        command,

        stdout=subprocess.DEVNULL,

        stderr=subprocess.DEVNULL

    )

    return thumbnail_path