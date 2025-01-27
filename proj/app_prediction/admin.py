from common.admin import create_predictions, delete_predictions, publish, unpublish
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
    readonly_fields = ("admin_image", "width", "height", "thumbhash")
    actions = [publish, unpublish, create_predictions, delete_predictions]
    model = ImagePrediction


class AudioPredictionAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "sound_display")
    readonly_fields = ("sound_display",)

    actions = [publish, unpublish, create_predictions, delete_predictions]
    model = AudioPrediction


class VideoPredictionAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "video_display")
    readonly_fields = ("video_display",)
    model = VideoPrediction
    actions = [publish, unpublish, create_predictions, delete_predictions]


class TextPredictionAdmin(admin.ModelAdmin):
    list_display = ("id", "text")
    actions = [publish, unpublish, create_predictions, delete_predictions]


class PredictionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "published",
        "created_at",
        "content_type",
        "object_id",
        "content_object",
    )
    list_filter = [
        "published",
        "created_at",
        "content_type",
    ]
    readonly_fields = (
        "content_object",
        "created_at",
    )

    actions = [publish, unpublish]


admin.site.register(ImagePrediction, ImagePredictionAdmin)
admin.site.register(AudioPrediction, AudioPredictionAdmin)
admin.site.register(TextPrediction, TextPredictionAdmin)
admin.site.register(Prediction, PredictionAdmin)
admin.site.register(VideoPrediction, VideoPredictionAdmin)
