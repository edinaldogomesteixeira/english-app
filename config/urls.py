from django.contrib import admin

from django.urls import path

from django.conf import settings

from django.conf.urls.static import static

from videos.views import (

    home,
    video_detail,
    vocabulary,
    save_word,
    upload_video,

)

from videos import views

urlpatterns = [

    path(
        'admin/',
        admin.site.urls
    ),

    path(
        '',
        home,
        name='home'
    ),

    path(
        'video/<int:video_id>/',
        video_detail,
        name='video_detail'
    ),

    path(
        'vocabulary/',
        vocabulary,
        name='vocabulary'
    ),

    path(
        'save-word/',
        save_word,
        name='save_word'
    ),
    path(
        'upload-video/',
        upload_video,
        name='upload_video'
    ),
        path(
        'word/delete/<int:word_id>/',
        views.delete_word,
        name='delete_word'
    ),
    
    path(
    'delete-video/<int:video_id>/',
    views.delete_video,
    name='delete_video'
    ),

    path(
    'video-status/<int:video_id>/',
    views.video_status,
    name='video_status'
    ),

]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)