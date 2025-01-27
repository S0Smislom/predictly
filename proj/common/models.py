from django.db import models

# Create your models here.


class ShowDefault(models.Model):
    title = models.CharField(max_length=120, null=True, blank=True)
    show_default = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def get_caption(self):
        if self.title:
            return self.title
        if self.show_default:
            return "Твое мем сказание"
