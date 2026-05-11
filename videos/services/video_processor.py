import os

from background_task import background

from django.conf import settings

from videos.models import Video

from videos.services.transcription import (
    generate_srt
)

from videos.services.word_counter import (
    count_words
)

from videos.services.thumbnails import (
    generate_thumbnail
)

from videos.services.video_duration import (
    get_video_duration
)


@background(schedule=5)
def process_video(video_id):
    
    print(
        'START PROCESS:',
        video_id
    )

    try:

        video = Video.objects.get(
            id=video_id
        )

        video_path = video.video_file.path

        # DURATION

        video.duration = (

            get_video_duration(
                video_path
            )

        )

       # THUMBNAIL

        thumbnail_dir = os.path.join(

            settings.MEDIA_ROOT,

            'thumbnails'

        )

        os.makedirs(

            thumbnail_dir,

            exist_ok=True

        )
        video_filename = os.path.basename(
            video_path
        )

        name, _ = os.path.splitext(
            video_filename
        )

        thumbnail_filename = (
            f'{name}.jpg'
        )

        thumbnail_path = os.path.join(

            thumbnail_dir,

            thumbnail_filename

        )

        generate_thumbnail(

            video_path,

            thumbnail_path

        )


        video.thumbnail.name = (
            f'thumbnails/{thumbnail_filename}'
        )

        # SUBTITLE

        subtitles_dir = os.path.join(

            settings.MEDIA_ROOT,

            'subtitles'

        )

        os.makedirs(

            subtitles_dir,

            exist_ok=True

        )

        srt_filename = (
            f'{video.id}.srt'
        )

        srt_path = os.path.join(

            subtitles_dir,

            srt_filename

        )

        generate_srt(

            video_path,

            srt_path

        )

        video.subtitle_file.name = (
            f'subtitles/{srt_filename}'
        )

        # WORD COUNT

        with open(

            srt_path,

            'r',

            encoding='utf-8'

        ) as file:

            srt_text = file.read()

        video.word_count = count_words(
            srt_text
        )

        video.status = 'ready'

        video.save()

        print(
            f'Video {video.id} processed'
        )

    except Exception as error:

        print(error)

        video.status = 'error'

        video.save()