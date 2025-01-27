from django.contrib import admin


# Register your models here.
@admin.action(description="Publish")
def publish(modeladmin, request, queryset):
    queryset.update(published=True)


@admin.action(description="Unpublish")
def unpublish(modeladmin, request, queryset):
    queryset.update(published=False)


@admin.action(description="Create predictions")
def create_predictions(modeladmin, request, queryset):
    from app_prediction.models import Prediction
    from django.contrib.contenttypes.models import ContentType

    for _ in queryset:
        Prediction.objects.get_or_create(
            defaults={"published": False},
            content_type=ContentType.objects.get_for_model(queryset.model),
            object_id=_.id,
        )


@admin.action(description="Delete predictions")
def delete_predictions(modeladmin, request, queryset):
    from app_prediction.models import Prediction
    from django.contrib.contenttypes.models import ContentType

    Prediction.objects.filter(
        content_type=ContentType.objects.get_for_model(queryset.model),
        object_id__in=[_.id for _ in queryset],
    ).delete()
