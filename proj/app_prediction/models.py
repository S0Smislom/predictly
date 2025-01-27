from asgiref.sync import sync_to_async
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.safestring import mark_safe
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import SmartResize
from PIL import Image as PImage
from thumbhash import image_to_thumbhash

# Create your models here.


class Prediction(models.Model):
    published = models.BooleanField(default=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pk} {self.published} {self.content_type} {self.object_id}"

    @sync_to_async
    def aget_content_object(self):
        return self.content_object

    class Meta:
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
        ]


class TextPrediction(models.Model):
    text = models.TextField()

    def __str__(self) -> str:
        return self.text


class ImagePrediction(models.Model):
    title = models.CharField(max_length=120, null=True, blank=True)
    file = ProcessedImageField(
        upload_to="images/%Y/%m/%d/", format="WEBP", options={"quality": 100}
    )
    file_thumbnail = ImageSpecField(
        source="file",
        processors=[SmartResize(100, 100)],
        format="WEBP",
        options={"quality": 80},
    )
    height = models.IntegerField(blank=True, null=True, verbose_name="Высота")
    width = models.IntegerField(blank=True, null=True, verbose_name="Ширина")
    thumbhash = models.TextField(
        max_length=100,
        blank=True,
        null=True,
    )

    def admin_image(self):
        tag = f"<img src='{self.file.url}'"
        if self.width > 480:
            tag += " width='480'"
        if self.height > 540:
            tag += " height='540'"
        tag += " />"
        return mark_safe(tag)

    admin_image.allow_tags = True
    admin_image.short_description = "Превью"

    def admin_image_thumbnail(self):
        return mark_safe(f"<img src='{self.file_thumbnail.url}' width='160' />")

    admin_image_thumbnail.allow_tags = True
    admin_image_thumbnail.short_description = "Превью"

    def save(self, *args, **kwargs):
        image = PImage.open(self.file.file)
        self.thumbhash = image_to_thumbhash(image)
        self.width = image.size[0]
        self.height = image.size[1]
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.file.name


class AudioPrediction(models.Model):
    title = models.CharField(max_length=120, null=True, blank=True)
    file = models.FileField(upload_to="audio/")

    # @property
    def sound_display(self):
        return mark_safe(
            f'<audio controls name="media"><source src="{self.file.url}" type="audio/mpeg"></audio>'
        )

    sound_display.short_description = "sound"
    sound_display.allow_tags = True

    def __str__(self) -> str:
        return self.file.name


class VideoPrediction(models.Model):
    title = models.CharField(max_length=120, null=True, blank=True)
    file = models.FileField(upload_to="video/")

    def video_display(self):
        return mark_safe(
            f"""<video width="320" height="240" controls>
  <source src="{self.file.url}">
</video>"""
        )

    video_display.short_description = "video"
    video_display.allow_tags = True

    def __str__(self):
        return self.file.name
