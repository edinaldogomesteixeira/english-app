import json
import os

import ffmpeg
import eng_to_ipa as ipa

from django.conf import settings

from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .utils.youtube import extract_youtube_id
from django.core.paginator import Paginator

from django.shortcuts import (

    render,
    redirect,
    get_object_or_404,

)

from .models import (

    Video,
    Vocabulary,

)


from .services.thumbnails import (
    generate_thumbnail
)

from .services.word_counter import (
    count_words
)

from .services.video_processor import (
    process_video
)

# ====================================
# HOME
# ====================================

def home(request):

    videos = Video.objects.all().order_by(
        '-created_at'
    )

    return render(

        request,

        'home.html',

        {
            'videos': videos
        }

    )


# ====================================
# VIDEO DETAIL
# ====================================

def video_detail(
    request,
    video_id
):

    video = get_object_or_404(

        Video,
        id=video_id

    )

    return render(

        request,

        'video_detail.html',

        {
            'video': video
        }

    )


# ====================================
# VOCABULARY
# ====================================

def vocabulary(request):

    words_list = Vocabulary.objects.all().order_by(
        '-created_at'
    )

    paginator = Paginator(
        words_list,
        10
    )

    page_number = request.GET.get(
        'page'
    )

    words = paginator.get_page(
        page_number
    )

    return render(

        request,

        'vocabulary.html',

        {
            'words': words
        }

    )
# ====================================
# SAVE WORD
# ====================================

def save_word(request):

    if request.method == 'POST':

        word = (

            request.POST.get(
                'word',
                ''
            )

            .strip()

            .lower()

        )

        sentence = (

            request.POST.get(
                'sentence',
                ''
            )

            .strip()

        )

        if word:

            existing_word = Vocabulary.objects.filter(
                word=word
            ).first()

            if not existing_word:

                try:

                    ipa_text = ipa.convert(
                        word
                    )

                except:

                    ipa_text = '-'

                Vocabulary.objects.create(

                    word=word,

                    ipa=ipa_text,

                    original_sentence=sentence,

                )

            return JsonResponse({

                'status': 'success',

                'word': word,

                'sentence': sentence

            })

    return JsonResponse({

        'status': 'error'

    })

def delete_word(request, word_id):

    word = get_object_or_404(
        Vocabulary,
        id=word_id
    )

    word.delete()
    page = request.POST.get('page', 1)

    return redirect(
        f'/vocabulary/?page={page}'
    )

# ====================================
# VIDEO YOUTUBE+LOCAL
# ====================================

def upload_video(request):
    print(request.POST)
    print(request.FILES)

    if request.method == 'POST':

        title = request.POST.get(
            'title'
        )

        description = request.POST.get(
            'description'
        )

        level = request.POST.get(
            'level'
        )

        video_file = request.FILES.get(
            'video_file'
        )

        if video_file:

            video = Video.objects.create(

                title=title or video_file.name,

                description=description,

                level=level,

                source_type='local',

                video_file=video_file,

                status='processing'
            )

            process_video(

                video.id,

                schedule=5

            )

    return redirect('home')

    #if request.method != 'POST':

    #    return redirect('home')

    # FORM DATA

    #title = request.POST.get(
    #    'title'
    #)

    #description = request.POST.get(
    #    'description'
    #)

    #level = request.POST.get(
    #    'level'
    #)

    #youtube_url = request.POST.get(
    #    'youtube_url'
    #)

    #video_file = request.FILES.get(
    #    'video_file'
    #)

    # =========================================================
    # YOUTUBE VIDEO
    # =========================================================

    #if youtube_url:

    #    youtube_id = extract_youtube_id(
    #        youtube_url
    #    )

    #    Video.objects.create(

    #        title=title or 'YouTube Video',

    #        description=description,

    #        level=level,

    #        source_type='youtube',

    #        youtube_url=youtube_url,

    #        youtube_id=youtube_id
    #    )

    #    return redirect('home')

    # =========================================================
    # LOCAL VIDEO
    # =========================================================

    #if video_file:

        # CREATE VIDEO

    #    video = Video.objects.create(

    #        title=title or video_file.name,

     #       description=description,

    #        level=level,

    #        source_type='local',

    #        video_file=video_file
    #    )

    #    process_video(
    #        video.id
    #    )

        #video_path = video.video_file.path

        # =====================================================
        # DURATION
        # =====================================================

        #video.duration = get_video_duration(
        #    video_path
        #)

        # =====================================================
        # THUMBNAIL
        # =====================================================

        #thumbnail_path = generate_thumbnail(
        #    video_path,
        #    None
        #)

        #video.thumbnail = thumbnail_path

        # =====================================================
        # SUBTITLES
        # =====================================================

        #subtitles_dir = os.path.join(

        #    settings.MEDIA_ROOT,

        #    'subtitles'
        #)

        #os.makedirs(

        #    subtitles_dir,

        #    exist_ok=True
        #)

        #srt_filename = (
        #    f'{video.id}.srt'
        #)

        #srt_path = os.path.join(

        #    subtitles_dir,

        #    srt_filename
        #)

        #from .services.transcription import (
        #    generate_srt
        #)

        #generate_srt(
        #    video_path,
        #    srt_path
        #)
        #with open(

        #    srt_path,

        #    'r',

        #    encoding='utf-8'

        #) as file:

        #    srt_text = file.read()

        #video.word_count = count_words(
        #    srt_text
        #)

        #video.subtitle_file.name = (
        #    f'subtitles/{srt_filename}'
        #)

        # SAVE
        #video.word_count = count_words(
        #    srt_text
        #)

        #video.save()

    #return redirect('home')

# =========================================================
# Delete CARD
# =========================================================
def delete_video(request, video_id):

    video = get_object_or_404(
        Video,
        id=video_id
    )

    if request.method == 'POST':

        video.delete()

    return redirect('home')

def video_status(request, video_id):

    video = Video.objects.get(
        id=video_id
    )

    return JsonResponse({

        'status': video.status,

        'thumbnail': (

            video.thumbnail.url

            if video.thumbnail

            else ''

        ),

        'duration': video.duration,

        'word_count': video.word_count

    })