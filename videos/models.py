from django.db import models

class Video(models.Model):
    
    LEVEL_CHOICES = [

        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),

    ]

    VIDEO_SOURCE_CHOICES = [
        ('local', 'Local'),
        ('youtube', 'YouTube'),
    ]
    
    STATUS_CHOICES = [

        ('processing', 'Processing'),

        ('ready', 'Ready'),

        ('error', 'Error'),

    ]
    
    title = models.CharField(
        max_length=255
    )
    
    description = models.TextField(
        blank=True,
        null=True
    )
    
    level = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )
    
    duration = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )
    
    thumbnail = models.ImageField(
        upload_to='thumbnails/',
        blank=True,
        null=True
    )
    
    subtitle_file = models.FileField(
        upload_to='subtitles/',
        blank=True,
        null=True
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    source_type = models.CharField(
        max_length=20,
        choices=VIDEO_SOURCE_CHOICES,
        default='local'
    )

    # LOCAL VIDEO
    video_file = models.FileField(
        upload_to='videos/',
        blank=True,
        null=True
    )
    
    # YOUTUBE
    youtube_url = models.URLField(
        blank=True,
        null=True
    )

    youtube_id = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )
    
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='processing'
    )
    
    word_count = models.IntegerField(
        default=0
    )

    def __str__(self):
        return self.title


class Vocabulary(models.Model):

    word = models.CharField(
        max_length=255
    )

    ipa = models.CharField(
        max_length=255,
        blank=True
    )

    original_sentence = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.word