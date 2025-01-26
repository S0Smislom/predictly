from common.admin import publish, unpublish
from django.contrib import admin

# Register your models here.
from .models import (
    AudioPrediction,
    ImagePrediction,
    Prediction,
    TextPrediction,
    VideoPrediction,
)


class ImagePredictionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "admin_image_thumbnail",
        "title",
        "file",
    )
    fields = ("admin_image", "title", "file")
    readonly_fields = ("admin_image",)
    actions = [publish, unpublish]
    model = ImagePrediction


class AudioPredictionAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "sound_display")
    readonly_fields = ("sound_display",)

    actions = [publish, unpublish]
    model = AudioPrediction


class VideoPredictionAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "video_display")
    readonly_fields = ("video_display",)
    model = VideoPrediction
    actions = [publish, unpublish]


class TextPredictionAdmin(admin.ModelAdmin):
    list_display = ("id", "text")
    actions = [publish, unpublish]


class PredictionAdmin(admin.ModelAdmin):
    list_display = ("id", "published", "content_type", "object_id", "content_object")
    # fields = ("pblished", "content_type", "object_id", "content_object")
    readonly_fields = ("content_object",)
    actions = [publish, unpublish]


admin.site.register(ImagePrediction, ImagePredictionAdmin)
admin.site.register(AudioPrediction, AudioPredictionAdmin)
admin.site.register(TextPrediction, TextPredictionAdmin)
admin.site.register(Prediction, PredictionAdmin)
admin.site.register(VideoPrediction, VideoPredictionAdmin)
