import ffmpeg

# ====================================
# VIDEO DURATION
# ====================================

def get_video_duration(video_path):

    probe = ffmpeg.probe(
        video_path
    )

    duration = float(
        probe['format']['duration']
    )

    minutes = int(
        duration // 60
    )

    seconds = int(
        duration % 60
    )

    return f'{minutes}:{seconds:02d}'

